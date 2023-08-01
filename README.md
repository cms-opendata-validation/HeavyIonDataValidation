# HeavyIonDataValidation

This repository contains utility files for CMS heavy-ion-related open data.

A codebase for heavy-ion data analysis is provided in the CMS open data containers. The users of the CMS open data virtual machine need to install this codebase on top of standard CMSSW releases. Instructions are provided in [Getting started with 2013 open data](http://opendata.cern.ch/docs/cms-getting-started-2013) on the CERN open data portal.

The lists of packages to be added are in the [main branch](https://github.com/cms-opendata-validation/HeavyIonDataValidation/tree/main) of this repository:
- for CMSSW_5_3_20: packages_HI_CMSSW_5_3_20.txt
- for CMSSW_7_5_8_patch3: packages_HI_CMSSW_7_5_8_patch3.txt

This [53X](https://github.com/cms-opendata-validation/HeavyIonDataValidation/tree/53X) branch of the repository contains some example configuration files with the necessary modifications for 2013 heavy-ion-related open data. See the [75X](https://github.com/cms-opendata-validation/HeavyIonDataValidation/tree/75X) branch for the example files for 2015 pp reference data.

The files are direct copies of the [HeavyIonsAnalysis/JetAnalysis/test](https://github.com/CmsHI/cmssw/tree/forest_CMSSW_5_3_20/HeavyIonsAnalysis/JetAnalysis/test) area of the original codebase.
For all files, the example input file has been changed to a file in the open data area. 

Additionally, `_cvmfs` versions of the files have been created to be used in the VM (or when accessing the condition database through a mounted cvmfs area in the container). They have the following changes:
- commands to create symbolic links to the condition database files in the `/cvmfs/cms-opendata-conddb.cern.ch` area
- connection to the condition database file for respective global tags
- use of the modified `CommonFunction_OD_53X_cff.py` with the connection to the `/cvmfs/cms-opendata-conddb.cern.ch/hi_53X_add_ons` area for additional databases not in the global tag.
The modified `CommonFunction_OD_53X_cff.py` should be placed in `HeavyIonsAnalysis/Configuration/python` of the local area.

The open data input files are in the `RECO` format, but some of the original test files may have had some additional content that is not included in the `RECO` files. Therefore the following modifications have been done 
- runForest_pPb_MC_53X:
  - `process.ppTrack.doSimTrack = cms.untracked.bool(False)`
  - comment out `cutsTPForFak` and `cutsTPForEff` from the path
- runForest_PbPb_MC_53X:
  - comment out `process.photonStep_withReco` from the path.
These modifications have not been verified by experts.    

No validation of the resulting output has been done. These configuration files are just examples and should not be taken as official instructions.
