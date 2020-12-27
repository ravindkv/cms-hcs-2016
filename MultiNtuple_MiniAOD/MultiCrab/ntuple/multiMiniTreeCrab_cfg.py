
#///////////////////////////////////////////////////
#                                                  #
# CRAB configuration to run over Multiple samples  #
#                                                  #
#///////////////////////////////////////////////////


#------------------ Setup CRAB -------------------------------#
#getEventsFromDAS("source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh")
#getEventsFromDAS("cmsenv")
#getEventsFromDAS("voms-proxy-init --voms cms")
#-------------------------------------------------------------#

import os
import sys
import datetime
import FWCore.ParameterSet.Config as cms

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("ntuple","module"))
from dataMiniAOD import muDataSampDict as muData
from dataMiniAOD import eleDataSampDict as eleData
from mcMiniAOD import mcMuSampDict as mcMu
from mcMiniAOD import mcEleSampDict as mcEle
from sampleKeyVal import *
from multiCrab import *

def getSummaryFromDAS(dataset_name):
    das_command = "dasgoclient --limit=1 --query=\"summary dataset=%s\"" %dataset_name
    print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  das_command
    das_summary = os.popen(das_command).read()
    return das_summary

#------------------------------------------
#Check availability of samples on DAS
#------------------------------------------
#toPrint("Total MC samples",len(mc))
for n in range(len(mcMu)):
    dataset_key = getMCKey(mcMu, n)
    dataset_name = getMCVal(mcMu, n)
    #dataset_summary = getSummaryFromDAS(dataset_name)
    #print '{:<30}  {:<30}'.format(dataset_key, dataset_summary)

#toPrint("Total single muon DATA samples",len(muData))
for n in range(len(muData)):
    dataset_key = getMCKey(muData, n)
    dataset_name = getMCVal(muData, n)
    #dataset_summary = getSummaryFromDAS(dataset_name)
    #print '{:<30}  {:<30}'.format(dataset_key, dataset_summary)

#toPrint("Total single electron DATA samples",len(eleData))
for n in range(len(eleData)):
    dataset_key = getMCKey(eleData, n)
    dataset_name = getMCVal(eleData, n)
    #dataset_summary = getSummaryFromDAS(dataset_name)
    #print '{:<30}  {:<30}'.format(dataset_key, dataset_summary)
#------------------------------------------
#USER INPUTS
#------------------------------------------
#muon channel
isMu = False
isMuMC = False
isMuData = False
range_muMC = len(mcMu)
range_muData = len(muData)

#electron channel
isEle = True
isEleMC = True
isEleData = False
range_EleMC = len(mcEle)
range_EleData = len(eleData)

#------------------------------------------
#CRAB PARAMETERS
#------------------------------------------
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#default CRAB parameters
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
#config.JobType.disableAutomaticOutputCollection = True
config.Data.inputDBS = 'global'
config.JobType.maxMemoryMB = 4000
#config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'

date = str(datetime.date.today()).replace("-","")
all_T2Paths = open("ntupleT2Paths_"+ date +".txt", 'w')

#------------------------------------------
#MUON CHANNEL
#------------------------------------------
muMC_T2Paths = ["MUON MC:"]
muData_T2Paths = ["MUON DATA:"]
muMC_dirT2 =   "NTuple_HIG-18-021_"+date+"_MuMC"
muData_dirT2 = "NTuple_HIG-18-021_"+date+"_MuData"
if isMu:
    if isMuMC:
        #toPrint("MUONS, MC ","")
        for m in range(range_muMC):
            mu_MC = "MuMC_"+ date
            config.Data.splitting = 'FileBased'
            if("ST" in getMCKey(mcMu, m)):
                config.Data.unitsPerJob = 3
            elif("TTJetsM" in getMCKey(mcMu, m)):
                config.Data.unitsPerJob = 2
            elif("TTJetsP" in getMCKey(mcMu, m)):
                config.Data.unitsPerJob = 3
            elif("Hplus" in getMCKey(mcMu, m)):
                config.Data.unitsPerJob = 3
            else:
                config.Data.unitsPerJob = 8
            createMuMCpsetFile(mu_MC, "../../MiniTree/Selection/test/muonMiniTreeMaker_cfg.py", mcMu, m)
            config.General.requestName = getMCKey(mcMu, m) +"_"+mu_MC
            config.General.workArea = 'Crab' +mu_MC
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.inputDataset = getMCVal(mcMu, m)
            config.Data.outLFNDirBase = getLFNDirBaseMC(mu_MC, mcMu, m, muMC_dirT2)
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muMC_T2Paths.append(getNtupleT2Paths(mu_MC, mcMu, m, muMC_dirT2))

    if isMuData:
        #toPrint("MUONS, DATA ","")
        for d in range(range_muData):
            mu_Data = "MuData_"+ date
            config.Data.unitsPerJob = 300
            config.Data.splitting = 'LumiBased'
            config.Data.allowNonValidInputDataset = True
            createMuDatapsetFile(mu_Data, "../../MiniTree/Selection/test/muonMiniTreeMaker_cfg.py", muData, d)
            config.General.requestName = getDataKey(muData, d) +"_"+mu_Data
            config.General.workArea = 'Crab'+mu_Data
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.lumiMask = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
            config.Data.inputDataset = getDataVal(muData, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(mu_Data, muData, d, muData_dirT2)
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muData_T2Paths.append(getNtupleT2Paths(mu_Data, muData, d, muData_dirT2))

all_T2Paths.write(str(muMC_T2Paths)+",\n\n")
all_T2Paths.write(str(muData_T2Paths)+",\n\n")

#------------------------------------------
#ELECTRON CHANNEL
#------------------------------------------
electrons_MC_t2_paths = ["ELECTRON MC:"]
electrons_Data_t2_paths = ["ELECTRON DATA:"]
eleMC_dirT2 =   "NTuple_HIG-18-021_"+date+"_EleMC"
eleData_dirT2 = "NTuple_HIG-18-021_"+date+"_EleData"
if isEle:
    if isEleMC:
        #toPrint("ELECTRONS, MC ","")
        for m in range(range_EleMC):
            ele_MC = "EleMC_"+ date
            config.Data.splitting = 'FileBased'
            if("ST" in getMCKey(mcEle, m)):
                config.Data.unitsPerJob = 3
            elif("TTJetsM" in getMCKey(mcEle, m)):
                config.Data.unitsPerJob = 2
            elif("TTJetsP" in getMCKey(mcEle, m)):
                config.Data.unitsPerJob = 3
            elif("Hplus" in getMCKey(mcEle, m)):
                config.Data.unitsPerJob = 3
            else:
                config.Data.unitsPerJob = 8
            createEleMCpsetFile(ele_MC, "../../MiniTree/Selection/test/eleMiniTreeMaker_cfg.py", mcEle, m)
            config.General.requestName = getMCKey(mcEle, m) +"_"+ele_MC
            config.General.workArea = 'Crab' +ele_MC
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.inputDataset = getMCVal(mcEle, m)
            config.Data.outLFNDirBase= getLFNDirBaseMC(ele_MC, mcEle, m, eleMC_dirT2)
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            electrons_MC_t2_paths.append(getNtupleT2Paths(ele_MC, mcEle, m, eleMC_dirT2))

    if isEleData:
        #toPrint("ELECTRONS, DATA ","")
        for d in range(range_EleData):
            ele_Data = "EleData_"+ date
            config.Data.unitsPerJob = 300
            config.Data.splitting = 'LumiBased'
            config.Data.allowNonValidInputDataset = True
            createEleDatapsetFile(ele_Data, "../../MiniTree/Selection/test/eleMiniTreeMaker_cfg.py", eleData, d)
            config.General.requestName = getDataKey(eleData, d) + "_"+ele_Data
            config.General.workArea = 'Crab' +ele_Data
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.lumiMask = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
            config.Data.inputDataset = getDataVal(eleData, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(ele_Data, eleData, d, eleData_dirT2)
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            electrons_Data_t2_paths.append(getNtupleT2Paths(ele_Data, eleData, d, eleData_dirT2))

#ALL T2 PATHS
all_T2Paths.write(str(electrons_MC_t2_paths)+",\n\n")
all_T2Paths.write(str(electrons_Data_t2_paths))
