#Install hmmer
wget https://anaconda.org/bioconda/hmmer/3.2.1/download/linux-64/hmmer-3.2.1-hf484d3e_1.tar.bz2
tar xvf hmmer-3.2.1-hf484d3e_1.tar.bz2 bin/hmmpress bin/hmmscan
mv ./bin/hmmpress hmmpress.linux
mv ./bin/hmmscan hmmscan.linux
rmdir ./bin
rm ./hmmer-3.2.1-hf484d3e_1.tar.bz2

#Prepare Pfam 32
mkdir -p db
#curl -o ./db/Pfam-A.full.gz 'ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/Pfam-A.full.gz'
curl -o ./db/Pfam-A.hmm.gz 'ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/Pfam-A.hmm.gz'
gzip -d ./db/Pfam-A.hmm.gz
hmmpress.linux db/Pfam-A.hmm


#Prepare PFam 27
mkdir -p db2
curl -o ./db2/Pfam-A.hmm.gz 'ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam27.0/Pfam-A.hmm.gz'
gzip -d ./db2/Pfam-A.hmm.gz
hmmpress.linux db2/Pfam-A.hmm

