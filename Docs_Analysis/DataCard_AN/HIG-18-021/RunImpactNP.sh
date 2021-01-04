t2wDataCard=$1
mass=$2
combineTool.py -M Impacts -d $t2wDataCard -m $mass -t -1 --doInitialFit --robustFit 1  --redefineSignalPOIs BR --setParameterRanges BR=0.0,0.1 | tee doInitialFit.log 
combineTool.py -M Impacts -d $t2wDataCard -m $mass -t -1 --doFit --robustFit 1  --redefineSignalPOIs BR --setParameterRanges BR=0.0,0.1 --parallel 20 | tee doFit.log
combineTool.py -M Impacts -d $t2wDataCard -m $mass -o nuisImpactJSON 
python plotImpacts.py --cms-label "   Internal" -i nuisImpactJSON -o nuisImpactPDF


