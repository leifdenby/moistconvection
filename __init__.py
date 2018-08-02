
class BaseCase:
    """
    Base case class. __doc__ here shold contain description of case
    """
    SCITATION_REF = "someAuthor et al 1970"
    FORCING_IS_TIME_DEPENDENT = False


    # initial conditions

    def q_t(self, z):
        """ Total water specific concentration [kg/kg]"""
        raise NotImplementedError

    @np.vectorize
    def theta_l(z):
        """ Liquid water potential temperature [K]"""
        raise NotImplementedError

    @np.vectorize
    def tke(z):
        """Initial subgrid profile of subgrid TKE"""
        raise NotImplementedError


    # forcings below

    def lh_surf_flux(self, t):
        """
        Surface latent heat flux in [W/m^2]
        """
        raise NotImplementedError

    def sh_surf_flux(self, t):
        """
        Surface latent heat flux in [W/m^2]
        """
        raise NotImplementedError


    @np.vectorize
    def ddt_theta_l__ls(t, z):
        """
        Large Scale Horizontal Liq. Water Pot. Temperature Advection combined
        with Radiative Cooling [K/s]
        """
        raise NotImplementedError

    @np.vectorize
    def ddt_qv_ls(t, z):
        """
        Large Scale Horizontal Moisture Advection [(kg/kg)/s]
        """
        raise NotImplementedError

    @np.vectorize
    def w_subsidence(t, z):
        """
        Large Scale Subsidence w [m/s] Apply the subsidence on the prognostic
        fields of q_t, theta_l.
        """
        raise NotImplementedError

    def rho(self, pos):
        raise NotImplementedError

    def p(self, pos):
        raise NotImplementedError

    def temp(self, pos):
        raise NotImplementedError

    def rel_humidity(self, z):
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__
