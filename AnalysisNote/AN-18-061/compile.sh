mkdir -p $PWD/output
export TDR_TMP_DIR=$PWD/output
eval `utils/tdr runtime -sh`
tdr --style=an b AN-18-061
