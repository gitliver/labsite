#!/bin/bash

# path where this script resides
scripts=$( dirname $( readlink -m $0 ) )

# variables to enable SGE qsub
export DRMAA_LIBRARY_PATH=/opt/gridengine/lib/lx24-amd64/libdrmaa.so
export SGE_CELL=default
export SGE_ROOT=/opt/gridengine/hpc
export SGE_CLUSTER_NAME=hpc
export PATH=$PATH:$SGE_ROOT/bin/lx-amd64

# scratch path - where the job will make output
d="/fake"
# scripts path
d2="/fake2"

qsub -V -b y -N webjob -e ${d}/logs -o ${d}/logs -l mem=2G,time=1:: -S /bin/sh -wd ${d} ${d2}/test_job.sh ${d}
