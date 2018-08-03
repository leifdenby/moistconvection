# Load all modules in folder: https://stackoverflow.com/a/1057534

from os.path import dirname, basename, isfile
import glob
import importlib
import inspect
import sys

class BaseCase:
    """
    Base case class. __doc__ here shold contain description of case
    """
    SCITATION_REF = "someAuthor et al 1970"
    FORCING_IS_TRANSIENT = True


    # forcings

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

    def ddt_theta_l__ls(self, t, z):
        """
        Large Scale Horizontal Liq. Water Pot. Temperature Advection combined
        with Radiative Cooling [K/s]
        """
        raise NotImplementedError

    def ddt_qv_ls(self, t, z):
        """
        Large Scale Horizontal Moisture Advection [(kg/kg)/s]
        """
        raise NotImplementedError

    def w_subsidence(self, t, z):
        """
        Large Scale Subsidence w [m/s] Apply the subsidence on the prognostic
        fields of q_t, theta_l.
        """
        raise NotImplementedError


    # initial conditions

    def q_t(self, z):
        """ Total water specific concentration [kg/kg]"""
        raise NotImplementedError

    def theta_l(self, z):
        """ Liquid water potential temperature [K]"""
        raise NotImplementedError

    def tke(self, z):
        """Initial subgrid profile of subgrid TKE"""
        raise NotImplementedError

    def rho(self, z):
        raise NotImplementedError

    def p(self, z):
        raise NotImplementedError

    def temp(self, z):
        raise NotImplementedError

    def rel_humidity(self, z):
        raise NotImplementedError

    def __str__(self):
        return "{} ({})".format(
            self.__class__.__name__.replace('_', ' '),
            self.SCITATION_REF
        )


modules = glob.glob(dirname(__file__)+"/*/*.py")

__all__ = [
    basename(dirname(f)) for f in modules
    if isfile(f) and f.endswith('__init__.py')
]

for m in __all__:
    importlib.import_module('.{}'.format(m), __name__)

_loaded_modules = inspect.getmembers(sys.modules[__name__], inspect.ismodule)


# make list which contains all defined classes for easy access

def _filter(c):
    return inspect.isclass(c) and issubclass(c, BaseCase) and not c == BaseCase

all = []
for name, loaded_module in _loaded_modules:
    for clsname, cls in inspect.getmembers(loaded_module, _filter):
        all.append(cls)
