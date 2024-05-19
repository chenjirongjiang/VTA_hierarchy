## DOWNLOAD PACKAGES
# Downloading bam files 4h for 5x 20gb files

#!/bin/bash
#SBATCH -t 1:00:00
#SBATCH -o download.log
#SBATCH -e download.err

cd /hpc/hers_basak/rnaseq_data/Basaklab/jjiang/software

wget https://ftp.cngb.org/pub/Tool/Aspera/ibm-aspera-connect_4.2.2.135_linux.ta$
tar -zxvf ibm-aspera-connect-3.11.1.58-linux-g2.12-64.tar.gz
sh ibm-aspera-connect-3.11.1.58-linux-g2.12-64.sh



#########################################################################

## USE ASPERA FOR CNSA FASTQ DOWNLOAD OF ZHONG MOUSE DATA
# It took ~1.5h for ~180GB file with 8cpus per task and 100GB memory
# FAILED (was at last file): 12h for 7 files around ~180GB with 8cpus per task, 120GB memory and array 0-6%2

#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH --mem=128G
#SBATCH --cpus-per-task=8
#SBATCH -o aspera.log
#SBATCH -e aspera.err
#SBATCH --array=0-1%2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

key=/hpc/hers_basak/rnaseq_data/Basaklab/jjiang/software/aspera_download.key
author=zhong_2021
out=/hpc/hers_basak/rnaseq_data/Basaklab/jjiang/outputs/fasta_files/mus_mus/${author}

cd ${out}

# Array of CNSA paths
paths=(CNS0195730/CNX0143518/CNR0176473
CNS0195733/CNX0143521/CNR0176476
)



# -i: aspera key
# -P: ssh-port (default 22)
# -T: disable encryption for max throughput
# -k1: resume partially transferred file (default 0)
# -l: target transfer rate in kbps (default 10000)
/hpc/hers_basak/rnaseq_data/Basaklab/jjiang/software/aspera/connect/bin/ascp -i ${key} -P33001 -T -k1 -l100m aspera_download@183.239.175.39:/pub/CNSA/data3/CNP0000892/${paths[$SLURM_ARRAY_TASK_ID]} ${out}



#########################################################################


## DOWNLOADING FASTQ FILES FROM SRA (see https://github.com/ncbi/sra-tools for quick start)
# First configure SRA toolkit (run it in terminal as it is an interactive program)

# Make sure to enable "Remote Access" in main screen
# Disable "local file-caching" in the cache tab 
# Set your user-repository location in the cache tab (needs to be empty, prefetch deposits the files here) You can use "vdb-config --prefetch-to-cwd" to set it as current working directory
# Accept "report cloud instance identity" in the cloud provider tab
/hpc/hers_basak/bin/software/sratoolkit.3.0.0-centos_linux64/bin/vdb-config --interactive


#########################################################################

## fastq-dump
## 2x 12.5GB with 3 cpus per task and default 6 threads per call took ~4h
## On paired reads and mate pair reads: https://gatk.broadinstitute.org/hc/en-us/articles/360035531792-Paired-end-or-mate-pair

##!/bin/bash
#SBATCH -t 16:00:00
#SBATCH --mem=128G
#SBATCH --cpus-per-task=3
#SBATCH -o smajic2021_data_test.log
#SBATCH -e smajic2021_data_test.err
#SBATCH --array=0-10%4
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl


# Set output directory
output=/hpc/hers_basak/rnaseq_data/Basaklab/jjiang/outputs/fasta_files/mus_mus/saunders_2018

# Set working directory
cd ${output}

# Array of SRA IDs
IDS=(SRR12621870
SRR12621869
SRR12621868
SRR12621867
SRR12621866
SRR12621865
SRR12621864
SRR12621863
SRR12621862
SRR12621861
)

#Use this if large amount of ids -> will make an array of ids (change array parameter of job)

file="sra_ids.txt"
IDS=()
while IFS=' ' read -ra line; do
    IDS+=("${line[@]}")
done < "$file"


# Download the fastq files
# You might need to increase download limit if a single file is larger than 20GB, for example if its 35GB you can use prefetch SRR0000001 --max-size 40000000000

prefetch ${IDS[$SLURM_ARRAY_TASK_ID]} -o ${output}

# Extract fastq file
# You might want to use one of the split parameters when working with pair end reads.
# --origfmt: use original header
# --split-files: writes reads into mate 1s, mate 2s and no mateless files
# --split-3: gives 1-3 files (R1, R2 and low Q reads respectively)
# --gzip: zip the fastq files

fastq-dump --origfmt --split-3 -O ${output} --gzip  ${IDS[$SLURM_ARRAY_TASK_ID]}


##########################################################################


## download from GEO link for Smajic UMI, Genes and Genes (was the plan before remapping)

#!/bin/bash
#SBATCH -t 04:00:00
#SBATCH --mem=20G
#SBATCH --cpus-per-task=8
#SBATCH -o download.log
#SBATCH -e download.err
#SBATCH --array=0-2%1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

out_dir=/home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/smajic_2021/old/

cd ${out_dir}

# Array of urls
urls=(https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE157783&format=file&file=GSE157783%5FIPDCO%5Fhg%5Fmidbrain%5FUMI%2Etar%2Egz
https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE157783&format=file&file=GSE157783%5FIPDCO%5Fhg%5Fmidbrain%5Fcell%2Etar%2Egz
https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE157783&format=file&file=GSE157783%5FIPDCO%5Fhg%5Fmidbrain%5Fgenes%2Etar%2Egz
)

wget ${urls[$SLURM_ARRAY_TASK_ID]}
################################################

##Welch bam file download


#!/bin/bash
#SBATCH -t 30:00:00
#SBATCH --mem=60G
#SBATCH --cpus-per-task=2
#SBATCH --array=0-22%2
#SBATCH -o download.log
#SBATCH -e download.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

urls=(https://sra-pub-src-1.s3.amazonaws.com/SRR8599205/SN_MD5893a.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599206/SN_MD5893b.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599207/SN_MD5893c.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599210/SN_MD6063a.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599211/SN_MD6063b.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599212/SN_MD6063c.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599201/SN_MD5840c.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599200/SN_MD5840b.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599199/SN_MD5840a.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599195/SN_MD5534f.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599194/SN_MD5534e.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599193/SN_MD5534d.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599192/SN_MD5534c.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599191/SN_MD5534b.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599190/SN_MD5534a.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599196/SN_MD5828a.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599197/SN_MD5828b.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599198/SN_MD5828c.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599204/SN_MD5862c.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599203/SN_MD5862b.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599202/SN_MD5862a.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599209/SN_MD6060b.bam.1
https://sra-pub-src-1.s3.amazonaws.com/SRR8599208/SN_MD6060a.bam.1
)

wget ${urls[SLURM_ARRAY_TASK_ID]}

#######################################################

##Wang fastq file download, request was requested on (https://explore.data.humancellatlas.org/projects/16cd6791-2adb-4d0f-8222-0184dada6456) which will give a script. 
#However downloading everything (1.1k files and ~1000GB) was not feasible nor needed
#So I copied the http link provided which gave me all download links, filtered on only the ones I needed and put them in the urls_wang.txt

#!/bin/bash
#SBATCH -t 30:00:00
#SBATCH --mem=60G
#SBATCH --cpus-per-task=1
#SBATCH --array=0-323%8
#SBATCH -o wang_download.log
#SBATCH -e wang_download.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl



readarray -t urls < ./urls_wang.txt
readarray -t outputs < ./outputs_wang.txt

curl --location --fail ${urls[SLURM_ARRAY_TASK_ID]} -o ${outputs[SLURM_ARRAY_TASK_ID]}


