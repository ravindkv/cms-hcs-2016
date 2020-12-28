
![CADI HIG-18-021](http://cms.cern.ch/iCMS/analysisadmin/cadilines?line=HIG-18-021)


These datacards reproduce the results in these documentation:
- [ ] AN-18-061
- [ ] HIG-18-021

### Clone these datacards ###  
git clone https://gitlab.cern.ch/cms-hcg/cadi/hig-18-021.git

### Commit the changes ###  
git add . 
git commit -m "add my new changes"
git push

### Convert txt to workspace using physics model  ###  

 * text2workspace.py datacard.txt P HiggsAnalysis.CombinedLimit.ChargedHiggs:brChargedHiggs  o text2workspace.root

### 95% limit computation  ###  
* combine -M Asymptotic --rAbsAcc 0.000001 text2workspace.root --mass 120 

### Run FitDiagnositics  ###  
./RunFitDiagnostics.sh text2workspace.root 100

### Run Impact  ###  
./RunImpactNP.sh text2workspace.root 100

### Get post-fit yields  ###  
python mlfitNormsToText.py fitDiagnostic.root -u

