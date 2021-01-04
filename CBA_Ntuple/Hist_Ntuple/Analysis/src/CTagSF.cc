#include "interface/CTagSF.hh"

ClassImp(CTagSF)

double CTagSF::getIncCTagPmc(TH2D *h2_qTagEff_Num, TH2D *h2_qTagEff_Denom, const double & eta, const double & pt, const bool & isCTag){
  //double pMC = 1.0; 
  double pMC = 1.0; 
  if(isCTag) pMC = getCTagEff(h2_qTagEff_Num, h2_qTagEff_Denom, eta, pt);
  else pMC = 1 - getCTagEff(h2_qTagEff_Num, h2_qTagEff_Denom, eta, pt);
  return pMC;
}

double CTagSF::getIncCTagPdata(BTagCalibrationReader &reader, TH2D *h2_qTagEff_Num, TH2D *h2_qTagEff_Denom, const double & eta, const double & pt, const double & csv, const bool & isCTag, const int & jetFlavor, const int & cTagSys){
  double pData = 1.0; 
  double sf = 1.0;
  double eff = 1.0;
  if(isCTag){//tagged 
    sf = getCTagSF(reader, eta, pt, csv, jetFlavor, cTagSys);
    eff = getCTagEff(h2_qTagEff_Num, h2_qTagEff_Denom, eta, pt);
    pData = sf*eff;
  }
  else{// untagged
    sf = getCTagSF(reader, eta, pt, csv, jetFlavor, cTagSys);
    eff = getCTagEff(h2_qTagEff_Num, h2_qTagEff_Denom, eta, pt);
    pData = 1.0 - sf*eff;
  }
  return pData;
}

//https://twiki.cern.ch/twiki/bin/view/CMS/BTagCalibration#Additional_scripts
//https://twiki.cern.ch/twiki/pub/CMS/BtagRecommendation80XReReco/CSVv2_Moriond17_B_H.csv
double CTagSF::getCTagSF(BTagCalibrationReader &reader, const double & eta, const double & pt, const double & csv, const double & jetFlavor, const int & cTagSys){
  double sf=1.0;
  if(abs(jetFlavor) ==5){
    if(cTagSys==0) sf = reader.eval_auto_bounds("central", BTagEntry::FLAV_B, eta, pt,csv);
    if(cTagSys==1) sf = reader.eval_auto_bounds("up",      BTagEntry::FLAV_B, eta, pt, csv);
    if(cTagSys==-1)sf = reader.eval_auto_bounds("down",    BTagEntry::FLAV_B, eta, pt, csv);
  }
  else if(abs(jetFlavor)==4){
    if(cTagSys==0) sf = reader.eval_auto_bounds("central", BTagEntry::FLAV_C, eta, pt,csv);
    if(cTagSys==1) sf = reader.eval_auto_bounds("up",      BTagEntry::FLAV_C, eta, pt, csv);
    if(cTagSys==-1)sf = reader.eval_auto_bounds("down",    BTagEntry::FLAV_C, eta, pt, csv);
  }
  else{
    if(cTagSys==0) sf = reader.eval_auto_bounds("central", BTagEntry::FLAV_UDSG, eta, pt,csv);
    if(cTagSys==1) sf = reader.eval_auto_bounds("up",      BTagEntry::FLAV_UDSG, eta, pt, csv);
    if(cTagSys==-1)sf = reader.eval_auto_bounds("down",    BTagEntry::FLAV_UDSG, eta, pt, csv);
  }
  return sf;
}

//https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods
double CTagSF::getCTagEff(TH2D *h2_CTagEff_Num, TH2D *h2_CTagEff_Denom, const double & eta, const double & pt){
  double eff = 1.0;
  double bin_num = h2_CTagEff_Num->FindBin(pt, double(eta));
  double bin_denom = h2_CTagEff_Denom->FindBin(pt, double(eta));
  double num = h2_CTagEff_Num->GetBinContent(bin_num); 
  double denom = h2_CTagEff_Denom->GetBinContent(bin_denom); 
  eff = num/denom;
  return eff;  
}
