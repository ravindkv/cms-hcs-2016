import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

muDataSampDict_ ={
        "MuRunB2v2": "/SingleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD",
        "MuRunCv1":  "/SingleMuon/Run2016C-03Feb2017-v1/MINIAOD",
        "MuRunDv1":  "/SingleMuon/Run2016D-03Feb2017-v1/MINIAOD",
        "MuRunEv1":  "/SingleMuon/Run2016E-03Feb2017-v1/MINIAOD",
        "MuRunFv1":  "/SingleMuon/Run2016F-03Feb2017-v1/MINIAOD",
        "MuRunGv1":  "/SingleMuon/Run2016G-03Feb2017-v1/MINIAOD",
        "MuRunH2v1": "/SingleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD",
        "MuRunH3v1": "/SingleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD"
         }
muDataSampDict= OrderedDict(sorted(muDataSampDict_.items(), key=lambda t: t[0]))

eleDataSampDict_ ={
        "EleRunBver2v2": "/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD",
        "EleRunCv1": "/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD",
        "EleRunDv1": "/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD",
        "EleRunEv1": "/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD",
        "EleRunFv1": "/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD",
        "EleRunGv1": "/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD",
        "EleRunHver2v1": "/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD",
        "EleRunHver3v1": "/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD"
         }
eleDataSampDict= OrderedDict(sorted(eleDataSampDict_.items(), key=lambda t: t[0]))
