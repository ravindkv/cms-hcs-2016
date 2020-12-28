#include<TRandom3.h>

//--------------------------------------------
//function to make graph from two array
//--------------------------------------------
TGraph* makeGraph(vector<Double_t> Xarray, vector<Double_t> Yarray){
  Int_t n = Xarray.size();
  Double_t x[n], y[n];
   for (Int_t i=0;i<n;i++) {
     x[i] = Xarray[i];
     y[i] = Yarray[i] ;
   }
   TGraph* gr = new TGraph(n,x,y);
   return gr;
}

//--------------------------------------------
//function to decorate Graph
//--------------------------------------------
TGraph* decorateGraph(TGraph *graph, TString xTitle, TString yTitle, TString myTitle, double yMin, double yMax, int color){
  graph->SetTitle(myTitle);
  graph->GetYaxis()->SetTitleOffset(1.10);
  graph->GetXaxis()->SetTitle(xTitle);
  graph->GetXaxis()->SetTitleSize(0.04);
  graph->GetXaxis()->SetLabelSize(0.04);
  graph->GetYaxis()->SetTitle(yTitle);
  graph->GetYaxis()->SetTitleSize(0.04);
  graph->GetYaxis()->SetRangeUser(yMin, yMax);
  //graph->GetXaxis()->SetRangeUser(0, 10);
  graph->GetYaxis()->SetLabelSize(0.04);
  //graph->SetLineColor(color);
  //graph->SetLineWidth(3);
  graph->SetMarkerSize(20);
  graph->SetMarkerStyle(20);
  graph->SetMarkerSize(1);
  return graph;
}
TH1F* decorateHist(TH1F* hist, TString myTit, TString xTit, TString yTit, int color){
  hist->SetTitle(myTit);
  hist->SetTitleSize(0.1);
  hist->SetFillColor(color);
  hist->GetXaxis()->SetTitle(xTit);
  hist->GetYaxis()->SetTitle(yTit);
  hist->GetYaxis()->SetTitleOffset(1.10);
  hist->GetXaxis()->SetTitleOffset(0.90);
  hist->GetYaxis()->SetTitleSize(0.05);
  hist->GetXaxis()->SetTitleSize(0.05);
  hist->GetXaxis()->SetLabelSize(0.05);
  hist->GetYaxis()->SetLabelSize(0.05);
  hist->SetLineColor(color);
  hist->SetLineWidth(3);
  //hist->GetXaxis()->SetTickLength(0.05);
  //hist->GetXaxis()->SetNdivisions(5);
  //hist->SetMinimum(pMin);
  return hist;
}

void MyTopQuarkPtWeight(){
  gStyle->SetOptStat(0);
  /*
  Bottom left of Figure.3:
  https://link.springer.com/content/pdf/10.1007%2FJHEP02%282019%29149.pdf
  ----------------------------------------------------------------
  bin     pT range        binCenter       Ratio           1/Ratio
  	(GeV)           (GeV)           Th./Data
  ----------------------------------------------------------------
  1       0-65            32.5            0.92            1.0869
  2       65-125          95.0            1.02            0.9804
  3       125-200         162.5           1.046           0.9560
  4       200-290         245.0           1.15            0.8695
  5       290-400         345.0           1.231           0.8123
  6       400-550         475.0           1.276           0.7837
  //Parton level

  1       0-65            32.5            0.9048            1.105216
  2       65-125          95.0            1.0098            0.990295
  3       125-200         162.5           1.0430            0.958772
  4       200-290         245.0           1.1502            0.869414
  5       290-400         345.0           1.2430            0.804505
  6       400-550         475.0           1.2975            0.770713

  */
  vector<Double_t> pT;
  pT.push_back(32.5);
  pT.push_back(95.0);
  pT.push_back(162.5);
  pT.push_back(245.0);
  pT.push_back(345.0);
  pT.push_back(475.0);
  vector<Double_t> dataOverBkg;
  dataOverBkg.push_back(1.105216);
  dataOverBkg.push_back(0.990295);
  dataOverBkg.push_back(0.958772);
  dataOverBkg.push_back(0.869414);
  dataOverBkg.push_back(0.804505);
  dataOverBkg.push_back(0.770713);
  TGraph* gr = makeGraph(pT, dataOverBkg);
  decorateGraph(gr, "pT of particle level top quark [GeV]", "Data/Bkg ", "", 0.5, 1.5, kGreen);

  //TF1 *function = new TF1("fit", "exp([0] + [1]*x + [2]*x^2)", 0, 550);
  TF1 *function = new TF1("fit", "exp([0] +[1]*x)", 0, 5);
  TLegend* leg3 = new TLegend(0.50,0.70,0.60,0.85,NULL,"brNDC");
  leg3->SetBorderSize(0);
  leg3->SetTextSize(0.04);
  leg3->SetFillColor(0);
  gr->GetYaxis()->SetTitleOffset(1.30);
  gr->Fit(function, "", "", 0, 550);
  float m_1 = function->GetParameter(0);
  float c_1 = function->GetParameter(1);
  TCanvas *c1 = new TCanvas("c1","c1",200,10,700,500);
  c1->cd();
  gr->Draw("AP");
  function->Draw("SAME");
  leg3->AddEntry(gr, "Ratio (TOP-17-014)");
  leg3->AddEntry(function, "Fit = #splitline{exp(a + bx),}{#splitline{a = 0.09494, b = -0.00084,}{#chi^{2}/ndf = 0.000985}}");
  leg3->Draw("SAME");
  c1->SaveAs("topSF_3param.png");


  TFile * f = new TFile("all_TTJetsP.root");
  TH1F * hPtTop = (TH1F*)f->Get("TopPtPlus/Iso/ptTop");
  TH1F * hPtTopBar = (TH1F*)f->Get("TopPtPlus/Iso/ptTopBar");
  TH1F * hMassTop = (TH1F*)f->Get("TopPtPlus/Iso/massTop");
  TH1F * hMassTopBar = (TH1F*)f->Get("TopPtPlus/Iso/massTopBar");
  TCanvas *c2 = new TCanvas("c2","c2",200,10,700,500);
  c2->Divide(2,2);
  c2->cd(1);
  gPad->SetLogy(true);
  decorateHist(hPtTop, "Parton-level", "top quark pT [GeV]", "Events", kRed);
  hPtTop->Draw();

  c2->cd(2);
  gPad->SetLogy(true);
  decorateHist(hPtTopBar, "Parton-level", "top anti-quark pT [GeV]", "Events", kRed);
  hPtTopBar->Draw();

  c2->cd(3);
  gPad->SetLogy(true);
  decorateHist(hMassTop, "Parton-level", "top quark mass [GeV]", "Events", kBlue);
  //hMassTop->GetXaxis()->SetRangeUser(0, 400);
  hMassTop->Draw();

  c2->cd(4);
  gPad->SetLogy(true);
  decorateHist(hMassTopBar, "Parton-level", "top anti-quark mass [GeV]", "Events", kBlue);
  //hMassTopBar->GetXaxis()->SetRangeUser(0, 400);
  hMassTopBar->Draw();
  c2->SaveAs("partonLevelTop.pdf");


  //----------------------------------------------
  // Signal (LO MadGraph) vs bkg ttbar (NLO PowHeg)
  //----------------------------------------------
  TFile * fSig = new TFile("all_Hplus80.root");
  TH1F* hSigBase = (TH1F*)fSig->Get("base/Iso/ptTop");
  TH1F* hBkgBase = (TH1F*)f->Get("base/Iso/ptTop");
  TH1F* hBkgUp   = (TH1F*)f->Get("TopPtPlus/Iso/ptTop");
  hSigBase->Scale(1/hSigBase->Integral());
  hBkgBase->Scale(1/hBkgBase->Integral());
  hBkgUp->Scale(1/hBkgUp->Integral());
  decorateHist(hSigBase, "Parton-level", "top quark pT [GeV]", "Events (norm. to 1)", kRed);
  decorateHist(hBkgBase, "Parton-level", "top quark pT [GeV]", "Events (norm. to 1)", kGreen);
  decorateHist(hBkgUp, "Parton-level", "top quark pT [GeV]", "Events (norm. to 1)", kBlue);
  //overlay histograms
  TCanvas *c3 = new TCanvas();
  c3->Divide(2,2);
  c3->cd(1);
  hBkgBase->GetYaxis()->SetTitleOffset(1.07);
  hBkgBase->Draw();
  hSigBase->Draw("same");
  TLegend * leg1 = new TLegend(0.4, 0.4, 0.7, 0.8, NULL, "brNDC");
  leg1->AddEntry(hBkgBase, "#splitline{Nominal ttbar bkg}{(NLO PowHeg)}", "LP");
  leg1->AddEntry(hSigBase, "#splitline{Nominal signal}{(LO MadGraph)}", "LP");
  leg1->SetBorderSize(0);
  leg1->SetTextSize(0.05);
  leg1->SetFillColor(0);
  leg1->Draw("same");

  c3->cd(2);
  hBkgUp->Draw();
  hSigBase->Draw("same");
  TLegend * leg2 = new TLegend(0.4, 0.4, 0.7, 0.8, NULL, "brNDC");
  leg2->AddEntry(hBkgUp, "#splitline{Reweighted ttbar bkg}{(NLO PowHeg)}", "LP");
  leg2->AddEntry(hSigBase, "#splitline{Nominal signal}{(LO MadGraph)}", "LP");
  leg2->SetBorderSize(0);
  leg2->SetTextSize(0.05);
  leg2->SetFillColor(0);
  leg2->Draw("same");

  //ratio
  TF1 *baseLine = new TF1("baseLine","1", -100, 2000);
  baseLine->SetLineColor(kBlack);
  c3->cd(3);
  TH1F* hRatioBase = (TH1F*)hBkgBase->Clone("hRatioBase");
  hRatioBase->Divide(hSigBase);
  decorateHist(hRatioBase, "", "top quark pT [GeV]", "Ratio (Nomimal ttbar / Nominal signal)", kGreen);
  hRatioBase->GetYaxis()->SetRangeUser(0.5, 1.5);
  hRatioBase->GetYaxis()->SetTitleOffset(1.0);
  hRatioBase->Draw();
  baseLine->Draw("same");

  c3->cd(4);
  TH1F* hRatioUp = (TH1F*)hBkgUp->Clone("hRatioUp");
  hRatioUp->Divide(hSigBase);
  decorateHist(hRatioUp, "", "top quark pT [GeV]", "Ratio (Reweighted ttbar / Nominal signal)", kBlue);
  hRatioUp->GetYaxis()->SetRangeUser(0.5, 1.5);
  hRatioUp->Draw();
  baseLine->Draw("same");
  c3->SaveAs("signalMadGraph_vs_ttbarPowheg.pdf");
}
