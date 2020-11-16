# PyCCD - Python Continuous Change Detection

pyccd creates change segments from Landsat timeseries data

## Using PyCCD
```python
>>> import ccd
>>> results = ccd.detect(dates, blues, greens, reds, nirs, swir1s, swir2s, thermals, qas, prev_results)
>>>
>>> type(results)
<class 'dict'>
>>>
>>> results
{algorithm: 'pyccd:x.x.x',
 processing_mask: [bool, bool, ...],
 snow_prob: float,
 water_prob: float,
 cloud_prob: float,
 change_models: [
     {start_day: int,
      end_day: int,
      break_day: int,
      observation_count: int,
      change_probability: float,
      curve_qa: int,
      blue:      {magnitude: float,
                  rmse: float,
                  coefficients: (float, float, ...),
                  intercept: float},
      green:     {magnitude: float,
                  rmse: float,
                  coefficients: (float, float, ...),
                  intercept: float},
      red:       {magnitude: float,
                  rmse: float,
                  coefficients: (float, float, ...),
                  intercept: float},
      nir:       {magnitude: float,
                  rmse: float,
                  coefficients: (float, float, ...),
                  intercept: float},
      swir1:     {magnitude: float,
                  rmse: float,
                  coefficients: (float, float, ...),
                  intercept: float},
      swir2:     {magnitude: float,
                  rmse: float,
                  coefficients: (float, float, ...),
                  intercept: float},
      thermal:   {magnitude: float,
                  rmse: float,
                  coefficients: (float, float, ...),
                  intercept: float}}
                 ]
}

```

Default processing parameters can be overridden using a dictionary (see parameters.yaml for valid keys):

```python
>>> import ccd
>>> params = {'QA_BITPACKED': False,
              'QA_FILL': 255,
              'QA_CLEAR': 0,
              'QA_WATER': 1,
              'QA_SHADOW': 2,
              'QA_SNOW': 3,
              'QA_CLOUD': 4}
>>> results = ccd.detect(dates, blues, greens, reds, nirs, swir1s, swir2s, thermals, qas, params=params)
```

## Installing
System requirements (Ubuntu)
* python3-dev
* gfortran
* libopenblas-dev
* liblapack-dev
* graphviz
* python-virtualenv

System requirements (Centos)
* python3-devel
* gfortran
* blas-dev
* lapack-dev
* graphviz
* python-virtualenv

It's highly recommended to do all your development & testing in a virtual environment.
```bash
user@dev:/home/user/$ mkdir pyccd
user@dev:/home/user/$ cd pyccd
user@dev:/home/user/pyccd$ virtualenv -p python3 .venv
user@dev:/home/user/pyccd$ . .venv/bin/activate
(.venv) user@dev:/home/user/pyccd$
```

##### Install
```bash
$ pip install -e .[test,dev,docs,deploy,profile]
```

## Testing
```bash
$ pytest
$ pytest --profile
$ pytest --profile-svg

# pytest-watch
$ ptw
```

## Make targets
```bash
$ make build
$ make tests
$ make docs
$ make deploy
$ make profile
```

## Profiling
Decorate the function to be profiled with ```@profile``` and
run ```make profile```.  Remove decorations before committing code.


## Contributing

Before committing to this repository, run the following command.

```bash
git config --local commit.template .gitmessage
```

This will add the LCMAP commit template to `git commit`.

```text
jira/lcmap-xxxx: Title
Description
```

Contributions are most welcome.
1. Open an issue and discuss the change.
2. Branch from major version and name it after the issue
   * jira/lcmap-xxxx
3. Write automated tests for your changes and make sure all tests pass.
4. Update documentation in project.
5. Submit pull request to the appropriate branch (e.g. 1,x)

## Versions

PyCCD previously followed MAJOR.MINOR.PATCH.LABEL semantic versioning but has
changed to date based semantic versioning, thus: YYYY.MM.DD[.HH.MM.SS][-label].

PyCCD's version is defined by the ```ccd/version.py/__version__``` attribute.

## References
* [PyCCD Digital Object Identifier 10.5066/P90V8IIX](https://doi.org/10.5066/P90V8IIX)
* [Test Data](docs/TestData.md)
* [Landsat Band Specifications](http://landsat.usgs.gov/band_designations_landsat_satellites.php)
* [Landsat 8 Surface Reflectance Specs](http://landsat.usgs.gov/documents/provisional_lasrc_product_guide.pdf)
* [Landsat 4-7 Surface Reflectance Specs](http://landsat.usgs.gov/documents/cdr_sr_product_guide.pdf)
* [Landsat Analysis Ready Data](https://www.usgs.gov/land-resources/nli/landsat/us-landsat-analysis-ready-data)
* [LCMAP CCDC Collection 1.0 Algorithm Description Document](https://www.usgs.gov/media/files/lcmap-ccdc-add)
