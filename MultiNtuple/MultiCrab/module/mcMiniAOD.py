import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

# MC Samples of Charged Higgs & Bkg at 13 TeV
run = "RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6"
runHig = "RunIISummer16MiniAODv2-PUMoriond17_HIG083_80X_mcRun2_asymptotic_2016_TrancheIV_v6"
year = run+"-v1"
yext1_v1 = run +"_ext1-v1"
yext1_v2 = run +"_ext1-v2"
M = "/MINIAODSIM"
#muon channel
mcMuSampDict_ ={
        "ST_tWChannel_antitop": "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_tChannel_antitop": "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_tWChannel_top": "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_tChannel_top": "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_sChannel_incl": "/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/"+year+M
        }
'''
mcMuSampDict_ ={
        "TTJetsM": "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "TTJetsP": "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_up": "/TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_down": "/TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_mtop1735": "/TT_TuneCUETP8M2T4_mtop1735_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_mtop1715": "/TT_TuneCUETP8M2T4_mtop1715_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_hdampUP": "/TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_hdampDOWN": "/TT_hdampDOWN_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "ST_tWChannel_antitop": "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_tChannel_antitop": "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_tWChannel_top": "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_tChannel_top": "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_sChannel_incl": "/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/"+year+M,
        "WJetsToLNu": "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W1JetsToLNu": "/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W2JetsToLNu": "/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W3JetsToLNu": "/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W4JetsToLNu": "/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DYJetsToLL": "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+yext1_v2+M,
        "DY1JetsToLL": "/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY2JetsToLL": "/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY3JetsToLL": "/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY4JetsToLL": "/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "QCD_Pt-15to20_Mu": "/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-20to30_Mu": "/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-30to50_Mu": "/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-50to80_Mu": "/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-80to120_Mu": "/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-120to170_Mu": "/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-170to300_Mu": "/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-300to470_Mu": "/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "WW": "/WW_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "WZ": "/WZ_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "ZZ": "/ZZ_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "HplusM80": "/ChargedHiggsToCS_M080_13TeV-madgraph/"+year+M,
        "HplusM90": "/ChargedHiggsToCS_M090_13TeV-madgraph/"+year+M,
        "HplusM100": "/ChargedHiggsToCS_M100_13TeV-madgraph/"+year+M,
        "HplusM120": "/ChargedHiggsToCS_M120_13TeV-madgraph/"+year+M,
        "HplusM140": "/ChargedHiggsToCS_M140_13TeV-madgraph/"+year+M,
        "HplusM150": "/ChargedHiggsToCS_M150_13TeV-madgraph/"+year+M,
        "HplusM155": "/ChargedHiggsToCS_M155_13TeV-madgraph/"+year+M,
        "HplusM160": "/ChargedHiggsToCS_M160_13TeV-madgraph/"+year+M
        }
'''
mcMuSampDict= OrderedDict(sorted(mcMuSampDict_.items(), key=lambda t: t[0]))

#electron channel
mcEleSampDict_ ={
        "ST_tWChannel_antitop": "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_tChannel_antitop": "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_tWChannel_top": "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_tChannel_top": "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_sChannel_incl": "/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/"+year+M
        }

'''
mcEleSampDict_ ={
        "TTJetsM": "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "TTJetsP": "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_up": "/TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_down": "/TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_mtop1735": "/TT_TuneCUETP8M2T4_mtop1735_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_mtop1715": "/TT_TuneCUETP8M2T4_mtop1715_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_hdampUP": "/TT_hdampUP_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "TTJetsP_hdampDOWN": "/TT_hdampDOWN_TuneCUETP8M2T4_13TeV-powheg-pythia8/"+year+M,
        "ST_tWChannel_antitop": "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_tChannel_antitop": "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_tWChannel_top": "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/"+yext1_v1+M,
        "ST_tChannel_top": "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/"+year+M,
        "ST_sChannel_incl": "/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/"+year+M,
        "WJetsToLNu": "/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W1JetsToLNu": "/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W2JetsToLNu": "/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W3JetsToLNu": "/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "W4JetsToLNu": "/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DYJetsToLL": "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+yext1_v2+M,
        "DY1JetsToLL": "/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY2JetsToLL": "/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY3JetsToLL": "/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "DY4JetsToLL": "/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/"+year+M,
        "QCD_Pt-20to30_EM": "/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-30to50_EM": "/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-50to80_EM": "/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-80to120_EM": "/QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-120to170_EM": "/QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-170to300_EM": "/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "QCD_Pt-300toInf_EM": "/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/"+year+M,
        "WW": "/WW_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "WZ": "/WZ_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "ZZ": "/ZZ_TuneCUETP8M1_13TeV-pythia8/"+year+M,
        "HplusM80": "/ChargedHiggsToCS_M080_13TeV-madgraph/"+year+M,
        "HplusM90": "/ChargedHiggsToCS_M090_13TeV-madgraph/"+year+M,
        "HplusM100": "/ChargedHiggsToCS_M100_13TeV-madgraph/"+year+M,
        "HplusM120": "/ChargedHiggsToCS_M120_13TeV-madgraph/"+year+M,
        "HplusM140": "/ChargedHiggsToCS_M140_13TeV-madgraph/"+year+M,
        "HplusM150": "/ChargedHiggsToCS_M150_13TeV-madgraph/"+year+M,
        "HplusM155": "/ChargedHiggsToCS_M155_13TeV-madgraph/"+year+M,
        "HplusM160": "/ChargedHiggsToCS_M160_13TeV-madgraph/"+year+M
        }
'''
mcEleSampDict= OrderedDict(sorted(mcEleSampDict_.items(), key=lambda t: t[0]))

'''
########################## H -> BB, CC, WW, GG ########################
mcMuSampDict_ ={
        "GluGluHToBB":              "/GluGluHToBB_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToTauTau":          "/GluGluHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToCC":              "/GluGluHToCC_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToGG":              "/GluGluHToGG_M-125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToWWTo2L2Nu":       "/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToWWToLNuQQ":       "/GluGluHToWWToLNuQQ_M125_13TeV_powheg_JHUGenV628_pythia8/"+run+"-v1"+M,
        "GluGluHToZZTo2L2Q":        "/GluGluHToZZTo2L2Q_M125_13TeV_powheg2_JHUGenV709_pythia8/"+runHig+"-v2/MINIAODSIM",
        "GluGluHToZZTo4L":          "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV709_pythia8/"+run+"-v1"+M,

        "WplusH_HToBB_WToLNu":      "/WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToBB_WToQQ":       "/WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusHToTauTau":           "/WplusHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToCC_WToLNu":      "/WplusH_HToCC_WToLNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToCC_WToQQ":       "/WplusH_HToCC_WToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToGG_WToAll":      "/WplusH_HToGG_WToAll_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,

        "WminusH_HToBB_WToQQ":      "/WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusHToTauTau":          "/WminusHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusH_HToCC_WToLNu":     "/WminusH_HToCC_WToLNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusH_HToCC_WToQQ":      "/WminusH_HToCC_WToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusH_HToGG_WToAll":     "/WminusH_HToGG_WToAll_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusH_HToZZTo2L2X":      "/WminusH_HToZZTo2L2X_M125_13TeV_powheg2-minlo-HWJ_JHUGenV709_pythia8/"+runHig+"-v1/MINIAODSIM",

        "ZH_HToBB_ZToNuNu":         "/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/"+run+"_ext1-v1"+M,
        "ZH_HToBB_ZToLL":           "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToBB_ZToQQ":           "/ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZHToTauTau":               "/ZHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToCC_ZToNuNu":         "/ZH_HToCC_ZToNuNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToCC_ZToLL":           "/ZH_HToCC_ZToLL_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToCC_ZToQQ":           "/ZH_HToCC_ZToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToGG_ZToAll":          "/ZH_HToGG_ZToAll_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToZZ_2L":              "/ZH_HToZZ_2LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV709_pythia8/"+runHig+"-v2/MINIAODSIM",

        "ggZH_HToBB_ZToNuNu":       "/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToBB_ZToLL":         "/ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToBB_ZToQQ":         "/ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToCC_ZToNuNu":       "/ggZH_HToCC_ZToNuNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToCC_ZToLL":         "/ggZH_HToCC_ZToLL_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToCC_ZToQQ":         "/ggZH_HToCC_ZToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluZH_HToWW":           "/GluGluZH_HToWW_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,

        "ttHToCC":                  "/ttHToCC_M125_TuneCUETP8M2_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ttHToGG":                  "/ttHToGG_M125_13TeV_powheg_pythia8_v2/"+run+"-v1"+M,

        "bbHToBB":                  "/bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo/"+run+"-v1"+M,
        "bbHToGG":                  "/bbHToGG_M-125_4FS_yb2_13TeV_amcatnlo/"+run+"-v1"+M,
        "bbHToWWTo2L2Nu":           "/bbHToWWTo2L2Nu_M-125_4FS_yb2_13TeV_amcatnlo/"+run+"-v1"+M,
        "bbH_HToZZTo4L":            "/bbH_HToZZTo4L_M125_13TeV_JHUgenV702_pythia8/"+run+"-v1"+M,

        "VBFHToBB":                 "/VBFHToBB_M-125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToTauTau":             "/VBFHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToCC":                 "/VBFHToCC_M-125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToGG":                 "/VBFHToGG_M-125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToWWTo2L2Nu":          "/VBFHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToWWToLNuQQ":          "/VBFHToWWToLNuQQ_M125_13TeV_powheg_JHUGenV628_pythia8/"+run+"-v1"+M

}
mcMuSampDict= OrderedDict(sorted(mcMuSampDict_.items(), key=lambda t: t[0]))

mcEleSampDict_ ={
        "GluGluHToBB":              "/GluGluHToBB_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToTauTau":          "/GluGluHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToCC":              "/GluGluHToCC_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToGG":              "/GluGluHToGG_M-125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToWWTo2L2Nu":       "/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluHToWWToLNuQQ":       "/GluGluHToWWToLNuQQ_M125_13TeV_powheg_JHUGenV628_pythia8/"+run+"-v1"+M,
        "GluGluHToZZTo2L2Q":        "/GluGluHToZZTo2L2Q_M125_13TeV_powheg2_JHUGenV709_pythia8/"+runHig+"-v2/MINIAODSIM",
        "GluGluHToZZTo4L":          "/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV709_pythia8/"+run+"-v1"+M,

        "WplusH_HToBB_WToLNu":      "/WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToBB_WToQQ":       "/WplusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusHToTauTau":           "/WplusHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToCC_WToLNu":      "/WplusH_HToCC_WToLNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToCC_WToQQ":       "/WplusH_HToCC_WToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToGG_WToAll":      "/WplusH_HToGG_WToAll_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,

        "WminusH_HToBB_WToQQ":      "/WminusH_HToBB_WToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusHToTauTau":          "/WminusHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusH_HToCC_WToLNu":     "/WminusH_HToCC_WToLNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusH_HToCC_WToQQ":      "/WminusH_HToCC_WToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusH_HToGG_WToAll":     "/WminusH_HToGG_WToAll_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WminusH_HToZZTo2L2X":      "/WminusH_HToZZTo2L2X_M125_13TeV_powheg2-minlo-HWJ_JHUGenV709_pythia8/"+runHig+"-v1/MINIAODSIM",

        "ZH_HToBB_ZToNuNu":         "/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/"+run+"_ext1-v1"+M,
        "ZH_HToBB_ZToLL":           "/ZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToBB_ZToQQ":           "/ZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZHToTauTau":               "/ZHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToCC_ZToNuNu":         "/ZH_HToCC_ZToNuNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToCC_ZToLL":           "/ZH_HToCC_ZToLL_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToCC_ZToQQ":           "/ZH_HToCC_ZToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToGG_ZToAll":          "/ZH_HToGG_ZToAll_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ZH_HToZZ_2L":
        "/ZH_HToZZ_2LFilter_M125_13TeV_powheg2-minlo-HZJ_JHUGenV709_pythia8/"+runHig+"-v2/MINIAODSIM",

        "ggZH_HToBB_ZToNuNu":       "/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToBB_ZToLL":         "/ggZH_HToBB_ZToLL_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToBB_ZToQQ":         "/ggZH_HToBB_ZToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToCC_ZToNuNu":       "/ggZH_HToCC_ZToNuNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToCC_ZToLL":         "/ggZH_HToCC_ZToLL_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ggZH_HToCC_ZToQQ":         "/ggZH_HToCC_ZToQQ_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "GluGluZH_HToWW":           "/GluGluZH_HToWW_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,

        "ttHToCC":                  "/ttHToCC_M125_TuneCUETP8M2_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ttHToGG":                  "/ttHToGG_M125_13TeV_powheg_pythia8_v2/"+run+"-v1"+M,

        "bbHToBB":                  "/bbHToBB_M-125_4FS_yb2_13TeV_amcatnlo/"+run+"-v1"+M,
        "bbHToGG":                  "/bbHToGG_M-125_4FS_yb2_13TeV_amcatnlo/"+run+"-v1"+M,
        "bbHToWWTo2L2Nu":           "/bbHToWWTo2L2Nu_M-125_4FS_yb2_13TeV_amcatnlo/"+run+"-v1"+M,
        "bbH_HToZZTo4L":            "/bbH_HToZZTo4L_M125_13TeV_JHUgenV702_pythia8/"+run+"-v1"+M,

        "VBFHToBB":                 "/VBFHToBB_M-125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToTauTau":             "/VBFHToTauTau_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToCC":                 "/VBFHToCC_M-125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToGG":                 "/VBFHToGG_M-125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToWWTo2L2Nu":          "/VBFHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "VBFHToWWToLNuQQ":          "/VBFHToWWToLNuQQ_M125_13TeV_powheg_JHUGenV628_pythia8/"+run+"-v1"+M
}
mcEleSampDict= OrderedDict(sorted(mcEleSampDict_.items(), key=lambda t: t[0]))
'''

'''
To be processed
mcMuSampDict_ ={
        "WminusH_HToBB_WToLNu":     "/WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WHiggs0PHToWW_2L":         "/WHiggs0PHToWW_2LFilter_M-125_13TeV-JHUGenV6_pythia8/"+run+"-v1"+M,
        "HZJ_HToWW":                "/HZJ_HToWW_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "ttHTobb_M125":             "/ttHTobb_M125_13TeV_powheg_pythia8/"+run+"-v1"+M,
        "WplusH_HToZZTo2L2X":       "/WplusH_HToZZTo2L2X_M125_13TeV_powheg2-minlo-HWJ_JHUGenV709_pythia8/"+runHig+"-v1/MINIAODSIM"
mcMuSampDict= OrderedDict(sorted(mcMuSampDict_.items(), key=lambda t: t[0]))
'''
