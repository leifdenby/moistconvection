# Test cases modelling moist convection

This repository represents an *unofficial* record of test cases defined as part
of the GCSS (GEWEX Cloud System Study) BLCWG (Boundary Layer Cloud Working
Group) and others before these disappear off the internet.

The sites which were mirrored (both directly and from the Wayback Machine) are
stored in [mirrors/](mirrors/) and detailed information for each case is
available in [cases/](cases/).

The whole repository is a python module with the intention that each defined
case can be imported as a python module and routines therein defined used to
set up simulations.

*NB*: Large files (images, PDFs, powerpoint etc) are stored in
[git-lfs](https://git-lfs.github.com/) so you'll need to install that before
being able to access these files.

If you find any errors or data-files which should be added please make a pull
request! Thank you :)

## List of test-cases

- [RICO](cases/RICO/) freely convecting shallow convection over maritime
tropics

- [BOMEX](cases/BOMEX/) non-precipitating shallow cumulus

- [TRMM_LBA_deep_convection_transition](cases/TRMM_LBA_deep_convection_transition/)
development of daytime convective boundary layer and the transition from
shallow to deep convection (*GCSS Working Group 4, Case 4*)

- [TOGA_COARE_deep_convection_transition](cases/TOGA_COARE_deep_convection_transition/)
transition from suppressed to deep convection over land (*GCSS Working Group 4,
Case 5*)
