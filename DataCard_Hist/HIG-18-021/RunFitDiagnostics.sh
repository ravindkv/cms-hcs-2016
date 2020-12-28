t2wDataCard=$1
mass=$2
combine $t2wDataCard --mass $mass -M FitDiagnostics --plots --saveShapes --saveWithUncertainties  --saveNormalizations --initFromBonly --redefineSignalPOIs BR --setParameterRanges BR=0,0.1 

python diffNuisances.py --all fitDiagnostics.root  --poi=BR -g fitDiag.pdf 


