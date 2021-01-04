#include "MyStackHisto.h"

///////////////////////////////////////////
bool isForPaper = true;
int iPeriod = 4;
int iPosX = 10;

bool isDDqcd = true;
TFile *f_QCD_dd = new TFile("all_QCD_dd.root","RECREATE");

///////////////////////////////////////////
void plotStackedHisto(TString baseDir, TString isoDir, TString histDir, TString histName, TString xTitle,bool isData=false, bool isSig=false, double xmin=0, double xmax=10, double unc=false){
  MyStackHisto MyS;
  //MyS.setTDRStyle();
  MyS.setTDRStyle();
  string hist_name (histName);
  TCanvas *c1 = MyS.myCanvas(histName, iPeriod, 1, isData);
  const float xpad[2] = {0.,1.0};
  const float ypad[4] = {0.,0.30,1.0};
  if(isData){
    c1->Divide(1, 2); c1->cd(1);
    gPad->SetRightMargin(0.03);
    gPad->SetPad(xpad[0],ypad[1],xpad[1],ypad[2]);
    if(isData) gPad->SetLogy(true);
    //if(hist_name.find("mjj") != string::npos) gPad->SetLogy(false);
  }
  else c1->cd();

  //-------------------------------
  // stack MC Bkg histo
  //-------------------------------
  THStack* hStack = new THStack("hStack","");
  TH1F* hVV = MyS.getHisto(fVV, baseDir, isoDir, histDir, histName);
  TH1F* hMC = (TH1F*)hVV->Clone("hMC");
  int col_depth =1;
  if(baseDir=="baseLowMET/") col_depth = 0;
  hVV->SetFillColor(kGreen + col_depth);
  hStack->Add(hVV);
  TH1F* hDY = MyS.stackHisto(fDY, baseDir, isoDir, histDir, histName, kOrange+col_depth, 1,   hStack, hMC);
  TH1F* hWJ = MyS.stackHisto(fWJ, baseDir, isoDir, histDir, histName, kYellow +col_depth , 1,   hStack, hMC);

  // trim the histDir string
  std::string histDir_str;
  std::string histDir_orig(histDir);
  std::remove_copy(histDir_orig.begin(), histDir_orig.end(), std::back_inserter(histDir_str), '/');
  TString histDir_(histDir_str);

  //-------------------------------
  // QCD from Data
  //-------------------------------
  //qcd scale factors for data-driven QCD
  double qcdSF = 1.0;
  double qcdErr = 0.0;
  if(isDDqcd){
    vector<double> sfAndErr = MyS.getQcdSF(fData, fTT, fST, fWJ, fDY, fVV, histDir, histName, xTitle, xmin, xmax);
    qcdSF = sfAndErr[0];
    qcdErr = sfAndErr[1];
  }
  if(histDir==""||baseDir=="baseLowMET/") isDDqcd = false;
  TH1F * hQCD_dd = MyS.getHisto(fQCD, baseDir, isoDir, histDir, histName);
  hQCD_dd->Reset(); // initialize empty hist
  if(isDDqcd){
    hQCD_dd = MyS.getDDqcd(baseDir, "NonIso/", histDir, histName,  qcdSF,  qcdErr);
    hQCD_dd->SetFillColor(kBlue+col_depth);
    hQCD_dd->GetXaxis()->SetRangeUser(xmin,xmax);
    //create same dir to the data driven qcd file
    std::string histPath = std::string(baseDir+isoDir+histDir_);
    TDirectory *d = f_QCD_dd->GetDirectory(histPath.c_str());
    if(!d) f_QCD_dd->mkdir(histPath.c_str());
    f_QCD_dd->cd(histPath.c_str());
    //hQCD->Draw();
    hQCD_dd->Write();
    hStack->Add(hQCD_dd);
    hMC->Add(hQCD_dd);
  }
  else hQCD_dd = MyS.stackHisto(fQCD, baseDir, isoDir, histDir, histName, kBlue +col_depth, 1,   hStack, hMC);
  TH1F * hST = MyS.stackHisto(fST, baseDir, isoDir, histDir, histName, kViolet +col_depth , 1,   hStack, hMC);
  TH1F* hTT = MyS.stackHisto(fTT, baseDir, isoDir, histDir, histName, kCyan+col_depth, 1,   hStack, hMC);

  if(isData){
    gPad->SetTopMargin(0.09);
    gPad->SetBottomMargin(0.0);
  }
  hStack->Draw("HIST");
  hStack->SetMinimum(1.0);
  hStack ->GetXaxis()->SetRangeUser(xmin, xmax);
  if(histName.Contains("mjj")){
    TGaxis::SetMaxDigits(3);
    hStack->GetYaxis()->SetTitle("Events / 5 GeV");
  }
  else hStack->GetYaxis()->SetTitle("Events / bin");
  hStack->GetXaxis()->SetTitle(xTitle);
  if(isData){
    //hStack->GetHistogram()->GetXaxis()->SetTickLength(0);
    hStack->GetHistogram()->GetXaxis()->SetLabelOffset(999);
    hStack->GetXaxis()->SetTitleSize(0);
  }

  //-------------------------------------///
  //unc band
  //-------------------------------------///
  TGraphAsymmErrors *UncBand;
  if(unc){
  UncBand = MyS.UNCGRAPH(
            MyS.addHistoForUnc("base/", 	 isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("JESPlus/",      isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("JESMinus/",     isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("JERPlus/",      isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("JERMinus/",     isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("bcTagPlus1/",     isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("bcTagMinus1/",    isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("bcTagPlus2/",     isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("bcTagMinus2/",    isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("bcTagPlus3/",     isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("bcTagMinus3/",    isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("PileupPlus/",   isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("PileupMinus/",  isoDir, histDir, histName, 	isDDqcd),
      	    MyS.addHistoForUnc("TopPtPlus/",   isoDir, histDir, histName,     isDDqcd),
      	    MyS.addHistoForUnc("TopPtMinus/",  isoDir, histDir, histName, 	isDDqcd),
	    hQCD_dd, true, false, isDDqcd);
  //UncBand->SetFillColor(17);
  UncBand->SetFillColor(kSpring +9);
  UncBand->SetFillStyle(3008);
  UncBand->Draw(" E2 same");
  c1->Update();
  }

  //-------------------------------
  //Data
  //-------------------------------
  TH1F* hData = MyS.getHisto(fData, baseDir, isoDir, histDir, histName);;
  ///MyS.decorateHisto(hData, "", xTitle, "Events");
  hData->SetFillColor(kBlack);
  hData->SetMarkerStyle(20); 
  hData->SetMarkerSize(1.2);
    c1->Update();
  if(isData)hData->Draw("Esame");

  //-------------------------------
  //Signal
  //-------------------------------
  TH1F* hSig = MyS.getHisto(fSig, baseDir, isoDir, histDir, histName);
  hSig->SetLineColor(kRed); hSig->SetLineStyle(2);
  hSig->SetLineWidth(3); hSig->SetFillColor(0);
    c1->Update();
  if(isSig)hSig->Draw("HISTSAME");
  double yMax = 0;
  if(hData->GetMaximum() > hSig->GetMaximum()) yMax = hData->GetMaximum();
  else yMax = hSig->GetMaximum();
  if(yMax < hMC->GetMaximum()) yMax = hMC->GetMaximum();
  hStack->SetMaximum(1000*yMax);

  //-------------------------------------///
  //  Draw Pave Text
  //-------------------------------------///
  //channel
  TPaveText *ch = MyS.paveText(0.20,0.65,0.30,0.75, 0, 19, 1, 0, 132);
  TString dirName = histDir_;
  if(baseDir=="baseLowMET/"){
    dirName = "#splitline{"+histDir_+"}{E_{T}^{miss} < 20 GeV}";
    gPad->SetTickx(0);
  }
  if(isForPaper && histDir=="BTag/") dirName = "BTag";
  if(isForPaper && histDir=="KinFit/") dirName = "After KF";
  ch->SetTextSize(0.05);
  ch->SetBorderSize(0);
  ch->SetFillStyle(0);
  TString charmCat = "";
  if(histName.Contains("ExL") || histName.Contains("ExM") || histName.Contains("ExT")){
    //ch = MyS.paveText(0.20,0.60,0.35,0.70, 0, 19, 1, 0, 132);
    ch->SetTextSize(0.05);
    if(histName.Contains("ExL")) charmCat = "Loose";
    if(histName.Contains("ExM")) charmCat = "Medium";
    if(histName.Contains("ExT")) charmCat = "Tight";
  }
  if(isEleChannel) ch->AddText("#splitline{#splitline{e + jets}{"+dirName+"}}{"+charmCat+"}");
  if(isMuChannel) ch->AddText("#splitline{#splitline{#mu + jets}{"+dirName+"}}{"+charmCat+"}");
      
  //hLable->Draw();
  c1->Update();

  //-------------------------------
  //Legends
  //-------------------------------
  TLegend* leg = new TLegend(0.3518792,0.65,0.9012081,0.88861,NULL,"brNDC");
  if(unc){leg->SetNColumns(3);}
  else{leg->SetNColumns(2);}
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);
  leg->SetFillColor(kBlack);
  leg->SetTextFont(42);
  leg->SetTextAngle(0);
  leg->SetTextSize(0.04);
  leg->SetTextAlign(12);
  //leg->AddEntry(hSig, "#splitline{Signal}{M_{H^{+}} = 120 GeV}","L");
  if(isData)leg->AddEntry(hData,"Data","PE");
  leg->AddEntry(hTT,"t#bar{t}","F");
  leg->AddEntry(hST,"Single t","F");
  leg->AddEntry(hQCD_dd,"QCD","F");
  leg->AddEntry(hWJ,"W + jets","F");
  leg->AddEntry(hDY,"Z/#gamma + jets","F");
  leg->AddEntry(hVV,"VV","F");
  //if(isSig)leg->AddEntry(hSig, "Signal","L");
  if(unc)leg->AddEntry(UncBand, "Pre-fit unc.(Bkg. stat. #oplus sys.)","F");
  if(isSig)leg->AddEntry((TObject*)0, "","");
  if(isSig)leg->AddEntry(hSig, "m_{H^{+}} = 100 GeV, B(t#rightarrow H^{+}b) = 0.13","L");
  c1->Update();
  c1->RedrawAxis();
  leg->Draw();
  ch->Draw();
  gPad->RedrawAxis();

  //-------------------------------------///
  // Ratio = DATA/Bkg
  //-------------------------------------///
  if(isData){
    c1->cd(2);
    c1->Update();
    c1->RedrawAxis();
    c1->GetFrame()->Draw();
    gPad->SetTopMargin(0); 
    gPad->SetBottomMargin(0.30); //gPad->SetGridy();
    gPad->SetRightMargin(0.03);
    gPad->SetTickx(0);
    //if(histDir=="") gPad->SetBottomMargin(0.55);
    gPad->SetPad(xpad[0],ypad[0],xpad[1],ypad[1]);
    TH1F *hRatio = (TH1F*)hData->Clone("hRatio");
    hRatio->Reset();
    hRatio->Add(hData);
    hRatio->Divide(hMC);
    hRatio->SetFillColor(kBlack);
    hRatio->GetYaxis()->SetRangeUser(0.1, 1.9);
    //hRatio->GetXaxis()->SetNdivisions(6,5,0);
    hRatio->GetXaxis()->SetTitleSize(0.13);
    hRatio->GetXaxis()->SetLabelSize(0.11);
    hRatio->GetXaxis()->SetLabelFont(42);
    hRatio->GetXaxis()->SetLabelColor(kBlack);
    hRatio->GetXaxis()->SetAxisColor(kBlack);
    hRatio->GetXaxis()->SetTickLength(0.06);
    hRatio->GetXaxis()->SetRangeUser(xmin, xmax);
    hRatio->GetXaxis()->SetTitleOffset(1);
    hRatio->GetXaxis()->SetLabelOffset(0.01);
    hRatio->SetMarkerStyle(20); 
    hRatio->SetMarkerSize(1.2);
    hRatio->GetYaxis()->SetTitleSize(0.13);
    hRatio->GetYaxis()->SetLabelSize(0.11);
    hRatio->GetYaxis()->SetLabelFont(42);
    hRatio->GetYaxis()->SetAxisColor(1);
    hRatio->GetYaxis()->SetTickLength(0.03);
    hRatio->GetYaxis()->SetNdivisions(6,5,0);
    hRatio->GetYaxis()->SetTitleOffset(0.5);
    hRatio->GetYaxis()->SetLabelOffset(0.01);
    hRatio->GetYaxis()->CenterTitle();
    /*
    if(hist_name.find("mjj") != string::npos){
      hRatio->GetXaxis()->SetTitleSize(0.15);
      hRatio->GetXaxis()->SetTitleOffset(1.40);
    }
    */
    hRatio->GetXaxis()->SetTitle(xTitle);
    //hRatio->GetYaxis()->SetNdivisions(6,5,0);
    //hRatio->GetYaxis()->SetTitleOffset(1);
    hRatio->GetYaxis()->SetTitle("#frac{Data}{Bkg}");
    
    //lable x-axis, for cutflow
    if(histName=="cutflow"){
      vector<string >cut_label;
      if(isEleChannel){
        cut_label.push_back("Ele trigger");
        cut_label.push_back("No. of ele = 1");
      }
      if(isMuChannel){
        cut_label.push_back("Mu trigger");
        cut_label.push_back("No. of mu = 1");
      }
      cut_label.push_back("No. of jets #geq 4");
      cut_label.push_back("MET #geq 20 GeV");
      cut_label.push_back("No. of b-jets #geq 2");
      cut_label.push_back("KinFit Sel");
      cut_label.push_back("No. of c-jet #geq 1");
      for(int istep=0; istep<cut_label.size(); istep++ ){
       hRatio->GetXaxis()->SetBinLabel(istep+1, cut_label[istep].c_str());
      }
      hRatio->GetXaxis()->LabelsOption("u");
      hRatio->GetXaxis()->SetTickLength(0.08);
      hRatio->GetXaxis()->SetLabelOffset(0.02);
      hRatio->GetYaxis()->SetRangeUser(0.8, 1.2);
    }
    //unc band
    c1->Update();
    hRatio->Draw("E"); // use "P" or "AP"
    if(unc){
    TGraphAsymmErrors *UncBand_Ratio;
    UncBand_Ratio = MyS.UNCGRAPH(
	    MyS.addHistoForUnc("base/", 	 isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("JESPlus/",     isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("JESMinus/",    isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("JERPlus/",     isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("JERMinus/",    isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("bcTagPlus1/",  isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("bcTagMinus1/", isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("bcTagPlus2/",  isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("bcTagMinus2/", isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("bcTagPlus3/",  isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("bcTagMinus3/", isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("PileupPlus/",  isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("PileupMinus/", isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("TopPtPlus/",  isoDir, histDir, histName,  isDDqcd),
      	    MyS.addHistoForUnc("TopPtMinus/", isoDir, histDir, histName,  isDDqcd),
	    hQCD_dd, false, true, isDDqcd);
    //UncBand_Ratio->SetFillColor(17);
    UncBand_Ratio->SetFillColor(kSpring +9);
    //UncBand_Ratio->SetFillStyle(3008);
    UncBand_Ratio->Draw(" E2 same ");
    }
    c1->Update();
    hRatio->Draw("E same"); // use "P" or "AP"
    //base line at 1
    TF1 *baseLine = new TF1("baseLine","1", -100, 2000);
    baseLine->SetLineColor(kBlack);
    c1->Update();
    baseLine->Draw("SAME");
    c1->Update();
    gPad->RedrawAxis();
  }
  MyS.CMS_lumi(c1, iPeriod, iPosX);
    c1->Update();
  if(isSaveHisto){
    mkdir(histDir_, S_IRWXU);
    TString outFile("$PWD/");
    outFile += histDir_+"/"+histName;
    if(isMuChannel) outFile += "_mu"+histDir_+".pdf";
    if(isEleChannel) outFile += "_ele"+histDir_+".pdf";
    c1->SaveAs(outFile);
    //c1->Close();
  }
}

void MyStackHisto(){
  TString histDir="BTag/"; // BTag/, KinFit/
  TString baseDir = "base/"; // base/, baseLowMET/

  TString isoDir = "Iso/";
  bool isDataOnMjj=true;
  //flags
  bool isData = true;
  bool isSig = true;
  bool isUnc = true;
  bool isMCqcd = false;
  if(isMuChannel && isMCqcd){
   plotStackedHisto(baseDir, "", "", "RelIso_1Mu","I_{rel}^{#mu}", isData,  isSig,  0.0, 1.0,  false);
   plotStackedHisto(baseDir, "", "", "pt_met_1Mu","E_{T}^{miss} (GeV)", isData,  isSig,  0.0, 500.0, false);
  }
  if(isEleChannel && isMCqcd){
   plotStackedHisto(baseDir, "", "", "RelIso_1Ele","I_{rel}^{e}", isData,  isSig,  0.0, 1.0,  false);
   plotStackedHisto(baseDir, "", "", "pt_met_1Ele","E_{T}^{miss} (GeV)", isData,  isSig,  0.0, 500.0, false);
  }
  if(isMCqcd) plotStackedHisto(baseDir, isoDir, "", "cutflow","Cutflow", isData,  isSig,  0.0, 15.0, false);

 if(histDir=="BTag/"){
   plotStackedHisto(baseDir, isoDir, histDir, "mjj", "m_{jj} (GeV)", isDataOnMjj, isSig,  0, 400, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "pfCISV", "CSVv2", isData, isSig,  -0.1, 1.1, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "chi2OfKinFit", "#chi^{2} of KF", isData, isSig,  0, 100, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "probOfKinFit", "prob of KF", isData, isSig,  0, 1, isUnc);
 }
 if(histDir=="KinFit/"){
   plotStackedHisto(baseDir, isoDir, histDir, "mjj_kfit", "m_{jj} (GeV)", isDataOnMjj, isSig,  5, 170, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "mjj_kfit_CTagIncL", "m_{jj} (GeV)", isDataOnMjj, isSig,  5, 170, isUnc);
   //plotStackedHisto(baseDir, isoDir, histDir, "mjj_kfit_CTagIncM", "m_{jj} (GeV)", isDataOnMjj, isSig,  5, 170, isUnc);
   //plotStackedHisto(baseDir, isoDir, histDir, "mjj_kfit_CTagIncT", "m_{jj} (GeV)", isDataOnMjj, isSig,  5, 170, isUnc);
   //plotStackedHisto(baseDir, isoDir, histDir, "mjj_kfit_CTagExO", "m_{jj} (GeV)", isDataOnMjj, isSig,  5, 170, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "mjj_kfit_CTagExL", "m_{jj} (GeV)", isDataOnMjj, isSig,  5, 170, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "mjj_kfit_CTagExM", "m_{jj} (GeV)", isDataOnMjj, isSig,  5, 170, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "mjj_kfit_CTagExT", "m_{jj} (GeV)", isDataOnMjj, isSig,  5, 170, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "pfCCvsL", "CvsL (CSVv2)", isData, isSig,  -1.1, 1.1, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "pfCCvsB", "CvsB (CSVv2)", isData, isSig,  -1.1, 1.1, isUnc);
   //plotStackedHisto(baseDir, isoDir, "nonKinFit/", "mjj_non_kfit", "m_{jj}(GeV)", isDataOnMjj, isSig,  0, 250, isUnc);
 }
 if(histDir=="BTag/" ||histDir=="KinFit/"){
   plotStackedHisto(baseDir, isoDir, histDir, "eta_jet", "#eta^{jets}", isData, isSig,  -3.0, 3.0, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "pt_jet", "p_{T}^{jets} (GeV)", isData, isSig,  0.0, 700.0, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "nvtx", "N^{vertex}", isData, isSig,  0, 70, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "rhoAll", "#rho", isData, isSig,  0, 70, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "final_multi_jet", "N^{jets} ", isData, isSig,  3, 15, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "CSVL_count", "N^{b jets}", isData, isSig,  1, 10, isUnc);
   if(baseDir=="baseLowMET/")plotStackedHisto(baseDir, isoDir, histDir, "final_pt_met", "E_{T}^{miss} (GeV)", isData, isSig,  0.0, 40.0, isUnc);
   else plotStackedHisto(baseDir, isoDir, histDir, "final_pt_met", "E_{T}^{miss} (GeV)", isData, isSig,  0.0, 500.0, isUnc);
   plotStackedHisto(baseDir, isoDir, histDir, "wmt", "m_{W^{+}}^{T} (GeV)", isData, isSig,  0.0, 500.0, isUnc);
   if(isMuChannel){
    plotStackedHisto(baseDir, isoDir, histDir, "pt_mu", "p_{T}^{#mu} (GeV)", isData, isSig,  0.0, 500.0, isUnc);
    plotStackedHisto(baseDir, isoDir, histDir, "eta_mu", "#eta^{#mu}", isData, isSig,  -3.0, 3.0, isUnc);
   }
   if(isEleChannel){
     plotStackedHisto(baseDir, isoDir, histDir, "pt_ele", "p_{T}^{e} (GeV)", isData, isSig,  0.0, 500.0, isUnc);
     plotStackedHisto(baseDir, isoDir, histDir, "eta_ele", "#eta^{e}", isData, isSig,  -3.0, 3.0, isUnc);
   }
  }
}
