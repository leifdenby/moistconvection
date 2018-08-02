import numpy as np
import matplotlib.pyplot as plot

from .. import BaseCase

API = 4.*np.arctan(1.)

def _calc_fluxes(t):
    """


    Appendix 2.  Evolution of surface heat fluxes.

    The code below (provided by Steve Lang from NASA Goddard) gives a
    simple fit to the surface latent and sensible heat fluxes for the
    February 23rd case.  Note that you can either assume some method
    to distribute this flux over the lowest few model levels, or rely on
    the subgrid-scale model to do this.

    c curve fit to observed LBA sensible and latent heat fluxes
    c      hrl is the local time in hours
    c      NOTE: simulation starts at 7:30am (t=7.50)
    c      FLXL is latent heat flux (W/m**2)
    c      FLXS is sensible heat flux (W/m**2)

           api=4.*atan(1.)
    cc time is model time in hrs (time=0 at model start)
           hrl=7.5 + time
           thea=api/2.*(12.75-hrl)/5.25
           xfact=cos(thea)
           if(xfact.le.0.) xfact=0.
           FLXL=554.*xfact**1.3
           FLXS=270.*xfact**1.5
    """
    t_hrs = t/60./60.

    thea = API/2.*(12.75-t_hrs)/5.25
    xfact = np.cos(thea)
    xfact[xfact < 0.0] = 0.
    FLXL = 554.*xfact**1.3
    FLXS = 270.*xfact**1.5

    return FLXL, FLXS

class TRMM_LBA_deep_convection_transition(BaseCase):
    FORCING_IS_TRANSIENT = True
    SCITATION_REF = "Gabrowski et al 2003"

    def lh_surf_flux(self, t):
        """
        Surface latent heat flux in [W/m^2]
        """
        latent_flx, _ = _calc_fluxes(t)
        return latent_flx

    def sh_surf_flux(self, t):
        """
        Surface latent heat flux in [W/m^2]
        """
        _, sens_flx = _calc_fluxes(t)
        return sens_flx


if __name__ == "__main__":
    t = np.linspace(7.5, 24.0, 100)*60.*60.

    plot.figure(figsize=(6,4))

    plot.plot(t, latent_flx, label="latent heat")
    plot.plot(t, sens_flx, label="sensible heat")

    plot.xlabel('time [hrs]')
    plot.ylabel('surface flux [W/m^2]')

    plot.legend()
    plot.title("Prescribed surface fluxes in TRMM-LBA\nGabrowski 2003")
    plot.tight_layout()

    plot.savefig(__file__.replace('.py', '.pdf'))
    plot.savefig(__file__.replace('.py', '.png'), dpi=300)
