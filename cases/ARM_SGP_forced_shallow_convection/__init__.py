from .. import BaseCase

import numpy as np
from scipy.interpolate import interp1d
from datetime import datetime, timedelta as dt

t0 = datetime(year=1997, month=6, day=21)

def _calc_sensible_heat_flux(t):
    """
    Calculate fluxes at time t, expected to be seconds since midnight
    """
    data = {
        dt(hours=11, minutes=30): -30.,
        dt(hours=15, minutes=30): 90.,
        dt(hours=18, minutes=0): 140.,
        dt(hours=19, minutes=0): 140.,
        dt(hours=21, minutes=30): 100.,
        dt(days=1, hours=0, minutes=0): -10.,
        dt(days=1, hours=2, minutes=0): -10.,
    }

    t_ref = np.array([t_.total_seconds() for t_ in data.keys()])
    flux_ref = np.array(list(data.values()))
    fn = interp1d(x=t_ref, y=flux_ref, bounds_error=False)

    return fn(t)

def _calc_latent_heat_flux(t):
    """
    Calculate fluxes at time t, expected to be seconds since midnight
    """
    data = {
        dt(hours=11, minutes=30): 5.,
        dt(hours=15, minutes=30): 250.,
        dt(hours=18, minutes=0): 450.,
        dt(hours=19, minutes=0): 500.,
        dt(hours=21, minutes=30): 420.,
        dt(days=1, hours=0, minutes=0): 180.,
        dt(days=1, hours=2, minutes=0): 0.,
    }

    t_ref = np.array([t_.total_seconds() for t_ in data.keys()])
    flux_ref = np.array(list(data.values()))

    print(t_ref, flux_ref)
    fn = interp1d(x=t_ref, y=flux_ref, bounds_error=False)

    return fn(t)


class ARM_SGP_ShCu(BaseCase):
    """
    This case is based on an idealization of observations made at the Southern
    Great Plains (SGP) site of the Atmospheric Radiation Measurement (ARM)
    Program on 21 June 1997. The site consists of in situ and remote-sensing
    instrumented clusters arrayed across approximately 140 000 km2 in Oklahoma
    and Kansas. On the day in question, cumulus clouds developed at the top of
    an initially clear convective boundary layer.
    """

    SCITATION_REF = "Brown et al 2002"
    FORCING_IS_TRANSIENT = True

    def lh_surf_flux(self, t):
        return _calc_latent_heat_flux(t)

    def sh_surf_flux(self, t):
        return _calc_sensible_heat_flux(t)
