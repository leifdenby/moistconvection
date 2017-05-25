*content below was converted from html of [website](website/) using pandoc*

Introduction
============

The Grey Zone Project aims to systematically explore convective
transport and cloud processes in weather and climate models at various
resolutions, ranging from high resolution turbulent resolving scales all
the way to coarse resolutions that require full parameterized
descriptions of these processes. By exploring the behaviour of these
models with and without convective parameterizations through the
so-called grey zone the project aims to answer

-   Which are the relative contributions of the parameterized versus the
    resolved contributions to the convective transport?
-   How well do models operate in the grey zone without an explicit
    convection parameterization?
-   How well do models operate in the grey zone with a convection
    parameterization?
-   How should scale-aware convection parameterizations behave in the
    grey zone?

The Grey Zone project aims to apply this methodology on a number of
different types of moist convective systems. The type of moist
convection considered here is a cold air outbreak.

Cold air outbreak case - CONSTRAIN
==================================

Cold air outbreaks are a common feature in the winter time to the north
of the British where cold air from the polar cap sweeps off the ice edge
over open water. The convection begins as organised rolls near to the
ice edge but eventually changes into open cellular convection as the
boundary layer evolves (see Brummer and Pohlmann (2000) and references
therein). These cloud morphological changes can have important impacts
on the transport of heat and moisture as well as radiative effects such
as high latitude Short Wave errors that are one of the largest biases in
climate models (Karlsson and Svensson, 2010, Trenberth and Fasullo,
2010, Bodas-Salcedo et al. 2012). Accurate forecasts of such events are
also important for civil aviation safety (e.g. Wilkinson et al. 2012).

The proposed intercomparison case is based on observations taken during
the Met Office CONSTRAIN campaign and associated NWP simulations.
Constrain took place over the North Atlantic, with flights carried out
from Prestwick airport from January 12 to 31 2010. The aim of CONSTRAIN
was to better determine the various ice and mixed-phase cloud
microphysical parameters used in the Met Office Unified Model (UM) and
cloud resolving models.

The proposed case is based in observations and NWP data from January
31st 2010 (see synoptic chart below). Observations show that this day
was characterised by northerly flow and stratocumulus clouds at 66N
-11W. As air advects over warmer seas the Sc transitions to mixed-phase
cumulus clouds at around 60N, prior to reaching land.

The domain of interest is of the order of 1500 km by 750 km which will be
The domain of interest is of the order of 1500 km by 750 km which will
be explored with various resolutions by both global Numerical Weather
Prediction (NWP) models and Limited Area Models (LAMs). Since it will be
unfeasible to fully resolve the relevant moist convective processes for
these two model types, we also have set up the case for idealised LAM
and Large Eddy Simulation (LES) models that can run in a Langrangian
setting on a smaller domain of around 100 km. For this set up it will be
feasible for a number of models to run at a turbulent resolved (\~100m)
resolution.

![](../../mirrors/appconv.metoffice.com/cold_air_outbreak/constrain_case/images/asxx_20100131_1200UTC.png)

-   **Global Case** - Global Models will run this case at their highest
    spatial resolution (3\~10km). The main research questions here
    are i) how well is the parameterized convection capable of
    representing realistically the transport of heat, moisture and
    momentum, thereby obtaining the correct vertical thermodynamical
    structure and cloud properties and ii) are global models already
    entering the grey zone at their highest spatial resolution and how
    does this affect their behaviour
-   **LAM case** - LAMs will be executed at various resolutions in the
    range of 1 to 10 km. Here the main research questions are how
    convective transport and cloud processes are changing at these
    various resolutions with and without convection parameterizations
-   **LES case** - LES codes and LAM’s will be run in a more idealized
    Lagrangian setting at a smaller domain of 100 km at turbulent
    resolving scales of 200 m ( and coarser) that will be advected with
    the mean flow. These runs will serve as a reference and the realism
    of the interaction between the parameterised cloud microphysics and
    the resolved turbulence will be explored: to what extent are the
    observed mesoscale structures (cloud streets and closed cells)
    realistically reproduced and how do these structures degrade with
    decreasing resolutions in the range of 100 m to a few kilometres.

References
----------

Bodas-Salcedo A. , K. D. Williams, P. R. Field, and A. P. Lock,
2012:Contribution of midlatitude cyclone clouds to the short-wave
deficit in the Southern Ocean . Submitted J. Clim.

Brummer, B and Pohlmann, S, 2000: Wintertime roll and cell convection
over Greenland and Barents Sea regions: A climatology. Journal of
Geophysical Research-Atmospheres. 105, D12, 15559-15566,
10.1029/1999JD900841

Karlsson, J., and G. Svensson, 2010: The simulation of Arctic clouds and
their influence on the winter surface temperature in present-day climate
in the CMIP3 multi-model dataset. Clim. Dyn., DOI
10.1007/s00382-00010-00758-00386.

Trenberth, K. E., and J. T. Fasullo, 2010: Simulation of Present-Day and
Twenty-First-Century Energy Budgets of the Southern Oceans. Journal of
Climate, 23, 44 0-454.

Wilkinson, J.M, Helen Wells, Paul R. Field and Paul Agnew, 2012:
Investigation and Prediction of Helicopter Triggered Lightning over the
North Sea. Submitted t o Met. Apps.

