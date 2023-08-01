# HeavyIonDataValidation

This repository contains utility files for CMS heavy-ion-related open data.

A codebase for heavy-ion data analysis is provided in the CMS open data containers. The users of the CMS open data virtual machine need to install this codebase on top of standard CMSSW releases. Instructions are provided in [Getting started with 2013 open data](http://opendata.cern.ch/docs/cms-getting-started-2013) on the CERN open data portal.

The lists of packages to be added are in this repository:
- for CMSSW_5_3_20: packages_HI_CMSSW_5_3_20.txt
- for CMSSW_7_5_8_patch3: packages_HI_CMSSW_7_5_8_patch3.txt

The [53X](https://github.com/cms-opendata-validation/HeavyIonDataValidation/tree/53X) and [75X](https://github.com/cms-opendata-validation/HeavyIonDataValidation/tree/75X) branches of the repository contain some example configuration files with the necessary modifications to use them with open data. The updates are only at the level of input files and access to the condition database. Some modules have been commented out, see details in the respective branches. No validation of the resulting output has been done. These configuration files are just examples and should not be taken as official instructions.

