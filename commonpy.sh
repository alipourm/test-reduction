#!/bin/bash
#$ -tc 50
#$ -t 1-50
#$ -e /nfs/eecs-fserv/share/alipour/processout/
#$ -o /nfs/eecs-fserv/share/alipour/processout/
#$ -l h=compute-0-1|compute-0-2|compute-0-3|compute-0-4|compute-0-5|compute-0-6|compute-0-7|compute-0-8|compute-0-9|compute-1-1|compute-1-10|compute-1-11|compute-1-12|compute-1-13|compute-1-2|compute-1-3|compute-1-4|compute-1-5|compute-1-6|compute-1-7|compute-1-8|compute-1-9|compute-2-1|compute-2-10|compute-2-11|compute-2-2|compute-2-3|compute-2-4|compute-2-6|compute-2-7|compute-2-8|compute-2-9|compute-3-1|compute-3-10|compute-3-11|compute-3-12|compute-3-2|compute-3-3|compute-3-4|compute-3-5|compute-3-6|compute-3-7|compute-3-8|compute-3-9|compute-4-1|compute-4-2|compute-4-3|compute-4-4|compute-5-1|compute-5-11|compute-5-2|compute-5-3|compute-5-4|compute-5-5|compute-5-6|compute-5-7|compute-5-8|compute-5-9|compute-6-25l|compute-6-26l|compute-6-26r|compute-7-10l|compute-7-10r|compute-7-12l|compute-7-12r|compute-7-13l|compute-7-13r|compute-7-14l|compute-7-15l|compute-7-15r|compute-7-1l|compute-7-1r|compute-7-2r|compute-7-3l|compute-7-3r|compute-7-4r|compute-7-5l|compute-7-5r|compute-7-6r|compute-7-7l|compute-7-7r|compute-7-8l|compute-7-8r|compute-7-9l|compute-7-9r|compute-8-11l|compute-8-11r|compute-8-12r|compute-8-13l|compute-8-13r|compute-8-14l|compute-8-14r|compute-8-15l|compute-8-15r|compute-8-1l|compute-8-2l|compute-8-3r|compute-8-4l|compute-8-4r|compute-8-5l|compute-8-5r|compute-8-6l|compute-8-6r|compute-8-7l|compute-8-7r|compute-8-8l|compute-8-8r|compute-8-9r|compute-9-3|compute-9-4|compute-a-1|compute-a-2|compute-b-1a|compute-b-1b|compute-b-1c|compute-b-1d|compute-b-2b|compute-b-2d|compute-c-1a|compute-c-1b|compute-c-1c|compute-c-1d|compute-c-2b|compute-c-2d|compute-gpu
TMP=$TMPDIR
source ~/.bashrc
ulimit -c 0
TC=TC$SGE_TASK_ID
DATA=/nfs/stak/students/a/alipourm/cluster-share/tcmin/pydata/$SUT
cd $TMP
cp -r nfs/stak/students/a/alipourm/test-reduction .
cd test-reduction
cp testcases/$SUT/$TC .
python non-adequate.py -sut $SUT -tc $TC -mutfile  /scratch/${SUT}muts.txt
yes | cp -f $TC* $DATA
rm -rf $TMP
