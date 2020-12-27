#HIG-18-021
#pip install --user hepdata_lib
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsHepData
import os
from hepdata_lib import *
import numpy as np
from hepdata_lib import Variable, Uncertainty
from hepdata_lib import Table

table2Yield = [
        [["Process"], ["muL"], ["eleL"], ["muM"], ["eleM"], ["muT"], ["eleT"]],
		[["mhp=80 GeV" ], [7690, 550], [5430, 380], [6560, 490], [4700, 370], [2670, 270], [1860, 180]],
		[["mhp=90 GeV" ], [7710, 550], [5620, 400], [6770, 510], [4860, 380], [2630, 260], [1870, 190]],
		[["mhp=100 GeV"], [7950, 590], [5550, 400], [7070, 540], [4950, 360], [2770, 270], [2000, 200]],
		[["mhp=120 GeV"], [7620, 570], [5360, 400], [6870, 510], [4780, 360], [2650, 260], [1960, 190]],
		[["mhp=140 GeV"], [6160, 500], [4370, 360], [5420, 420], [3840, 310], [2010, 210], [1500, 150]],
		[["mhp=150 GeV"], [4530, 390], [3230, 280], [3850, 330], [2800, 250], [1340, 140], [1030, 120]],
		[["mhp=155 GeV"], [3700, 340], [2560, 250], [2980, 270], [2230, 220], [1020, 120], [766, 86]],
		[["mhp=160 GeV"], [2780, 270], [2080, 200], [2370, 230], [1710, 180], [728, 83], [510, 59]],
		[["ttbar"], [100540, 410], [71800, 470], [73210, 320], [52340, 290], [18760, 130], [13380, 130]],
		[["Single t quark"], [2750, 220], [1970, 160], [1940, 160], [1400, 110], [421, 35], [302, 26]],
		[["QCD multijet"], [520, 130], [2120, 470], [498, 98], [1460, 210], [88, 28], [346, 39]],
		[["W + jets"], [1360, 140], [1061, 90], [950, 110], [681, 58], [127, 23], [102, 9]],
		[["Z/gamma +jets"], [189, 18], [240, 25], [132, 13], [132, 14], [56, 7], [31, 4]],
		[["VV"], [61, 9], [43, 6], [56, 8], [11, 4], [15, 5], [3, 1]],
		[["All background"], [105410, 500], [77240, 690], [76780, 390], [56020, 380], [19470, 140], [14160, 140]],
		[["Data"], [105474, 325], [77244, 278], [76807, 277], [56051, 237], [19437, 139], [14179, 119]]
		]

table3Syst = [
		[["Category"], ["Process"], ["Pileup"], ["jet"], ["ptmiss"], ["PQb"], ["PQc jets"], ["Normalization"], ["Statistical"], ["pT (t)"]],
		[["Loose"], ["mhp=100 GeV"], [0.6 ,1.1], [4.2 ,3.5], [6.1 ,6.1], [6.1 ,6.1], [1.0 ,1.2], [1.4 ,1.8]],
		[["Loose"], ["ttbar"], [0.9 ,1.1], [3.6 ,3.6], [5.8 ,5.8], [6.1 ,6.1], [0.2 ,0.2], [1.5 ,1.9]],
		[["Loose"], ["Single t quark"], [0.6 ,0.8], [4.9 ,5.4], [6.5 ,6.6], [5.0 ,5.0], [0.7 ,0.8], ["-", "-"]],
		[["Loose"], ["W + jets"], [2.3 ,0.4], [13 ,6.9], [10 ,10], [5.0 ,5.0], [3.9 ,4.5], ["-", "-"]],
		[["Loose"], ["Z/g + jets"], [1.8 ,2.4], [11 ,8.4], [9.2 ,9.0], [4.5 ,4.5], [5.7 ,4.2], ["-", "-"]],
		[["Loose"], ["VV"], [1.5 ,7.9], [19 ,13], [7.2 ,7.0], [4.0 ,4.0], [19 ,22], ["-", "-"]],
		[["Loose"], ["QCD multijet"], ["-", "-"], ["-", "-"], ["-", "-"], [10 ,10], [20 ,7.3], ["-", "-"]],
		[["Medium"], ["mhp=100 GeV"], [0.4 ,0.3], [3.5 ,2.0], [6.7 ,6.8], [6.1 ,6.1], [1.1 ,1.3], [1.6 ,1.9]],
		[["Medium"], ["ttbar"], [0.3 ,0.4], [3.0 ,3.0], [7.3 ,7.3], [6.1 ,6.1], [0.2 ,0.3], [1.5 ,2.0]],
		[["Medium"], ["Single t quark"], [0.3 ,0.1], [4.4 ,4.1], [8.1 ,8.1], [5.0 ,5.0], [0.9 ,1.0], ["-", "-"]],
		[["Medium"], ["W + jets"], [2.9 ,1.6], [14 ,6.8], [12 ,11], [5.0 ,5.0], [4.8 ,5.7], ["-", "-"]],
		[["Medium"], ["Z/g + jets"], [0.7 ,3.4], [9.0 ,11], [12 ,11], [4.5 ,4.5], [5.9 ,5.9], ["-", "-"]],
		[["Medium"], ["VV"], [0.6 ,4.4], [15 ,49], [10 ,9.4], [4.0 ,4.0], [20 ,36], ["-", "-"]],
		[["Medium"], ["QCD multijet"], ["-", "-"], ["-", "-"], ["-", "-"], [10 ,10], [19 ,9.4], ["-", "-"]],
		[["Tight"], ["mhp=100 GeV"], [1.2 ,1.3], [2.2 ,3.0], [9.2 ,9.2], [6.1 ,6.1], [1.6 ,1.9], [1.4 ,1.8]],
		[["Tight"], ["ttbar"], [0.9 ,1.0], [2.7 ,3.1], [9.4 ,9.4], [6.1 ,6.1], [0.4 ,0.5], [1.4 ,1.8]],
		[["Tight"], ["Single t quark"], [0.4 ,0.5], [4.3 ,4.5], [9.8 ,9.8], [5.0 ,5.0], [1.8 ,2.1], ["-", "-"]],
		[["Tight"], ["W + jets"], [1.1 ,2.8], [23 ,3.4], [13 ,13], [5.0 ,5.0], [12 ,14], ["-", "-"]],
		[["Tight"], ["Z/g + jets"], [3.7 ,2.7], [7.5 ,10], [13 ,12], [4.5 ,4.5], [9.1 ,15], ["-", "-"]],
		[["Tight"], ["VV"], [2.3 ,8.9], [36 ,0.3], [11 ,10], [4.0 ,4.0], [38 ,100], ["-", "-"]],
		[["Tight"], ["QCD multijet"], ["-", "-"], ["-", "-"], ["-", "-"], [10 ,10], [47 ,17], ["-", "-"]]
		] 
def getCol(arr, isMu):
    col = []
    for e in arr:
        if isMu:
            col.append(e[0])
        else:
            col.append(e[1])
    return col
#-----------------------------	
#Limit tables
#-----------------------------	
table4Limit = np.array([	
		[[80 ], [1.58, 1.96], [2.10, 2.61], [2.95, 3.63], [4.16, 5.10], [5.61, 6.84], [2.44, 2.77]],
		[[90 ], [0.69, 0.79], [0.92, 1.06], [1.28, 1.47], [1.79, 2.05], [2.39, 2.74], [0.72, 1.38]],
		[[100], [0.35, 0.42], [0.46, 0.56], [0.64, 0.77], [0.90, 1.08], [1.19, 1.43], [0.34, 0.53]],
		[[120], [0.24, 0.28], [0.32, 0.37], [0.44, 0.52], [0.61, 0.72], [0.82, 0.95], [0.32, 0.44]],
		[[140], [0.21, 0.24], [0.28, 0.32], [0.39, 0.44], [0.54, 0.61], [0.72, 0.81], [0.47, 0.32]],
		[[150], [0.20, 0.23], [0.27, 0.31], [0.37, 0.43], [0.52, 0.60], [0.69, 0.80], [0.52, 0.26]],
		[[155], [0.20, 0.23], [0.27, 0.31], [0.38, 0.42], [0.53, 0.60], [0.71, 0.80], [0.57, 0.26]],
		[[160], [0.22, 0.26], [0.30, 0.35], [0.42, 0.48], [0.59, 0.68], [0.80, 0.92], [0.53, 0.32]]
		])
table5Limit = np.array([
		[80 , 1.29, 1.72, 2.39, 3.36, 4.50, 1.68],
		[90 , 0.54, 0.72, 0.99, 1.38, 1.84, 0.60],
		[100, 0.28, 0.37, 0.51, 0.71, 0.94, 0.25],
		[120, 0.19, 0.25, 0.35, 0.49, 0.64, 0.25],
		[140, 0.17, 0.22, 0.31, 0.42, 0.56, 0.28],
		[150, 0.16, 0.21, 0.29, 0.41, 0.54, 0.26],
		[155, 0.16, 0.21, 0.29, 0.41, 0.54, 0.28],
		[160, 0.17, 0.23, 0.32, 0.45, 0.61, 0.29]
		])
def makeTableLimit(outdir, isLep, isMu):
    #observed 
    d = Variable("Mass of charged Higgs", is_independent=True, is_binned=False, units="GeV")
    obs = Variable("BR (t->H+ b) upper limit at 95% CL", is_independent=False, is_binned=False, units="%")
    obs.add_qualifier("Limit", "Observed")
    obs.add_qualifier("SQRT(S)", 13, "TeV")
    obs.add_qualifier("LUMINOSITY", 35.9, "fb$^{-1}$")
    #expected
    exp = Variable("BR (t->H+ b) upper limit at 95% CL", is_independent=False, is_binned=False, units="%")
    exp.add_qualifier("Limit", "Expected")
    exp.add_qualifier("SQRT(S)", 13, "TeV")
    exp.add_qualifier("LUMINOSITY", 35.9, "fb$^{-1}$")
    # +/- 1 sigma
    unc_1s = Uncertainty("1 s.d.", is_symmetric=False)
    # +/- 2 sigma
    unc_2s = Uncertainty("2 s.d.", is_symmetric=False)
    if not isLep:
        d.values = table5Limit[:,0] # first column
        obs.values = getCol(table4Limit[:,-1], isMu) # last column
        exp.values = getCol(table4Limit[:,3], isMu)
        unc_1s.set_values_from_intervals(zip(getCol(table4Limit[:,2], isMu), 
            getCol(table4Limit[:,4], isMu)), nominal=exp.values)
        unc_2s.set_values_from_intervals(zip(getCol(table4Limit[:,1], isMu), 
            getCol(table4Limit[:,5], isMu)), nominal=exp.values)
        if isMu:
            table = Table("Figure 4a")
            table.location = "Data from Figure 4a"
            table.add_image("./Figure_004-a.pdf")
            table.description = "Expected and observed 95% CL exclusion limits in % on BR(t->H+ b) for the muon channel after the individual charm tagging categories have been combined."
        else:
            table = Table("Figure 4b")
            table.location = "Data from Figure 4b"
            table.add_image("./Figure_004-b.pdf")
            table.description = "Expected and observed 95% CL exclusion limits in % on BR(t->H+ b) for the electron channel after the individual charm tagging categories have been combined."
    else:
        d.values = table5Limit[:,0] # first column
        obs.values = table5Limit[:,-1] # last column
        exp.values = table5Limit[:,3]
        unc_1s.set_values_from_intervals(zip(table5Limit[:,2], table5Limit[:,4]), nominal=exp.values)
        unc_2s.set_values_from_intervals(zip(table5Limit[:,1], table5Limit[:,5]), nominal=exp.values)
        table = Table("Figure 4c")
        table.location = "Data from Figure 4c"
        table.add_image("./Figure_004-c.pdf")
        table.description = "Expected and observed 95% CL exclusion limits in % on BR(t->H+ b) after the individual charm tagging categories and the muon and electron channels have been combined."
    table.keywords["observables"] = ["SIG"]
    table.keywords["reactions"] = ["p p > t t~, ( t > h+ b, ( h+ > c s~ )), ( t~ > w- b~, ( w- > l- vl~ ))"]
    exp.add_uncertainty(unc_1s)
    exp.add_uncertainty(unc_2s)
    #add to tables
    table.add_variable(d)
    table.add_variable(obs)
    table.add_variable(exp)
    return table

def main():
    # Write to this directory
    outdir = "./hepdata"
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    with open("%s/abstract.txt"%outdir, "w") as abstract:
        abstract.write("A search is conducted for a low-mass charged Higgs boson produced\
        in a top quark decay and subsequently decaying into a charm and\
        a strange quark. The data sample was recorded in proton-proton\
        collisions at $\sqrt{s}=13 TeV$ by the CMS experiment at the LHC\
        and corresponds to an integrated luminosity of 35.9/fb. The search\
        is performed in the process of top quark pair production,\
        where one top quark decays to a bottom quark and a charged Higgs\
        boson, and the other to a bottom quark and a W boson. With\
        the W boson decaying to a charged lepton (electron or muon) and a\
        neutrino, the final state comprises an isolated lepton, missing\
        transverse momentum, and at least four jets, of which two are tagged\
        as b jets. To enhance the search sensitivity, one of the jets\
        originating from the charged Higgs boson is required to satisfy a\
        charm tagging selection. No significant excess beyond standard model\
        predictions is found in the dijet invariant mass distribution. An\
        upper limit in the range 1.68--0.25% is set on the branching fraction\
        of the top quark decay to the charged Higgs boson and bottom quark for\
        a charged Higgs boson mass between 80 and 160 GeV.")
        abstract.close()
    # Write some files
    submission = Submission()
    submission.tables.append(makeTableLimit(outdir, False, True))
    submission.tables.append(makeTableLimit(outdir, False, False))
    submission.tables.append(makeTableLimit(outdir, True, False))
    submission.read_abstract("%s/abstract.txt"%outdir)
    submission.add_link("Webpage with all figures and tables", "http://cms-results.web.cern.ch/cms-results/public-results/publications/HIG-18-021/")
    submission.add_link("arXiv", "http://arxiv.org/abs/2005.08900")
    submission.add_record_id(1796727, "inspire")
    submission.create_files(outdir)

if __name__ == '__main__':
    main()
