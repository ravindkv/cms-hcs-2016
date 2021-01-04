t2wDataCard=$1
mass=$2
#combine $t2wDataCard -m $mass -M FitDiagnostics --expectSignal 1 --redefineSignalPOIs BR --setParameterRanges BR=0,0.10 --plots --saveShapes --saveWithUncertainties --saveNormalizations --cminDefaultMinimizerStrategy 0| tee FitDiagnostics.log
python diffNuisances.py -a fitDiagnostics.root --poi=BR -g fitDiag.pdf | tee diffNuisances.log

