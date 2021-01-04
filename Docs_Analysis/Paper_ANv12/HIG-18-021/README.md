HIG-18-021 area:
light charged Higgs to c sbar with 2016 data

```
scl enable rh-git29 bash # this allows you to access a recent version of git. It will place you in a bash shell.

git clone --recursive https://:@gitlab.cern.ch:8443/tdr/papers/HIG-18-021.git
cd HIG-18-021
./compile.sh

# to commit changes back...
git add .                           # add all files modified in current directory
git commit -m "add my new changes"  # to stage your changes
git push                            # to send them back to the repo

```
