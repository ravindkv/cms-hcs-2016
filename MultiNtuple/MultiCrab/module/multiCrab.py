
#//////////////////////////////////////////////////////
#                                                     #
# CRAB Command to submit multiple datasets in one go. #
#                                                     #
#//////////////////////////////////////////////////////

from subprocess import call, check_output
import sys, os
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException
from sampleKeyVal import *

#Documentations about multicrab:
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRABClientLibraryAPI#Example_submitting_multiple_task
#https://lost-contact.mit.edu/afs/cern.ch/ubackup/z/zdemirag/public/forSid/crabNero_80X.py

def multiCrabSubmit(config, path_T2):
    ### for some reason only the first dataset is submitted correctly, work around
    if len(sys.argv) ==1:
        ## book the command and run python
        cmd = "python " + sys.argv[0] + " '" + config.General.requestName + "'"
        print ""
        print "calling: "+cmd
        call(cmd,shell=True)
        return
    if len(sys.argv) > 1:
        ## if it is not in the request try the next
        if sys.argv[1] !=  config.General.requestName: return
        toPrint("Submitting", "\033[01;32m" + config.Data.inputDataset.split('/')[1] + "\033[00m")
        #toPrint("outLFNDirBase at T2", "/cms"+path_T2)
        config.Data.outputDatasetTag = config.General.requestName
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
import os
def execme(cmd):
    os.system(cmd)

def createMuMCpsetFile(muMC, ntuple_cfg, mc, m):
    samp_code = getMCKey(mc, m)
    t2_ntuple = samp_code+"_"+ muMC+ "_Ntuple.root"
    pset_file = samp_code+ "_"+ muMC+ "_cfg.py"
    execme("cp "+ntuple_cfg+ " "+ pset_file)
    execme('sed -i '+'s/isData=True/isData=False/g'+ " "+ pset_file)
    execme('sed -i '+'s/outFile_.root/'+t2_ntuple+'/g'+ " "+ pset_file)
    execme('sed -i '+'s/sampCode_/'+samp_code+'/g'+ " "+ pset_file)
    execme('mv '+pset_file+ " config/")
    #print "\033[01;32m"+ " config file created: "+ "\033[00m",  pset_file

def createEleMCpsetFile(eleMC, ntuple_cfg, mc, m):
    samp_code = getMCKey(mc, m)
    t2_ntuple = samp_code+"_"+ eleMC+ "_Ntuple.root"
    pset_file = samp_code+ "_"+ eleMC+ "_cfg.py"
    execme("cp "+ntuple_cfg+ " "+ pset_file)
    execme('sed -i '+'s/isData=True/isData=False/g'+ " "+ pset_file)
    execme('sed -i '+'s/outFile_.root/'+t2_ntuple+'/g'+ " "+ pset_file)
    execme('sed -i '+'s/sampCode_/'+samp_code+'/g'+ " "+ pset_file)
    execme('mv '+pset_file+ " config/")
    #print "\033[01;32m"+ "config file created: "+ "\033[00m",  pset_file

def createMuDatapsetFile(muData, ntuple_cfg, data, d):
    samp_code = getDataKey(data, d)
    t2_ntuple = samp_code+"_"+ muData+ "_Ntuple.root"
    pset_file = samp_code+ "_"+ muData+ "_cfg.py"
    execme("cp "+ntuple_cfg+ " "+ pset_file)
    execme('sed -i '+'s/isData=False/isData=True/g'+ " "+ pset_file)
    execme('sed -i '+'s/outFile_.root/'+t2_ntuple+'/g'+ " "+ pset_file)
    execme('sed -i '+'s/sampCode_/'+samp_code+'/g'+ " "+ pset_file)
    execme('mv '+pset_file+ " config/")
    #print "\033[01;32m"+ "config file created: "+ "\033[00m",  pset_file

def createEleDatapsetFile(eleData, ntuple_cfg, data, d):
    samp_code = getDataKey(data, d)
    t2_ntuple = samp_code+"_"+ eleData+ "_Ntuple.root"
    pset_file = samp_code+ "_"+ eleData+ "_cfg.py"
    execme("cp "+ntuple_cfg+ " "+ pset_file)
    execme('sed -i '+'s/isData=False/isData=True/g'+ " "+ pset_file)
    execme('sed -i '+'s/outFile_.root/'+t2_ntuple+'/g'+ " "+ pset_file)
    execme('sed -i '+'s/sampCode_/'+samp_code+'/g'+ " "+ pset_file)
    execme('mv '+pset_file+ " config/")
    #print "\033[01;32m"+ "config file created: "+ "\033[00m",  pset_file

