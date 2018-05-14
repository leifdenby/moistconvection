import itertools
import os
import inspect

import numpy as np
import matplotlib.pyplot as plot
from matplotlib.gridspec import GridSpec
import seaborn as sns


sns.set_style("ticks")

def plot_LS_forcing(profile):
    s_day = 60*60*24
    qv_day = s_day*1.0e3
    plot_vars = [
        dict(name="u_wind", label="u-wind", units="m/s", xaxis='wind'),
        dict(name="v_wind", label="v-wind", units="m/s", xaxis='wind'),
        dict(name="w_subsidence", xaxis=r"$w_{sub}$", units="m/s",
             label='subsidence velocity'),
        dict(name="ddt_qv_ls", xaxis=r"$\left.\frac{dq_v}{dt}\right|_{LS}$",
             units="g/kg/day", scaling=qv_day,
             label='advection'),
        dict(name="ddt_theta_l__ls",
             xaxis=r"$\left.\frac{d\theta_l}{dt}\right|_{LS}$",
             units="K/day", scaling=s_day,
             label='advection & radiation',
             ),
    ]
    grids = iter(GridSpec(1, len(plot_vars)-1))

    z_max = getattr(profile, 'z_max', 4.0e3)
    z = np.linspace(1, z_max, 100)

    plot.figure(figsize=(8, 3.5))

    palette = itertools.cycle(sns.color_palette())

    lines = []

    color__w_sub = None

    for n, v in enumerate(plot_vars):
        d = getattr(profile, v['name'])(z)
        s = v.get('scaling', 1.0)

        if v['name'] != "v_wind":
            ax = plot.subplot(grids.next())

        color = palette.next()

        lines += plot.plot(d*s, z, color=color, label=v.get('label', None))
        plot.xlabel('{} [{}]'.format(v['xaxis'], v['units']))

        if v['name'] == "ddt_theta_l__ls":
            if color__w_sub is None:
                color__w_sub = palette.next()

            ddz__theta_l = np.gradient(profile.theta_l(z))/np.gradient(z)
            ddt__theta_l = -ddz__theta_l * profile.w_subsidence(z)

            # plot.plot(ddt__theta_l*s, z)
            color = palette.next()
            plot.plot((d + ddt__theta_l)*s, z, linestyle='--',
                      color=color__w_sub,
                      label='total (incl. subsidence from initial profile)')

        if v['name'] == "ddt_qv_ls":
            if color__w_sub is None:
                color__w_sub = palette.next()

            ddz__qt = np.gradient(profile.q_t(z))/np.gradient(z)
            ddt__qt = -ddz__qt * profile.w_subsidence(z)

            # plot.plot(ddt__qt*s, z)
            color = palette.next()
            lines += plot.plot(
                (d + ddt__qt)*s, z, linestyle='--',
                color=color__w_sub,
                label='total (incl. subsidence from initial profile)'
            )

        plot.axvline(0, linestyle=':', color='grey')

        plot.ylim(0, z_max)

        if n < 2:
            plot.ylabel('height [m]')
        else:
            ax.set_yticklabels([])

    plot.tight_layout()
    plot.figlegend(lines, [l.get_label() for l in lines],
                   loc='lower center', ncol=3)
    plot.subplots_adjust(bottom=0.35)

    sns.despine()

    plot.draw()


if __name__ == "__main__":

    from cases.BOMEX.setup_3d_LES import BOMEX
    from cases.RICO.setup_3d_LES import RICO

    test_cases = [
        BOMEX(),
        RICO(),
    ]

    for case in test_cases:
        case_name = case.__class__.__name__
        case_directory = os.path.dirname(inspect.getfile(case.__class__))
        out_filename = os.path.join(case_directory,
                                    "{}_LS_forcing.png".format(case_name))

        print "{} -> {}".format(case, out_filename)

        plot_LS_forcing(case)
        plot.suptitle("Large-scale forcing for {} test-case\n{}"
                      "".format(case_name, case.SCITATION_REF))
        plot.subplots_adjust(top=0.85)
        plot.savefig(out_filename, dpi=300)
