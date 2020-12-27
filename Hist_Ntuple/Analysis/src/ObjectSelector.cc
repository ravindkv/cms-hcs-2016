#include "interface/ObjectSelector.hh"
#include <iostream>
#include <iomanip>

ClassImp(ObjectSelector)

using namespace std;

//https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
//Electron ID: veto
bool ObjectSelector::cutBasedElectronID_Summer16_80X_V1_veto(const MyElectron *e)
{
  bool passID = false;
  //barrel
  if(abs(e->eleSCEta) <= 1.479 
     && e->sigmaIetaIeta 	< 0.0115	 
     && abs(e->dEtaInSeed) 	< 0.00749	
     && abs(e->dPhiIn) 		< 0.228	
     && e->hadOverEm 		< 0.356	
     && e->relCombPFIsoEA 	< 0.175	
     && abs(e->iEminusiP) 	< 0.299	
     && e->nInnerHits       	<= 2
     && e->passConversionVeto  
    )passID = true;
  //endcap 
  if(abs(e->eleSCEta) > 1.479 
     && e->sigmaIetaIeta 	< 0.037	
     && abs(e->dEtaInSeed) 	< 0.00895	 
     && abs(e->dPhiIn) 		< 0.213	
     && e->hadOverEm 		< 0.211	
     && e->relCombPFIsoEA 	< 0.159	
     && abs(e->iEminusiP) 	< 0.15	
     && e->nInnerHits       	<= 3
     && e->passConversionVeto  
     )passID = true;
  return passID;
}

//Electron ID: medium
bool ObjectSelector::cutBasedElectronID_Summer16_80X_V1_medium(const MyElectron *e, MyVertex & vertex)
{
  bool passID = false;
  //barrel
  double dxy = abs(e->D0);
  double dz  = abs(e->Dz);
  if(abs(e->eleSCEta) <= 1.479 
     && e->sigmaIetaIeta 	< 0.00998	 
     && abs(e->dEtaInSeed) 	< 0.00311	
     && abs(e->dPhiIn) 		< 0.103	
     && e->hadOverEm 		< 0.253	
     ///&& e->relCombPFIsoEA 	< 0.0695	
     && abs(e->iEminusiP) 	< 0.134
     && dxy                 < 0.05
     && dz                  < 0.10    
     && e->nInnerHits       <= 1
     && e->passConversionVeto  
    )passID = true;
  //endcap
  if(abs(e->eleSCEta) > 1.479 
     && e->sigmaIetaIeta 	< 0.0298	
     && abs(e->dEtaInSeed) 	< 0.00609	 
     && abs(e->dPhiIn) 		< 0.045	
     && e->hadOverEm 		< 0.0878	
     ///&& e->relCombPFIsoEA 	< 0.0821	
     && abs(e->iEminusiP) 	< 0.13	
     && dxy                 < 0.10
     && dz                  < 0.20    
     && e->nInnerHits       <= 1
     && e->passConversionVeto  
     )passID = true;
  return passID;
}

void ObjectSelector::preSelectElectrons(vector<int> * e_i, const vector<MyElectron> & vE , MyVertex & vertex, const bool & isPFlow){
  //https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2#Offline_selection_criteria
  for(unsigned int i=0;i<vE.size();i++){
    const MyElectron * e    = &vE[i];
    double ePt     	        = TMath::Abs(e->p4.pt());
    double eEta     	    = TMath::Abs(e->p4.eta());
    bool passID = cutBasedElectronID_Summer16_80X_V1_medium(e, vertex);
    if(passID && ePt >30.0 && eEta <2.5){e_i->push_back(i);}
  }
}

//https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2
bool ObjectSelector::isMediumMuon(const MyMuon * m){
  bool isMedium(false);
  bool goodGlob = m->isGlobalMuon && 
      m->normChi2 <3 && 
      m->chi2LocalPosition < 12 && 
      m->trkKink < 20; 
  bool isLooseMuon = m->isPFMuon && (m->isGlobalMuon || m->isTrackerMuon);
  isMedium =  isLooseMuon &&  
        m->validFraction > 0.8 && 
        m->segmentCompatibility >(goodGlob ? 0.303 : 0.451); 
  return isMedium; 
}

bool ObjectSelector::isTightMuon(const MyMuon * m){
  bool isTight(false);
  isTight = 
      m->isGlobalMuon && 
      m->isPFMuon &&
      m->normChi2 <10 &&
      m->nMuonHits > 0 &&
      m->nMatchedStations >1 &&
      m->nPixelHits >0 && 
      m->nTrackerLayers >5;
  return isTight; 
}

void ObjectSelector::preSelectMuons(TString url, vector<int> * m_i, const vector<MyMuon> & vM , MyVertex & vertex, const bool & isData, const double & random_u1, const double & random_u2, const int & err_member, const int & err_set){
  for( int i=0;i< (int) vM.size();i++){
    const MyMuon * m = &vM[i];
    double mEta     = TMath::Abs(m->p4.eta());
    ///double mPt      = TMath::Abs(m->p4.pt());
    double mPt   = muPtWithRochCorr(m, isData, random_u1, random_u2, err_set, err_member); 
    double dxy = abs(m->D0);
    double dz = abs(m->Dz);
    bool passID = false;
    passID = isMediumMuon(m);
    if(passID && mPt > 26.0 && mEta < 2.4 && dxy < 0.05 && dz <0.2){
      m_i->push_back(i);
    }
  }
}

void ObjectSelector::preSelectJets( string jetAlgo, vector<int> * j_i, const vector<MyJet> & vJ){
  //https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2016
  for(unsigned int i=0;i<vJ.size();i++){
    const MyJet *jet= &vJ[i];
    double jetEta   = TMath::Abs(jet->p4.eta());
    double jetPt    = TMath::Abs(jet->p4.pt());
    double NHF      = jet->neutralHadronEnergyFraction;
    double NEMF     = jet->neutralEmEnergyFraction;
    double CHF      = jet->chargedHadronEnergyFraction;
    double CEMF     = jet->chargedEmEnergyFraction;
    double NumConst = jet->NumConst;
    double CHM      = jet->chargedMultiplicity;
    double looseJetID = (NHF<0.99 && NEMF<0.99 && NumConst>1) && (abs(jetEta)<=2.4 && CHF>0 && CHM>0 && CEMF<0.99);
    if(looseJetID && jetPt > 25.0) j_i->push_back(i);
  }
}

bool ObjectSelector::looseMuonVeto( const int & selectedMuon, const vector<MyMuon> & vM, const bool & isPFlow){
  bool looseVeto(false);
  for(int i=0;i< (int)vM.size();i++){
    if( i==selectedMuon ){continue;}
    const MyMuon * m = &vM[i];
    bool isGlobalMuon = m->isGlobalMuon;
    double mEta     = TMath::Abs(m->p4.eta());
    double mPt      = TMath::Abs(m->p4.pt());
    double mRelIso  = m->pfRelIso;
    if(! isGlobalMuon) continue;
    if(mEta<2.4  && mPt> 15.0 && mRelIso < 0.25){ looseVeto = true; }
  }
  return looseVeto;
}

bool ObjectSelector::looseElectronVeto(unsigned long selectedElectron, const vector<MyElectron> & vE, MyVertex & vertex, const bool & isPFlow){
  //https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2#Offline_selection_criteria
  bool looseVeto(false);
  for(unsigned long i=0;i<vE.size();i++){
    const MyElectron * e   = &vE[i];
    double ePt     	   = TMath::Abs(e->p4.pt());
    if( i==selectedElectron) continue; 
    bool passID = cutBasedElectronID_Summer16_80X_V1_veto(e);
    double dxy = abs(e->D0);
    double dz  = abs(e->Dz);
    if(passID && ePt >15.0 && dxy<0.05 && dz < 0.1){looseVeto = true;}
  }
  return looseVeto;
}

void ObjectSelector::ElectronCleaning( const vector<MyElectron> & vE, const vector<MyMuon> & vM, vector<int> * e_old, vector<int> * e_new, vector<int> * mu, const double & DR ){
  for(size_t i = 0; i < e_old->size(); i++){
    int iele = (*e_old)[i];
    double delR2Mu = 5.0;
    for(size_t j = 0; j < mu->size(); j++){
      int imu = (*mu)[j];
      double delR = DeltaR(vE[iele].p4, vM[imu].p4);
      if(delR < delR2Mu)delR2Mu = delR;
    }
    if(delR2Mu > DR) e_new->push_back(iele);
  }
}

void ObjectSelector::JetCleaning(const vector<MyJet> & vJ, const vector<MyMuon> & vM, const vector<MyElectron> & vE,vector<int> * j_old, vector<int> * j_new, vector<int> * mu, vector<int> * el, const double & DR){
  for(size_t i = 0; i < j_old->size(); i++){
    int ijet = (*j_old)[i];
    double delR2Mu = 5.0, delR2Ele = 5.0;
    for(size_t j = 0; j < mu->size(); j++){
      int imu = (*mu)[j];
      double delR = DeltaR(vJ[ijet].p4, vM[imu].p4);
      if(delR < delR2Mu)delR2Mu = delR;
    }
    for(size_t k = 0; k < el->size(); k++){
      int iele = (*el)[k];
      double delR = DeltaR(vJ[ijet].p4, vE[iele].p4);
      if(delR < delR2Ele)delR2Ele = delR;
    }
    if(delR2Mu > DR && delR2Ele > DR )
    {
        j_new->push_back(ijet);
    }
    }
}

double ObjectSelector::DeltaR(const MyLorentzVector & aV, const MyLorentzVector & bV){
  double deta = TMath::Abs(aV.eta() - bV.eta());
  double dphi = TMath::Abs(aV.phi() - bV.phi());
  if(dphi > M_PI) dphi = 2*M_PI - dphi;
  double delR = sqrt(deta*deta + dphi*dphi);
  return delR;
}

