import numpy as np

class RICO:
    """
    Based on KNMI's synthesis of the RICO field compaign for a LES intercomparison study

    http://projects.knmi.nl/rico/setup3d.html

    OBS: The sea surface temperature is different from the temperature at z=0m,
    which is necessary to have surface fluxes.
    """
    SCITATION_REF = "vanZanten et al 2011"

    def __init__(self, include_wind=True):
        self.include_wind = include_wind
        if include_wind:
            self.u_wind = self._u_wind
            self.v_wind = self._v_wind
        else:
            self.u_wind = lambda z: np.zeros_like(z)
            self.v_wind = lambda z: np.zeros_like(z)

        # surface conditions
        self.ps = 101540.  # [Pa], surface pressure
        self.p0 = 100000. # [Pa], reference pressure
        self.Ts = 299.8  # [K], sea surface temperature

        # constants
        self.Lv = 2.5e6  # [J/kg]
        self.c_p = 1005. # [J/kg/K]
        self.g = 9.81    # [m/s^2]
        self.R_d = 287.  # [J/kg/K]

        self.z_max = 4e3

        self._create_profile()

    def q_t(self, z):
        """ Total water specific concentration [kg/kg]"""
        return self._q_t(z)/1000.

    @np.vectorize
    def _q_t(z):
        if 0 <= z < 740:
            return 16.0 + (13.8 - 16.0) / (740) * z
        if 740 < z < 3260:
            return 13.8 + (2.4 - 13.8) / (3260 - 740)*(z - 740)
        else:
            return 2.4 + (1.8 - 2.4)/(4000 - 3260)*(z - 3260) 

    @np.vectorize
    def theta_l(z):
        """ Liquid water potential temperature [K]"""
        if 0 <= z < 740:
            return 297.9
        else:
            return 297.9 + (317.0 - 297.9)/(4000 - 740) *(z - 740)

    @np.vectorize
    def _u_wind(z):
        """
        u-component of wind
        """
        if z > 0.0:
            return -9.9 + 2.0e-3*z
        else:
            return 0.0


    @np.vectorize
    def _v_wind(z):
        """
        v-component of wind
        """
        if z > 0.0:
            return -3.8 
        else:
            return 0.0

    @np.vectorize
    def ddt_theta_l__ls(z):
        """
        Large Scale Horizontal Liq. Water Pot. Temperature Advection combined
        with Radiative Cooling [K/s] 

        NB: Initial profile contains no liquid water so `temp = pot. temp`
        """
        if z > 0:
            return -2.5 / 86400
        else:
            return 0.0

    @np.vectorize
    def ddt_qv_ls(z):
        """
        Large Scale Horizontal Moisture Advection [(kg/kg)/s]

        NB: not exactly as the KNMI website because we want to return tendencies
        in kg/kg/s, not g/kg/s
        """
        if 0 < z <= 2980:
            return (-1.0 / 86400 + (1.3456/ 86400) * z / 2980) * 1.0e-3
        elif z > 2980:
            return 4.*1.0e-6  * 1.0e-3
        else:
            return 0.0

    @np.vectorize
    def w_subsidence(z):
        """
        Large Scale Subsidence w [m/s] Apply the subsidence on the prognostic fields of q_t, theta_l.
        """
        if 0 < z < 2260:
            return - (0.005/2260) * z
        else:
            return - 0.005

    @np.vectorize
    def tke(z):
        """Initial subgrid profile of subgrid TKE"""
        return  1 - z/4000

    def _create_profile(self):
        """ Create a vertical profile that we can interpolate into later. 
        Integrating with the hydrostatic assumption.
        """
        try:
            from pyclouds import parameterisations
        except ImportError:
            warning.warn("pyclouds module couldn't be found, can't create"
                    "profile for interpolation of rho, T, RH and p")
            return

        parameterisation = parameterisations.SaturationVapourPressure()

        # XXX: R_v and cp_v are not given in the RICO test definition on the
        # the KNMI site I will use what I believe are standard values here
        self.R_v = parameterisations.common.default_constants.get('R_v')
        self.cp_v = parameterisations.common.default_constants.get('cp_v')

        dz = 100.
        R_d = self.R_d

        R_v = self.R_v
        R_d = self.R_d
        cp_d = self.c_p
        cp_v = self.cp_v

        z = 0.0
        p = self.ps

        # Cathy suggested using the liquid water potential temperature as the
        # temperature in the first model level
        T = self.theta_l(0.0)

        profile = []

        n = 0
        while z < self.z_max:
            qt = self.q_t(z)

            # assume no liquid water
            ql = 0.0
            qv = qt

            qd = 1.0 - qt

            theta_l = self.theta_l(z)

            R_l = R_d*qd + R_v*qv
            c_l = cp_d*qd + cp_v*qv

            T = theta_l/((self.p0/p)**(R_l/c_l))
            # T = self.iteratively_find_temp(theta_l=theta_l, p=p, q_t=qt, q_l=ql, T_initial=T)

            rho = 1.0/((qd*R_d + qv*R_v)*T/p) # + 1.0/(ql/rho_l), ql = 0.0

            profile.append((z, rho, p, T))

            # integrate pressure
            z += dz
            p += - rho * self.g * dz

            n += 1

        self._profile = np.array(profile)

    def iteratively_find_temp(self, theta_l, p, q_t, q_l, T_initial):
        R_v = self.R_v
        R_d = self.R_d
        cp_d = self.c_p
        cp_v = self.cp_v

        p0 = self.p0
        omega_l = 1.0
        L_v = self.Lv

        R_l = R_d*(1.0 - q_t) + R_v*q_t
        c_l = cp_d*(1.0 - q_t) + cp_v*q_t

        C = R_l/c_l*np.log(p0/p) + np.log(omega_l) - np.log(theta_l)

        theta_l_f = lambda T: T*(p0/p)**(R_l/c_l)*omega_l*np.exp(- L_v * q_l /( c_l * T))

        f = lambda T: C + np.log(T) - L_v*q_l/(c_l*T)
        T = scipy.optimize.brentq(f, 1., 410.)

        if np.isnan(T):
            raise Exception("Integration failed")

        if not np.abs(theta_l_f(T) - theta_l) < 1.0e-10:
            print theta_l_f(T), theta_l, np.abs(theta_l_f(T) - theta_l) 

        return T

    def _get_value_from_precomputed_profile(self, pos, var_indx):
        z = self._profile[:,0]
        if np.any(z > self.z_max):
            raise Exception("RICO test case is only defined for z < 7km")
        T = self._profile[:,var_indx]
        return np.interp(pos, z, T)

    def rho(self, pos):
        return self._get_value_from_precomputed_profile(pos, 1)

    def p(self, pos):
        return self._get_value_from_precomputed_profile(pos, 2)

    def temp(self, pos):
        return self._get_value_from_precomputed_profile(pos, 3)

    def rel_humidity(self, z):
        q_v = self.q_t(z)
        p = self.p(z)
        T = self.temp(z)

        from pyclouds import parameterisations
        parameterisation = parameterisations.SaturationVapourPressure()

        qv_sat = parameterisation.qv_sat(T=T, p=p)

        return q_v/qv_sat

    def __str__(self):
        return "RICO, LES test case from KNMI (%s wind)" % ['without', 'with'][self.include_wind]
