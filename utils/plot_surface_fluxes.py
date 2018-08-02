import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import inspect

from .. import cases

t_start, t_end = 0., 24
t = np.linspace(t_start, t_end, 100)

fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, sharey=True)

case_instances = [c() for c in cases.all]

color = iter(sns.color_palette("hls", len(case_instances)))
for case in case_instances:
    if case.FORCING_IS_TRANSIENT:
        ax1.plot(t, case.lh_surf_flux(t=t*60*60),
                 label=str(case), color=next(color))
    else:
        ax1.axhline(case.lh_surf_flux(), label=str(case), color=next(color))
ax1.set_xlabel('time [hours]')
ax1.set_ylabel('latent flux [W/m^2]')
sns.despine()

color = iter(sns.color_palette("hls", len(case_instances)))
for case in case_instances:
    if case.FORCING_IS_TRANSIENT:
        ax2.plot(t, case.sh_surf_flux(t=t*60*60),
                 label=str(case), color=next(color))
    else:
        ax2.axhline(case.sh_surf_flux(), label=str(case), color=next(color))
ax2.set_xlabel('time [hours]')
ax2.set_ylabel('sensible flux [W/m^2]')
sns.despine()

lines = ax2.get_lines()
plt.figlegend(lines, [l.get_label() for l in lines], loc='lower center')
plt.suptitle("Surface heat flux")
plt.subplots_adjust(bottom=0.25, top=0.9)

plt.show()
