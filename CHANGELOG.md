# pyccd change log
All notable changes to this project will be documented in this file. Changes before 1.0.0.b1 are not tracked.
## 2021.07.19
### Bug Fixes
 - Fix a return statement inside of the standard procedure that was missing the processing mask

## 2021.07.14
### Bug Fixes  
 - Edge case exceptions related to exceptionally low observation counts that are also temporally disparate

## 2020.10.10
### Added
 - Parameter STAT_ORD to constrain calculations that normally look at the entire time series
 - Support for building off a previous set of PYCCD results

## 2018.10.17
### Added
 - Additional testing for main detect() method to ensure all the code is flexed to some degree
 - link to Algorithm Description Document (ADD)
 - link to Analysis Ready Data (ARD) information

### Changed
 - The number of observations used to detect change is now variable, and dependant on input characteristics
 - Permanent snow and insufficient clear procedures now return the last day in the series as the break day instead of 0
 - Replaced the parameters.yaml with a .py

### Removed
 - pyyaml dependency
 - parameters.yaml file dependency
 - docs directory (superseded by ADD)
  
## 2018.03.12
### Added
 - Number of parameters option for RMSE, for influencing the calculation based on model complexity versus your sample size.

### Changed
 - Variable name change on the main ccd.detect function signature slightly. quality -> qas. This was requested to better support downstream processing.
 - Average number of days per year from 365.25 -> 365.2425 . While seemingly insignificant, this can add up depending on where your ordinal 0 starting point is at.
 
### Removed
 - The click and cachetools dependencies as they were unused.
 - procedure from the ccd.detect dictionary return. This is redundant with the curve fit information returned with each segment.

## 2017.10.27
### Added
 - Probability that any given observation will be cloud, snow, or water, based on the QA information passed in
 - Efficiencies to filling out the lasso coefficient matrix
 - Release checklist

### Changed
 - Removed unused py files that may have been causing confusion
 - Results should use standard Python types, this helps with any downstream applications

## 2017.08.18
### Added
 - Conditional treatment of cirrus confidence and terrain occlusion bits from Landsat 8 pixelQA

## 2017.06.20
### Bug Fixes
 - The lasso coefficient matrix was not being populated correctly when the number of requested coefficients was 8.

## 2017.06.08
### Added
 - Check the inputs to make sure that they are appropriately sized relative to each-other

### Changed
 - Moved to a date orientated versioning scheme (YYYY.MM.DD). This brings the project more inline with other LCMAP efforts.

### Bug Fixes
 - fixed Tmask regression to include a column of ones

## 1.4.0 - 2017-04-26
### Added
 - this file
 - can now pass a processing parameter dictionary to ccd.detect, key/values will override parameters.yaml
 - support for ARD bit-packed QA values
 
### Changed
 - overhauled code base to have some separation of paradigms, procedures.py relates to the more procedural code while changes.py should be more functional in nature
 - tried to remove all default argument values for all methods
 - adjusted many internal method signatures
 - removed ensure_ndarray_input decorator
 - logging is less global and listens to what imports ccd
 
### Bug Fixes
 - reference period array rather than original dates array for the model window in the initialize method
 - simplified logic and removed find_time_index method
 - changed adjusted variogram logic to match the Matlab approach 1:1

## 1.3.1 - 2017-04-10
### Changed
 - move duplicate date trimming to occur after other masking is done
 - ensure_ndarray_input to use keyword args better [broken]
 
### Bug Fixes
 - removed errant print statement
 - fixed the adjusted variogram calculation introduced last version

## 1.3.0 - 2017-03-30
### Changed
 - robust iterative reweighted least squares for the regression used by the partial Tmask, alignment with original Matlab CCDC v12.30
 - updated variogram calculation to try and only use observations > 30 days a part
 - TestData.md now copy/pastable

## 1.1.0 - 2017-03-02
### Added
 - auto-deploy to pypi from master
 
### Bug Fixes
 - per band change magnitudes based on the final peek window of a time segment

## 1.0.4.b1 - 2017-02-24
### Added
 - travis-ci automated testing and deployment setup
 - better pypi interactions
 
### Changed
 - time segment QA values aligned with original Matlab CCDC v12.30
 - general fits removed between stable segments
 
### Bug Fixes
 - updated setup.py for numpy >= 1.10

## 1.0.0.b1 - 2017-01-31
 - Initial beta release for evaluation efforts
 - Change tracking start

## 1.0.0.a1 - 2016-10-13
 - Proof of concept for moving the CCDC code base to python
