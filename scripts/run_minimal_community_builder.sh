#!/bin/bash
set +x
echo Activate syncom conda environment
source /miniconda/etc/profile.d/conda.sh
conda activate syncom
set -x


resultdir=$1
metagenomefileName=$2
genomeVectorFileName=$3
iteration=$4
mimicOutputName=$5
kneepointbasedOutputName=$6

cd $resultdir
Rscript --vanilla /kb/module/scripts/minimal_community.R \
       -m $metagenomefileName \
       -g $genomeVectorFileName \
       -i $iteration  \
       -o $mimicOutputName \
       -k $kneepointbasedOutputName
