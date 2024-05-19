## All STARSOLO RELATED SCRIPTS
##  INDEX
#  16- 39: Star index reference genome
#  42- 70: Parameter notes
#  74-133: ALTENA (standard ref genome)
# 137-174: SILETTI (standard ref genome)

###########################################################

## STAR INDEX REFERENCE GENOME

Nodes: 1
Cores per node: 4
CPU Utilized: 01:43:10
CPU Efficiency: 75.01% of 02:17:32 core-walltime
Job Wall-clock time: 00:34:23
Memory Utilized: 27.35 GB
Memory Efficiency: 54.70% of 50.00 GB


#!/bin/bash
#SBATCH -t 12:00:00
#SBATCH --mem=50G
#SBATCH --cpus-per-task=4
#SBATCH -o starsolo.log
#SBATCH -e starsolo.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

cd  /home/hers_basak/jjiang/jack/software/siletti_ref/

STAR  --runMode genomeGenerate --runThreadN 8 --genomeDir ./ --genomeFastaFiles   GRCh38.p13.genome.fa.gz --sjdbGTFfile custom_annot.gtf --genomeSAsparseD 3 

###########################################################

## Parameter notes


#--soloType: turn on STAR solo
#--genomeDir: path/to/ref/
#--readFilesIn cDNAfragmentSequence.fastq.gz CellBarcodeUMIsequence.fastq.gz: 1file of cDNA read and 2nd file barcode (cell+umi) -> 10X R2 then R1
#--readFilesCommand zcat: for zipped fastq files


#--soloFeatures Gene Velocyto: counts for other features
#--soloBarcodeReadLength 0: 1 -> calculate from CB + UMI
#--soloCBwhitelist: A barcode whitelist is the list of all known barcode sequences that have been included in the assay kit and are available during library preparation(need to be compatible with the cellranger chromium version), in "/hpc/hers_basak/bin/cellranger-6.1.1/lib/python/cellranger/barcodes"
#--soloCBmatchWLtype 1MM_multi_Nbase_pseudocounts: type whitelist files
#--soloUMIlen: barcode lengths

## Cell filtering like in cellranger 3.0
#--soloCellFilter EmptyDrops_CR %s maxPercentile 0.99 (upper percentile threshold for # UMIs detected), maxMinRatio 10 (max amount of umi in droplet can only be 10x the smallest umi), indMin 45000 (lowerbound barcode rank, based on umi counts, for ambient profile making), indMax 90000 , umiMin 500 (minimal amount of umi), umiMinFracMedian 0.01 (minimal amount has to be this fraction from median), candMaxN 20000 (maximal droplets as cells), FDR 0.01 (false discrovery rate threshold), simN 10000 (max umis that are considered as similar)

##match cellranger 4.x.x and 5.x.x results
#--soloUMIfiltering MultiGeneUMI_CR
#--soloUMIdedup 1MM_CR
#--clipAdapterType CellRanger4
#--outFilterScoreMin 30

## barcode coordinates (https://www.biostars.org/p/462568/)
#--soloCBstart: beginning of barcode
#--soloCBlen: barcode length
#--soloUMIstart: umi beginning (barcode + 1)
#--soloUMIlen: length of UMI

#####################################################################################

## ALTENA

Job ID: 26107335
Array Job ID: 26107335_5
Cluster: udac
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 8
CPU Utilized: 08:51:40
CPU Efficiency: 12.72% of 2-21:40:32 core-walltime
Job Wall-clock time: 08:42:34
Memory Utilized: 15.42 GB
Memory Efficiency: 12.05% of 128.00 GB

#!/bin/bash
#SBATCH -t 20:00:00
#SBATCH --mem=128G
#SBATCH --cpus-per-task=8
#SBATCH -o starsolo2.log
#SBATCH -e starsolo2.err
#SBATCH --array=0-1%2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

# Path to reference genome

ref=/home/hers_basak/jjiang/jack/software/ensemble_109/standard/ref_starsolo/
whitelist=/home/hers_basak/jjiang/jack/scripts/1_star/3M-february-2018.txt

samples=(UMC-AR-g004-SCI7T024_S1_L004
UMC-AR-g004-SCI7T024_S2_L004
)

path=/hpc/hers_basak/rawdata/data_SCDiscoveries/Anna_Tiziana/human_VTA/UMC-AR-g004/

fastq1=${path}/${samples[SLURM_ARRAY_TASK_ID]}_R1_001.fastq.gz
fastq2=${path}/${samples[SLURM_ARRAY_TASK_ID]}_R2_001.fastq.gz

cd /home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/van_regteren_altena_2023/standard_109/${samples[SLURM_ARRAY_TASK_ID]}/



STAR --genomeDir ${ref} --readFilesIn ${fastq2} ${fastq1} --readFilesCommand zcat \
--soloCBwhitelist ${whitelist} \
--soloFeatures Gene Velocyto \
--soloBarcodeReadLength 1 \
--soloType CB_UMI_Simple \
--soloCellFilter EmptyDrops_CR %s 0.99 10 45000 90000 500 0.01 20000 0.01 10000 \
--soloCBmatchWLtype 1MM_multi_Nbase_pseudocounts \
--soloUMIfiltering MultiGeneUMI_CR \
--soloUMIdedup 1MM_CR \
--clipAdapterType CellRanger4 \
--outFilterScoreMin 30 \
--soloCBlen 16 \
--soloUMIstart 17 \
--soloUMIlen 12  \
--soloBarcodeMate 1 \
--clip3pNbases 28


###################################################################################

## SILETTI 

#!/bin/bash
#SBATCH -t 30:00:00
#SBATCH --mem=100G
#SBATCH --cpus-per-task=8
#SBATCH -o starsolo2.log
#SBATCH -e starsolo2.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

# Path to reference genome

ref=/home/hers_basak/jjiang/jack/software/ensemble_109/standard/ref_starsolo/
whitelist=/home/hers_basak/jjiang/jack/scripts/1_star/3M-february-2018.txt

path=/home/hers_basak/jjiang/jack/outputs/fasta_files/homo_sap/siletti_2022/10X194-6_S31/

fastql3_1=${path}/10X194-6_S31_L003/10X194-6_S31_L003_R1_001.fastq.gz
fastql3_2=${path}/10X194-6_S31_L003/10X194-6_S31_L003_R2_001.fastq.gz

fastql4_1=${path}/10X194-6_S31_L004/10X194-6_S31_L004_R1_001.fastq.gz
fastql4_2=${path}/10X194-6_S31_L004/10X194-6_S31_L004_R2_001.fastq.gz

cd /home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/siletti_2022/standard_109_2/

STAR --genomeDir ${ref} --readFilesIn ${fastql3_2},${fastql4_2} ${fastql3_1},${fastql4_1} --readFilesCommand zcat --soloCBwhitelist ${whitelist} --soloFeatures Gene Velocyto --soloBarcodeReadLength 1 \
--soloType CB_UMI_Simple \
--soloCellFilter EmptyDrops_CR %s 0.99 10 45000 90000 500 0.01 20000 0.01 10000 \
--soloCBmatchWLtype 1MM_multi_Nbase_pseudocounts \
--soloUMIfiltering MultiGeneUMI_CR \
--soloUMIdedup 1MM_CR \
--clipAdapterType CellRanger4 \
--outFilterScoreMin 30 \
--soloCBlen 16 \
--soloUMIstart 17 \
--soloUMIlen 12

