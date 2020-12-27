import FWCore.ParameterSet.Config as cms

#----------------------------------------------------------
#NICE WAY TO PRINT STRINGS
#----------------------------------------------------------
def toPrint(string, value):
    length = (len(string)+len(str(value))+2)
    line = "-"*length
    print ""
    print "* "+ line +                    " *"
    print "| "+ " "*length +              " |"
    print "| "+ string+ ": "+ str(value)+ " |"
    print "| "+ " "*length +              " |"
    print "* "+ line +                    " *"

#----------------------------------------------------------
# MET filters
#----------------------------------------------------------
# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/PhysicsTools/PatAlgos/python/slimming/metFilterPaths_cff.py
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#2016_data
# Muon
from RecoMET.METFilters.metFilters_cff import BadChargedCandidateFilter, BadPFMuonFilter #2016 post-ICHEPversion
def addMETFilters(process):
    # Muon
    process.BadChargedCandidateFilter = BadChargedCandidateFilter.clone()
    process.BadChargedCandidateFilter.muons  = cms.InputTag("slimmedMuons")
    process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
    process.BadChargedCandidateFilter.taggingMode = True
    process.BadPFMuonFilter = BadPFMuonFilter.clone()
    process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
    process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
    process.BadPFMuonFilter.taggingMode = True
    process.metFilterSequence = cms.Sequence(process.BadPFMuonFilter*
            process.BadChargedCandidateFilter
            )

#----------------------------------------------------------
# Jet corrections: L1, L2, L3: Already applied at the MiniAOD level
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC#2016_Data
# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_20_patchX/PhysicsTools/PatAlgos/python/tools/jetTools.py
#----------------------------------------------------------
'''
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
def addCorrJetL1L2L3(process, isData):
    levels = ['L1FastJet','L2Relative','L3Absolute']
    if(isData): levels.append('L2L3Residual')
    myLevels = cms.vstring(levels)
    updateJetCollection(
            process,
            jetSource = cms.InputTag('slimmedJets'),
            postfix = 'UpdatedJEC',
            #jetCorrections = ('AK4PFchs', myLevels, 'None'),
            jetCorrections = ('AK8PF', myLevels, 'None'),
            )
    process.corrJetsProducerSequence = cms.Sequence(process.patJetCorrFactorsUpdatedJEC *process.updatedPatJetsUpdatedJEC)
    toPrint("Jet Energy Corrections:", levels)
# Note: Once this producer is run, the jet collection will be accessed by
# "updatedPatJetsUpdatedJEC" string, instead of "slimmedJets".
'''

