# read-netcdf
This is a parser for netcdf-files storing climate data for Europe and Germany. It currently supports reading files from 5 datasets (4 are actually netCDF):

  * Regional Climate Projections from **CORDEX** climate models regarding the variable 'tas' (average daily temperature) for Europe
  * a **Heatwaves** and Cold Spells dataset for Europe (climate projections)
  * a **Temperature Statistics** dataset for Europe (climate projections)
  * **HOSTRADA**, historical data (until present, still updated) for Germany
  * TRY for Germany with a present and future representative year

The scripts named `read_...` reads from netCDF or other data files, which you have to download from climate data stores. See the section on [prerequisites](#Prerequisites) below for datasets from Copernicus Climate Data Store. NOTE, that they write to outfiles and usually append to them! This is useful for collecting data from monthly datafiles into one outfile containing the data for a whole year.

Scripts names `plot_...` work with data which have to be prepared beforehand by running the respective `read...`-script. NOTE, that plots are evenly spaced on the x-axis rather than reading the x-values.

Some scripts have further instructions as a header comment within the script.

The script 'read_heatwaves_or_temperature_stats.py' works with netCDF files from 2 datasets, see header comment in 
script. This README is written for the script 'read_cordex_tas.py'.

## For whom?
If you are starting to work with .nc-files this is a good starting point for you. 
If you just want a small piece of code to read from .nc-files, you will find it here, too.

### Am I Working with the Right Data?
Climate Projection Data is a large field. If you are an end user, like me, you might want to keep searching for already processed datasets. Someone has already done the analysis you need. For example: From climate projection data one can analyse heat days and heat waves, because they contain a maximum daily temperature. Someone has already done this analysis, there is a heatwave dataset. See for example [this gist](https://gist.github.com/mueller-fr/44da1d02aecae0fc79159a503b5efa20).

The "Deutscher Wetterdienst" has some good [advice about using climate projection data](https://www.dwd.de/DE/klimaumwelt/klimaforschung/klimaprojektionen/fuer_deutschland/fuer_dtld_nutzungshinweis_node.html;jsessionid=D1A87E60A29B9CBDEB44F0D498D0A079.live31084) on their page (in german). The first 3 points are:
1. Look for the information that suits your tasks and needs
2. Don't use only ONE dataset
3. Climate Projection computations are not forecasts
4. ...

## How to Run the Script
### Prerequisites:
* you need an .nc-file, from the CORDEX. You can download one at Copernicus' Climate Data Store
   * create a free account. Logged in, make selections in the form below (link)
     * monthly data is recommended for testing, since it is smaller than daily data
     * choose variable "2m air temperature" (called 'tas' in the dataset to download)
   * Submit the form, download the file and unzip it
   * https://cds.climate.copernicus.eu/cdsapp#!/dataset/projections-cordex-domains-single-levels?tab=form
* `pip install -r requirements.txt`
 * change this script, lines to change are marked with "<---"
 * change filename to your downloaded .nc-file
   * change the path or place it in the same location as this script
   * change the location to the one you are interested in (lat, lon coordinates)

### Usage:
*	`python read_cordex_tas.py` 

## What's up with that File 'variables_values_info.md'?
It contains some information about the structure of the data in the .nc file.
You can reproduce the outputs (or get different ones) with the steps below, alternatively check out 
'explore_netCDF_dataset.py'.

Since CORDEX-data have a standardized structure, you might get the same responses from your .nc-file.

It depends on the query.

### Take a look into the Datastructure via the Python-shell
1. Pip install netCDF as mentioned in the script.

2. Start the python interpreter from your terminal
```sh
python
```

3. Import netCDF4 and your file. Replace 'path_to_file_and_name.nc' with your filename and location
```python
>>> import netCDF4
>>> dataset = netCDF4.Dataset('path_to_file_and_name.nc')
```

4. Then, try the commands from 'variables_values.md'
```python
>>> dataset.dimensions.keys()
>>> dataset.variables.keys()
>>> dataset.variables['tas'] # if 'tas' was part of the variables.keys() above
```

## Contributing
We appreciate your contributions! In fact, we decided to open-source this simple script mainly to connect with others working on similar topics. Leave us a note in Discussions!

### How to Contribute to the Code
Just open a PR or an Issue.
Make sure to give some context, WHY this change is useful and HOW your need for the change came to be.
Thank you!!
