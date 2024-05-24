#!/bin/bash

# check if user wants to compile and run checker on modest.model
echo 'Compile model.modest and run checker?(approx 10-15 mins)'
read -p "$*[y/N]" yn
case $yn in
  [Yy]*) modest mopy model.modest -Y -O model.py && python3 checker.py model.py;; # if yes run it
  *) echo 'skipping...' ;; # else skip it
esac

# 1) create jobs_picked.png and charge.png 
# 2) replace previous modest arrays with new. This is done by removing the first 16 lines of schedule.modest
#     which is the arrays of the scheduled jobs. Then concatinate the output of schedule.py to add the new ones
#     finaly move the file back to schedule.modest
# 3) run modest modes with correct parameters and store trace to schedule.csv
# 4) call graph.py to create 
python3 schedule.py > schedule.modest.bak \
  && tail -n +16 schedule.modest >> schedule.modest.bak && mv schedule.modest.bak schedule.modest \
  && modest modes -M NonlinearSHA --int DormandPrince54 infinity=54000 --int-events BracketingNthOrderBrent --trace-delays -T ContinuousCoordinates -N 1  schedule.modest -Y -TF schedule.csv\
  && python3 graph.py 
