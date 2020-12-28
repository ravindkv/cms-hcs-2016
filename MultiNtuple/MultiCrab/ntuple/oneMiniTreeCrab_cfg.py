
#/////////////////////////////////////////////
#                                            #
# CRAB configuration to run over ONE sample  #
#                                            #
#/////////////////////////////////////////////

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#Do read the below link, for CRAB parameters:
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
#config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'
#config.JobType.inputFiles = ["../../MiniTree/Selection/test/Spring16_25nsV10_MC_PtResolution_AK4PF.txt"]

config.JobType.maxMemoryMB = 4000
config.General.requestName = 'HplusM100_20170425'
config.General.workArea = 'HplusM120_20170425'
config.JobType.psetName = '../../MiniTree/Selection/test/muonMiniTreeMaker_cfg.py'
config.Data.inputDataset = '/ChargedHiggsToCS_M120_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
#config.Data.inputDataset = '/HplusM100ToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
config.Data.outLFNDirBase = '/store/user/%s/HplusM100_test' % (getUsernameFromSiteDB())
