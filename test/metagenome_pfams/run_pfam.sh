#Step 1: First install dependencies and prepare db
#sTEP 2: ./run_pfam.sh metagenome1.faa
#see output in $protein_file.pfam $protein_file.pfam.out
protein_file=$1

#Run with pfam27
hmmscan=./hmmscan.linux
pfamdb=./db2/Pfam-A.hmm
$hmmscan -o $protein_file.stdout  --domtblout=$protein_file.pfam --acc --notextw --cut_tc $pfamdb $protein_file 

#Output is in $protein_file.pfam.out
python parser.py --file $protein_file.pfam  --evalue 1e-05 --overlap 40
