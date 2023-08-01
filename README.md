# HeavyIonDataValidation

This repository contains utility files for CMS heavy-ion-related open data.

A codebase for heavy-ion data analysis is provided in the CMS open data containers. The users of the CMS open data virtual machine need to install this codebase on top of standard CMSSW releases. Instructions are provided in [Getting started with 2013 open data](http://opendata.cern.ch/docs/cms-getting-started-2013) on the CERN open data portal.

The lists of packages to be added are in the [main branch](https://github.com/cms-opendata-validation/HeavyIonDataValidation/tree/main) of this repository:
- for CMSSW_5_3_20: [packages_HI_CMSSW_5_3_20.txt](https://github.com/cms-opendata-validation/HeavyIonDataValidation/blob/main/packages_HI_CMSSW_5_3_20.txt)
- for CMSSW_7_5_8_patch3: [packages_HI_CMSSW_7_5_8_patch3.txt](https://github.com/cms-opendata-validation/HeavyIonDataValidation/blob/main/packages_HI_CMSSW_7_5_8_patch3.txt)

This [75X](https://github.com/cms-opendata-validation/HeavyIonDataValidation/tree/75X) branch of the repository contains some example configuration files with the necessary modifications for 2015 pp HI reference open data. See the [53X](https://github.com/cms-opendata-validation/HeavyIonDataValidation/tree/53X) branch for the example files for 2013 heavy-ion-related data.

The configuration file is a direct copy of the [HeavyIonsAnalysis/JetAnalysis/test](https://github.com/CmsHI/cmssw/tree/forest_CMSSW_7_5_8_patch3/HeavyIonsAnalysis/JetAnalysis/test) area of the original codebase.
The example input file has been changed to a file in the open data area. 

Additionally, a `_cvmfs` version of the file has been created to be used in the VM (or when accessing the condition database through a mounted cvmfs area in the container). It has the following changes:
- commands to create symbolic links to the condition database files in the `/cvmfs/cms-opendata-conddb.cern.ch` area
- connection to the condition database file for respective global tags
- use of the modified `CommonFunction_OD_75X_cff.py` with the connection to the `/cvmfs/cms-opendata-conddb.cern.ch/hi_75X_add_ons` area for additional databases not in the global tag
  - the modified `CommonFunction_OD_75X_cff.py` should be placed in `HeavyIonsAnalysis/Configuration/python` of the local area.    

No validation of the resulting output has been done. These configuration files are just examples and should not be taken as official instructions.
