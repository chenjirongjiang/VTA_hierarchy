# QUALITY CHECK WITH FASTQC (check on local machine)

#!/bin/bash
#SBATCH -t 03:00:00
#SBATCH --mem=10G
#SBATCH --cpus-per-task=4
#SBATCH -o fastqc.log
#SBATCH -e fastqc.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

cd /hpc/hers_basak/rnaseq_data/Basaklab/jjiang/outputs/fastqc/

fastqc -o /hpc/hers_basak/rnaseq_data/Basaklab/jjiang/outputs/fastqc/sauders_2018 -f /hpc/hers_basak/rnaseq_data/Basaklab/jjiang/outputs/fasta_files/homo_sap/wang_2022/*.fastq.gz -d /home/hers_basak/jjiang/temp/ 
