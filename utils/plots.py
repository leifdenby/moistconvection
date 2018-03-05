import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plot
import numpy as np
import os
from tephigram_python import Tephigram

import moistconvection.cases.BOMEX.setup_3d_LES
import moistconvection.cases.RICO.setup_3d_LES

def plot_initial_condition(profile, output_dir):
    fig = plot.figure(figsize=(8,6))

    z = np.linspace(0., profile.z_max, 100)
    p = profile.p(z)
    T = profile.temp(z)
    rel_humid = profile.rel_humidity(z)

    assert not np.any(rel_humid > 1.0)

    tephigram = Tephigram(fig=fig, p00=profile.p0)
    tephigram.plot_temp(p=p, T=T, marker='')
    tephigram.plot_RH(p=p, T=T, RH=rel_humid, marker='')
    tephigram.set_plim(400e2, 1200e2)
    tephigram.plot_legend()
    plot.title(str(profile))

    plot.savefig(os.path.join(output_dir, "initial_condition.png"))

    pass


if __name__ == "__main__":
    profile_module = moistconvection.cases.BOMEX.setup_3d_LES
    profile = profile_module.BOMEX()

    # profile_module = moistconvection.cases.RICO.setup_3d_LES
    # profile = profile_module.RICO()

    output_dir = os.path.dirname(os.path.abspath(profile_module.__file__))
    plot_initial_condition(profile, output_dir)
