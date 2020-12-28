# MultiCrab

 #### Set the CMSSSW release ####
 
 * cmsrel CMSSW_8_0_25
 * cd CMSSW_8_0_25/src/
 * cmsenv
 
 #### Download and compile MiniTree ####
 
 * git clone https://github.com/ravindkv/MiniTree.git
 * cd MiniTree
 * scram b -j20
 * cd ..
 
 #### Download and set MultiCrab ####
 
 * git clone https://github.com/ravindkv/MultiCrab.git
 * cd MultiCrab/test
 * source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh
 * voms-proxy-init -voms cms

 #### Run CRAB over single sample ####
 
 * crab submit -c CrabOneSample_cfg.py 
 
 #### Run CRAB over multiple samples ####
 
 * python CrabAllSamples_cfg.py
 
 #### Take a look at CRAB tutorial ####
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRABClientLibraryAPI#Example_submitting_multiple_task 
