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

echo $1
echo $2
echo $3
echo $4
echo $5
echo $6



cd $resultdir
cp /kb/module/scripts/minimal_community.R $resultdir
echo $resultdir
ls -al $resultdir
#echo Now Running Rscript --vanilla minimal_community.R \
#       -m $metagenomefileName \
#       -g $genomeVectorFileName \
#       -i $iteration  \
#       -o $mimicOutputName \
#       -k $kneepointbasedOutputName

Rscript --vanilla minimal_community.R \
       -m $metagenomefileName \
       -g $genomeVectorFileName \
       -i $iteration  \
       -o $mimicOutputName \
       -k $kneepointbasedOutputName


