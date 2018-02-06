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

import numpy as np
import matplotlib.pyplot as plot

api = 4.*np.arctan(1.)

def calc_fluxes(t_hrs):
    thea = api/2.*(12.75-t_hrs)/5.25
    xfact = np.cos(thea)
    xfact[xfact < 0.0] = 0.
    FLXL = 554.*xfact**1.3
    FLXS = 270.*xfact**1.5

    return FLXL, FLXS


if __name__ == "__main__":
    t_hrs = np.linspace(7.5, 24.0, 100)

    latent_flx, sens_flx = calc_fluxes(t_hrs)

    plot.figure(figsize=(6,4))

    plot.plot(t_hrs, latent_flx, label="latent heat")
    plot.plot(t_hrs, sens_flx, label="sensible heat")

    plot.xlabel('time [hrs]')
    plot.ylabel('surface flux [W/m^2]')

    plot.legend()
    plot.title("Prescribed surface fluxes in TRMM-LBA\nGabrowski 2003")
    plot.tight_layout()

    plot.savefig(__file__.replace('.py', '.pdf'))
    plot.savefig(__file__.replace('.py', '.png'), dpi=300)
