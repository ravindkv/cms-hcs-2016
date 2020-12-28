source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh
export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
voms-proxy-init --voms cms
