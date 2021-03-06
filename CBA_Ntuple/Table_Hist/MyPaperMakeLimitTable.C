#include <iostream>
#include <fstream>
#include <iomanip>

void makeLimitTable(TString CHANNEL, TString CAT,
         bool isObs, bool isOut, ofstream & outFile)
  {

  float X[]        = {80, 90,100,120, 140, 150, 155, 160};
  float obsY[]     = {0., 0.,0.,0, 0, 0, 0, 0,0};
  float expY[]     = {0., 0.,0.,0, 0, 0, 0, 0,0};
		      
  float expX1sL[]   = {0.,0.,0.,0, 0, 0, 0, 0,0};
  float expX1sH[]   = {0.,0.,0.,0, 0, 0, 0, 0,0};
  float expY1sL[]   = {0.,0.,0.,0, 0, 0, 0, 0,0};
  float expY1sH[]   = {0.,0.,0.,0, 0, 0, 0, 0,0};
		      
  float expX2sL[]  = {0.,0.,0.,0, 0, 0, 0, 0,0};
  float expX2sH[]  = {0.,0.,0.,0, 0, 0, 0, 0,0};
  float expY2sL[]  = {0.,0.,0.,0, 0, 0, 0, 0,0};
  float expY2sH[]  = {0.,0.,0.,0, 0, 0, 0, 0,0};

  float expY1sL_[]   = {0.,0.,0.,0, 0, 0, 0, 0,0};
  float expY1sH_[]   = {0.,0.,0.,0, 0, 0, 0, 0,0};

  int nMassPoints = 8;
  TString ch_hist = CHANNEL+"_"+CAT;
  TString massFiles [8] = {
  "Mass80/higgsCombine_hcs_13TeV_"+ch_hist+".AsymptoticLimits.mH80.root",
  "Mass90/higgsCombine_hcs_13TeV_"+ch_hist+".AsymptoticLimits.mH90.root",
  "Mass100/higgsCombine_hcs_13TeV_"+ch_hist+".AsymptoticLimits.mH100.root",
  "Mass120/higgsCombine_hcs_13TeV_"+ch_hist+".AsymptoticLimits.mH120.root",
  "Mass140/higgsCombine_hcs_13TeV_"+ch_hist+".AsymptoticLimits.mH140.root",
  "Mass150/higgsCombine_hcs_13TeV_"+ch_hist+".AsymptoticLimits.mH150.root",
  "Mass155/higgsCombine_hcs_13TeV_"+ch_hist+".AsymptoticLimits.mH155.root",
  "Mass160/higgsCombine_hcs_13TeV_"+ch_hist+".AsymptoticLimits.mH160.root"};
  
  for(unsigned int i = 0 ; i < nMassPoints; i++){
    TFile f("limit/"+CHANNEL+"/"+CAT+"/"+massFiles[i],"READ"); 
    if(f.IsZombie()){
      cout << "Cannot open file for " << string(CHANNEL.Data()) << " and mass " << X[i] << endl;
      continue;
    }
    Double_t r;
    TTree* limit = (TTree*)f.Get("limit");
    limit->SetBranchAddress("limit",&r);
    
    for(int k = 0 ; k< limit->GetEntries() ; k++){
      limit->GetEntry(k);
      r = r*100;
      if(k==0) expY2sL[i] = r;
      if(k==1) expY1sL[i] = r;
      if(k==1) expY1sL_[i] = r;
      if(k==2) expY[i]    = r;
      if(k==3) expY1sH[i] = r;
      if(k==3) expY1sH_[i] = r;
      if(k==4) expY2sH[i] = r;
      if(k==5) obsY[i]    = r;
    }
  }
  cout<<std::setprecision(4)<<endl;
  cout<<CHANNEL<<": "<<CAT<<endl;
  cout<<"Mass:"<<setw(10)<<"base value"<<setw(10)<<"-2 #sigma"<<setw(10)<<"-1 #sigma"<<setw(10)<<"+1 #sigma"<<setw(10)<<"+2 #sigma"<<setw(10)<<"Observed"<<endl; 
  TString ch_name = "mu";
  if(CHANNEL=="mu") ch_name = "muon";
  if(CHANNEL=="ele") ch_name = "electron";
  if(CHANNEL=="mu_ele") ch_name = "lepton";

  //make table
  outFile<<"\\begin{table}[ht]"<<endl; 
  outFile<<"\\centering"<<endl; 
  outFile<<"\\topcaption{Expected and observed 95\\% \\CL exclusion limits in \\% on $\\mathcal{B}(\\PQt \\to \\PSHp\\PQb)$ for "+ch_name+" channel, after the individual charm tagging categories have been combined.}"<<endl; 
  outFile<<"\\label{tab:limit_"+ch_name+"}"<<endl;
  outFile<<"\\label{tab:limit_"+ch_name+"}"<<endl;
  outFile<<"\\begin{tabular}{ccccccc}"<<endl; 
  outFile<<"\\hline "<<endl;
  outFile<<"\\multirow{2}{*}{$m_{\\PSHp}$ (\\GeVns)} & \\multicolumn{5}{c}{Expected} & \\multirow{2}{*}{Observed} \\\\ & $-2\\sigma$ & $-1\\sigma$ & median & $+1\\sigma$ & $+2\\sigma$ & \\\\"<<endl;                          
  outFile<<"\\hline "<<endl;
  for(int i1 = 0 ; i1 < nMassPoints ; i1++){
  cout<<X[i1]<<setw(10)<<expY[i1]<<setw(10)<<expY2sL[i1]<<setw(10)<< expY1sL[i1]<<setw(10)<<expY1sH[i1]<<setw(10)<<expY2sH[i1]<<setw(10)<<obsY[i1]<<endl; 
  if(isObs)outFile<<X[i1]<<fixed<<std::setprecision(2)<<" & "<<expY2sL[i1]<<" & "<< expY1sL[i1]<<" & "<<expY[i1]<<" & "<<expY1sH[i1]<<" & "<<expY2sH[i1]<<" & "<<obsY[i1]<<"\\\\"<<endl; 
  else outFile<<X[i1]<<fixed<<std::setprecision(2)<<" & "<<expY2sL[i1]<<" & "<< expY1sL[i1]<<" & "<<expY[i1]<<" & "<<expY1sH[i1]<<" & "<<expY2sH[i1]<<" & "<<"-"<<"\\\\"<<endl; 
  }
  outFile<<"\\hline "<<endl;
  outFile<<"\\end{tabular}"<<endl; 
  outFile<<"\\end{table}"<<endl; 
  outFile<<endl;
  
}

void MyPaperMakeLimitTable(){
  ofstream outFile; 
  outFile.open("limit/paperLimitTable.tex"); 
  //outFile<<"\\documentclass[landscape,letterpaper]{article}"<<endl;  
  outFile<<"\\documentclass[]{article}"<<endl;  
  outFile<<"\\pagestyle{empty}"<<endl;  
  outFile<<"\\usepackage{epsfig}"<<endl;  
  outFile<<"\\usepackage{amsmath}"<<endl;  
  outFile<<"\\usepackage{array}"<<endl;  
  outFile<<"\\usepackage{multirow}"<<endl;  
  outFile<<"\\usepackage[cm]{fullpage}"<<endl;  
  outFile<<"\\begin{document}"<<endl;  
  outFile<<""<<endl;
  //muon 
  bool isObs = true;
  makeLimitTable("mu", "Cat3_cTagEx", isObs, true, outFile);
  makeLimitTable("ele", "Cat3_cTagEx", isObs, true, outFile);
  makeLimitTable("mu_ele","Cat3_cTagEx", isObs, true, outFile);
  /*
  makeLimitTable("mu", "Cat3_cTagExL", isObs, true, outFile);
  makeLimitTable("mu", "Cat3_cTagExM", isObs, true, outFile);
  makeLimitTable("mu", "Cat3_cTagExT", isObs, true, outFile);
  makeLimitTable("ele", "Cat3_cTagExL", isObs, true, outFile);
  makeLimitTable("ele", "Cat3_cTagExM", isObs, true, outFile);
  makeLimitTable("ele", "Cat3_cTagExT", isObs, true, outFile);
  */

  outFile<<"\\end{document}"<<endl;  
  outFile.close(); 
}

