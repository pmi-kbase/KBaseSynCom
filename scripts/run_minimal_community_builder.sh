set +x
echo Activate syncom conda environment
source /miniconda/etc/profile.d/conda.sh
conda activate syncom
set -x

metagenomefileName=$1
genomeVectorFileName=$2
iteration=$3
mimicOutputName=$4
kneepointbasedOutputName=$5
resultdir=$6

cd $resultdir
Rscript --vanilla /kb/module/scripts/mimic_algorithm.R \
       -m $metagenomefileName \
       -g $genomeVectorFileName \
       -i $iteration  \
       -o $mimicOutputName \
       -k $kneepointbasedOutputName
