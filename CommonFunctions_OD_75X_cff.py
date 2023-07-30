
import FWCore.ParameterSet.Config as cms




def overrideJEC_pp5020(process):
    process.load("CondCore.DBCommon.CondDBCommon_cfi")
    #from CondCore.DBCommon.CondDBSetup_cfi import *
    process.jec = cms.ESSource("PoolDBESSource",
                               DBParameters = cms.PSet(
                                   messageLevel = cms.untracked.int32(0)
                               ),
                               timetype = cms.string('runnumber'),
                               toGet = cms.VPSet(
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK1Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK1Calo_offline.db"),
                                            label = cms.untracked.string("AK1Calo_offline")
                                   ),
                                   
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK1PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK1PF_offline.db"),
                                            label = cms.untracked.string("AK1PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK2Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK2Calo_offline.db"),
                                            label = cms.untracked.string("AK2Calo_offline")
                                   ),
                                   
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK2PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK2PF_offline.db"),
                                            label = cms.untracked.string("AK2PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK3Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK3Calo_offline.db"),
                                            label = cms.untracked.string("AK3Calo_offline")
                                   ),
                                   
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK3PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK3PF_offline.db"),
                                            label = cms.untracked.string("AK3PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK4Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK4Calo_offline.db"),
                                            label = cms.untracked.string("AK4Calo_offline")
                                   ),
                                   
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK4PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK4PF_offline.db"),
                                            label = cms.untracked.string("AK4PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK5Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK5Calo_offline.db"),
                                            label = cms.untracked.string("AK5Calo_offline")
                                   ),
                                   
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK5PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK5PF_offline.db"),
                                            label = cms.untracked.string("AK5PF_offline")
                                   )
                                   ,
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK6Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK6Calo_offline.db"),
                                            label = cms.untracked.string("AK6Calo_offline")
                                   ),
                                   
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK6PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v12_AK6PF_offline.db"),
                                            label = cms.untracked.string("AK6PF_offline")
                                   )
                               )
    )
                               ## add an es_prefer statement to resolve a possible conflict from simultaneous connection to a global tag
    process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')
    if hasattr(process, 'HiForest'):
        process.HiForest.inputLines.extend([process.jec.toGet[6].tag.configValue()]) #pick the ak4PF one to record
    return process

def overrideJEC_PbPb5020(process):
    #process.GlobalTag.toGet.extend([
    process.load("CondCore.DBCommon.CondDBCommon_cfi")
    #from CondCore.DBCommon.CondDBSetup_cfi import *
    process.jec = cms.ESSource("PoolDBESSource",
                               DBParameters = cms.PSet(
                                   messageLevel = cms.untracked.int32(0)
                               ),
                               timetype = cms.string('runnumber'),
                               toGet = cms.VPSet(
                                   #VsPF
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK1PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK1PF_offline.db"),
                                            label = cms.untracked.string("AK1PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK1Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK1Calo_offline.db"),
                                            label = cms.untracked.string("AK1Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK2PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK2PF_offline.db"),
                                            label = cms.untracked.string("AK2PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK2Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK2Calo_offline.db"),
                                            label = cms.untracked.string("AK2Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK3Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK3Calo_offline.db"),
                                            label = cms.untracked.string("AK3Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK3PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK3PF_offline.db"),
                                            label = cms.untracked.string("AK3PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK4PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK4PF_offline.db"),
                                        label = cms.untracked.string("AK4PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK4Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK4Calo_offline.db"),
                                            label = cms.untracked.string("AK4Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK5Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK5Calo_offline.db"),
                                            label = cms.untracked.string("AK5Calo_offline")
                                   ),                                   
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK5PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK5PF_offline.db"),
                                            label = cms.untracked.string("AK5PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK6Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK6Calo_offline.db"),
                                            label = cms.untracked.string("AK6Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK6PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AK6PF_offline.db"),
                                            label = cms.untracked.string("AK6PF_offline")
                                   ),
                                   #PuPF
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu1PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu1PF_offline.db"),
                                            label = cms.untracked.string("AKPu1PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu1Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu1Calo_offline.db"),
                                            label = cms.untracked.string("AKPu1Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu2PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu2PF_offline.db"),
                                            label = cms.untracked.string("AKPu2PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu2Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu2Calo_offline.db"),
                                            label = cms.untracked.string("AKPu2Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu3Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu3Calo_offline.db"),
                                            label = cms.untracked.string("AKPu3Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu3PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu3PF_offline.db"),
                                            label = cms.untracked.string("AKPu3PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu4PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu4PF_offline.db"),
                                        label = cms.untracked.string("AKPu4PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu4Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu4Calo_offline.db"),
                                            label = cms.untracked.string("AKPu4Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu5Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu5Calo_offline.db"),
                                            label = cms.untracked.string("AKPu5Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu5PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu5PF_offline.db"),
                                            label = cms.untracked.string("AKPu5PF_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu6Calo_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu6Calo_offline.db"),
                                            label = cms.untracked.string("AKPu6Calo_offline")
                                   ),
                                   cms.PSet(record = cms.string("JetCorrectionsRecord"),
                                            tag = cms.string("JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu6PF_offline"),
                 connect = cms.string("sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/JetCorrectorParametersCollection_HI_PythiaCUETP8M1_5020GeV_753p1_v13_AKPu6PF_offline.db"),
                                            label = cms.untracked.string("AKPu6PF_offline")
                                   )
 
    )
	)
                               ## add an es_prefer statement to resolve a possible conflict from simultaneous connection to a global tag
    process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')
    if hasattr(process, 'HiForest'):
        process.HiForest.inputLines.extend([process.jec.toGet[6].tag.configValue()]) #pick the ak4PF one to record
    return process
