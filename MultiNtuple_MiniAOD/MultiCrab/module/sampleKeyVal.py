#///////////////////////////////////////////////////////
#                                                      #
# Define functions to read input datasets, paths at T2 #
#                                                      #
#///////////////////////////////////////////////////////

import datetime
import collections

#Get nth key, value of MC
def getMCVal(mc, n):
    return mc[list(mc)[n]]

def getMCKey(mc, n):
    return list(mc)[n]
    '''
    val = getMCVal(mc, n)
    #today_date = str(datetime.date.today()).replace("-","")
    if val !="":
        start_name = val.split("/")[1].split("_")[0]
        key = start_name #+"_Ntuple"+str(today_date)
        if start_name == "ST":
            start_name = start_name+ "_" +val.split("/")[1].split("_")[1]
            key = start_name #+"_Ntuple"+str(today_date)
            return key
        else:
            return key
    '''
#Get nth key, value of DATA
def getDataVal(data, n):
    return data[list(data)[n]]

def getDataKey(data, n):
    return list(data)[n]
    '''
    val = getDataVal(data, n)
    if val !="":
        name = val.replace("MINIAOD","")
        key = name.replace("/","_").replace("-","_")
        return key
    '''
def getLFNDirBaseMC(lable, mc, m, dirT2 = "ntuple_MuMC"):
    outLFNDirBase = '/store/user/rverma/'+ dirT2+ '/'+ lable+ '/'+getMCKey(mc, m)+"_"+ lable
    return outLFNDirBase

def getLFNDirBaseData(lable, data, m, dirT2='ntuple_MuData'):
    outLFNDirBase = '/store/user/rverma/'+dirT2+ '/'+ lable+ '/'+getDataKey(data, m)+"_"+ lable
    return outLFNDirBase

#PATHS OF NTUPLE AT T2_IN_TIFR
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling
def getNtupleT2Paths(lable, samp, n, dirT2='ntuple_MuData'):
    '''
    /cms/store/user/rverma/
    ntuple/CrabMuonsMC/QCD_ntuple_2017-03-15_MuonsMC/
    QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/
    crab_QCD_ntuple_2017-03-15_MuonsMC/170315_214120/
    0000/W1JetsToLNu_ntuple_2017-03-15_muons_98.root
    '''
    crab_dir = lable
    crab_subdir = getMCKey(samp, n) +"_"+lable
    t2user_dir = '/store/user/rverma/'+dirT2+'/'
    t2crab_dir = crab_dir+'/'+crab_subdir
    t2samp_name = "/"+getMCVal(samp, n).split("/")[1]
    t2samp_subdir = "/"+crab_subdir

    year_full = str(datetime.date.today()).split("-")[0]
    year_short = year_full.replace(year_full[0],"").replace(year_full[1],"")
    month = str(datetime.date.today()).split("-")[1]
    day = str(datetime.date.today()).split("-")[2]
    date = "/"+year_short+ month+ day
    time = "_"+str(datetime.datetime.now().time()).replace(":","").split(".")[0]
    date_time = date + time
    t2ntuple_file = "/0000/"+getMCKey(samp, n)+ lable+ "_Ntuple.root"
    t2full_path = '/cms'+ t2user_dir+ t2crab_dir+ t2samp_name+ t2samp_subdir#+ date_time+ t2ntuple_file

    return t2full_path

#NICE WAY TO PRINT STRINGS
def toPrint(string, value):
    length = (len(string)+len(str(value))+2)
    line = "-"*length
    print "* "+ line +                    " *"
    print "| "+ " "*length +              " |"
    print "| "+ string+ ": "+ str(value)+ " |"
    print "| "+ " "*length +              " |"
    print "* "+ line +                    " *"


