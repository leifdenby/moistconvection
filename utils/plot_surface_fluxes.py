import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import numpy as np
import seaborn as sns

import inspect
from datetime import timedelta as dt, datetime


from .. import cases

t0_hrs = 4.
t_start, t_end = t0_hrs, t0_hrs + 24.
t = np.linspace(t_start, t_end, 100)
# matplotlib needs datetime objects and not timedelta, so we need to have a reference time
t0 = datetime(year=1970, month=1, day=1)
t_ = np.array([t0 + dt(hours=s) for s in t])

fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8,6))

case_instances = [c() for c in cases.all]

color = iter(sns.color_palette("hls", len(case_instances)))
for case in case_instances:
    try:
        if case.FORCING_IS_TRANSIENT:
            ax1.plot(t_, case.lh_surf_flux(t=t*60*60),
                     label=str(case), color=next(color))
        else:
            ax1.axhline(case.lh_surf_flux(), label=str(case), color=next(color))
    except NotImplementedError:
        pass

ax1.set_xlabel('time')
ax1.set_ylabel('latent flux [W/m^2]')
ax1.axhline(y=0, linestyle=':', color="grey")
sns.despine()

color = iter(sns.color_palette("hls", len(case_instances)))
for case in case_instances:
    try:
        if case.FORCING_IS_TRANSIENT:
            ax2.plot(t_, case.sh_surf_flux(t=t*60*60),
                     label=str(case), color=next(color))
        else:
            ax2.axhline(case.sh_surf_flux(), label=str(case), color=next(color))
    except NotImplementedError:
        pass
ax2.set_xlabel('time')
ax2.set_ylabel('sensible flux [W/m^2]')
ax2.axhline(y=0, linestyle=':', color="grey")
sns.despine()

fig.autofmt_xdate()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

lines = ax2.get_lines()
plt.figlegend(lines, [l.get_label() for l in lines], loc='lower center')
plt.suptitle("Surface heat flux")
plt.subplots_adjust(bottom=0.3, top=0.9)

plt.show()
