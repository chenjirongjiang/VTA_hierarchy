## All CELL RANGER RELATED SCRIPTS
##  INDEX
#   5- 60: bamtofastq (welch)
#  63- 84: indexing ref genome (siletti custome)
#  87-119: Alignment hey (v6 ensemble 98 w/ intron)
# 122-154: Alignment hey (2 samples for tests)
# 158-   : Start Human Counts (van Regteren Altena is missing)
# 160-200: SMAJIC
# 203-241: AGARWAL
# 244-290: WANG
# 294-326: WELCH
# 331-435: SILETTI
################################################################

Job ID: 28236215
Array Job ID: 28236213_1
Cluster: udac
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 01:52:25
CPU Efficiency: 97.27% of 01:55:34 core-walltime
Job Wall-clock time: 00:57:47
Memory Utilized: 49.15 MB
Memory Efficiency: 0.12% of 40.00 GB

## Bam to fastq for Welch

#!/bin/bash
#SBATCH -t 20:00:00
#SBATCH --mem=40G
#SBATCH --cpus-per-task=2
#SBATCH --array=0-22%2
#SBATCH -o bam.log
#SBATCH -e bam.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

path=/home/hers_basak/jjiang/jack/outputs/fasta_files/homo_sap/welch_2019/bam

bam=(SN_MD5534a.bam.1
SN_MD5534b.bam.1
SN_MD5534c.bam.1
SN_MD5534d.bam.1
SN_MD5534e.bam.1
SN_MD5534f.bam.1
SN_MD5828a.bam.1
SN_MD5828b.bam.1
SN_MD5828c.bam.1
SN_MD5840a.bam.1
SN_MD5840b.bam.1
SN_MD5840c.bam.1
SN_MD5862a.bam.1
SN_MD5862b.bam.1
SN_MD5862c.bam.1
SN_MD5893a.bam.1
SN_MD5893b.bam.1
SN_MD5893c.bam.1
SN_MD6060a.bam.1
SN_MD6060b.bam.1
SN_MD6063a.bam.1
SN_MD6063b.bam.1
SN_MD6063c.bam.1)

bam_path=${path}/${bam[SLURM_ARRAY_TASK_ID]}

cellranger bamtofastq ${bam_path} /home/hers_basak/jjiang/jack/outputs/fasta_files/homo_sap/welch_2019/${bam[SLURM_ARRAY_TASK_ID]}

########################################################################
## Indexing 109 custom (siletti)

## Indexing ref genome

#!/bin/bash
#SBATCH -t 12:00:00
#SBATCH --mem=40G
#SBATCH --cpus-per-task=8
#SBATCH -o ref.log
#SBATCH -e ref.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

cd /home/hers_basak/jjiang/jack/software/ensemble_109_standard


cellranger mkref \
--genome=GRCm38.p6.indexed \
--fasta=GRCm38.p6.genome.fa.gz \
--genes=gencode.vM21.annotation.filtered.gtf


#################################################################


## Alignment hey (v6 ensemble 98 w/ intron)
# 3h for 2 human fasta files with 128GB and 16 cpus per task

#!/bin/bash
#SBATCH -t 6:00:00
#SBATCH --mem=70G
#SBATCH --cpus-per-task=8
#SBATCH -o alignment_v3.log
#SBATCH -e alignment_v3.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

# Dataset variable
out_dir=ref98_cellrangerv6_intron

fastqs=/hpc/hers_basak/rnaseq_data/Basaklab/jjiang/outputs/fasta_files/mus_mus/hey/
reference=/hpc/hers_basak/bin/reference_genomes_cellranger/refdata-gex-mm10-2020-A/


# Move to count folder
cd /hpc/hers_basak/rnaseq_data/Basaklab/jjiang/outputs/count_files/mus_mus/hey/

# --id: unique run id and ouput folder name
# --fastqs: path to sequence files
# --sample: prefix of fastqs to select (needed when multiple samples were demultiplexed)
# --transcriptome: path to folder with 10x-compatible transcriptome reference
# --include-introns: include intronic reads in count
# fasta files need to be in this naming convention: SampleName_S1_L001_R1_001.fastq.gz

cellranger count --id=${out_dir} --fastqs=${fastqs} --transcriptome=${reference} --expect-cells=5000 --include-introns

################################################################
## Alignment Altena (2 samples for tests)

#!/bin/bash
#SBATCH -t 30:00:00
#SBATCH --mem=128G
#SBATCH --cpus-per-task=4
#SBATCH -o alignment_hs.log
#SBATCH -e alignment_hs.err
#SBATCH --array=0-1%2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

# Dataset variable

reference=/home/hers_basak/jjiang/jack/software/ensemble_109/standard/ref_cellranger/standard_109.indexed

fastqs=/hpc/hers_basak/rawdata/data_SCDiscoveries/Anna_Tiziana/human_VTA/UMC-AR-g004/

SAMPLES=(UMC-AR-g004-SCI7T024_S1
UMC-AR-g004-SCI7T024_S2
)

# Move to count folder
cd /home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/van_regteren_altena_2023/cellranger/standard_109/

# --id: unique run id and ouput folder name
# --fastqs: path to sequence files
# --sample: prefix of fastqs to select (needed when multiple samples were demultiplexed)
# --transcriptome: path to folder with 10x-compatible transcriptome reference
# --include-introns: include intronic reads in count
# fasta files need to be in this naming convention: SampleName_S1_L001_R1_001.fastq.gz

cellranger count --id=${SAMPLES[$SLURM_ARRAY_TASK_ID]} --fastqs=${fastqs} --samples=${SAMPLES[SLURM_ARRAY_TASK_ID]} --transcriptome=${reference} --include-introns --expect-cells=8000
#####################################################################################################################

## OFFICIAL START HUMAN ALIGNMENT
# Job parameters are left out after this one

## SMAJIC

#!/bin/bash
#SBATCH -t 30:00:00
#SBATCH --mem=126G
#SBATCH --cpus-per-task=4
#SBATCH -o alignment_hs.log
#SBATCH -e alignment_hs.err
#SBATCH --array=0-5%2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

# Dataset variable

reference=/home/hers_basak/jjiang/jack/software/ensemble_109/standard/ref_cellranger/standard_109.indexed

path=/home/hers_basak/jjiang/jack/outputs/fasta_files/homo_sap/smajic_2021

samples=(SRR12621867
SRR12621868
SRR12621869
SRR12621870
SRR12621871
SRR12621872
)

fastqs=${path}/${samples[SLURM_ARRAY_TASK_ID]}

# Move to count folder
cd /home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/smajic_2021/ref109_v6.1/

# --id: unique run id and ouput folder name
# --fastqs: path to sequence files
# --sample: prefix of fastqs to select (needed when multiple samples were demultiplexed)
# --transcriptome: path to folder with 10x-compatible transcriptome reference
# --include-introns: include intronic reads in count
# fasta files need to be in this naming convention: SampleName_S1_L001_R1_001.fastq.gz

cellranger count --id=${samples[SLURM_ARRAY_TASK_ID]}  --fastqs=${fastqs} --transcriptome=${reference} --include-introns --expect-cells=6000

#################################################################

## AGARWAL

# Dataset variable

reference=/home/hers_basak/jjiang/jack/software/ensemble_109/standard/ref_cellranger/standard_109.indexed

fastqs=/home/hers_basak/jjiang/jack/outputs/fasta_files/homo_sap/agarwal_2021

ids=(GSM4157068
GSM4157069
GSM4157070
GSM4157072
GSM4157074
GSM4157076
GSM4157078
)

samples=(SRR10433204,SRR10433205,SRR10433206
SRR10433207
SRR10433208
SRR10433212,SRR10433213,SRR10433214
SRR10433218,SRR10433219,SRR10433220
SRR10433224
SRR10433228)

expect=(1800
600
750
700
1350
550
500
)

# Move to count folder
cd /home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/agarwal_2021/

cellranger count --id=${ids[SLURM_ARRAY_TASK_ID]} --sample=${samples[SLURM_ARRAY_TASK_ID]} --fastqs=${fastqs} --transcriptome=${reference} --include-introns --expect-cells=${expect[SLURM_ARRAY_TASK_ID]}

###################################################

## WANG

# Dataset variable

reference=/home/hers_basak/jjiang/jack/software/ensemble_109/standard/ref_cellranger/standard_109.indexed

fastqs=/home/hers_basak/jjiang/jack/outputs/fasta_files/homo_sap/wang_2022

ids=(SAMN21889411
SAMN21889406
SAMN21889416
SAMN21889423
SAMN21889424
SAMN21889433
SAMN21889422
SAMN21889407
SAMN21889409
SAMN21889436
)

samples=(SRR16105824,SRR16105825,SRR16105826,SRR16105827,SRR16105828,SRR16105829,SRR16105830,SRR16105831,SRR16105832,SRR16105833,SRR16105834,SRR16105835
SRR16105777,SRR16105778,SRR16105779,SRR16105780,SRR16105781,SRR16105782,SRR16105783,SRR16105784,SRR16105785,SRR16105786,SRR16105787,SRR16105788
SRR16105881,SRR16105882,SRR16105883,SRR16105884,SRR16105885,SRR16105886,SRR16105887,SRR16105888,SRR16105889,SRR16105890,SRR16105891,SRR16105892
SRR16105959,SRR16105960,SRR16105961,SRR16105962,SRR16105963,SRR16105964,SRR16105965,SRR16105966,SRR16105967,SRR16105968,SRR16105969,SRR16105970
SRR16105972,SRR16105973,SRR16105974,SRR16105975,SRR16105976,SRR16105977,SRR16105978,SRR16105979,SRR16105980,SRR16105981,SRR16105982,SRR16105983
SRR16106076,SRR16106077,SRR16106078,SRR16106079,SRR16106080,SRR16106081,SRR16106082,SRR16106083,SRR16106084,SRR16106085,SRR16106086,SRR16106099
SRR16105948,SRR16105949,SRR16105950,SRR16105951,SRR16105952,SRR16105953,SRR16105954,SRR16105955,SRR16105956,SRR16105957,SRR16105958,SRR16105971
SRR16105789,SRR16105790,SRR16105791,SRR16105792,SRR16105793,SRR16105794,SRR16105795,SRR16105796
SRR16105808,SRR16105809,SRR16105810,SRR16105811,SRR16105812,SRR16105813,SRR16105814,SRR16105823
SRR16106108,SRR16106109,SRR16106110,SRR16106111,SRR16106112,SRR16106113,SRR16106114,SRR16106115
)

expect=(4782
18829
10243
7421
5017
11055
7804
14068
19450
2165)

# Move to count folder
cd /home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/wang_2022

cellranger count --id=${ids[SLURM_ARRAY_TASK_ID]} --sample=${samples[SLURM_ARRAY_TASK_ID]} --fastqs=${fastqs} --transcriptome=${reference} --include-introns --expect-cells=${expect[SLURM_ARRAY_TASK_ID]}
#################################


## WELCH


reference=/home/hers_basak/jjiang/jack/software/ensemble_109/standard/ref_cellranger/standard_109.indexed

fastqs=/home/hers_basak/jjiang/jack/outputs/fasta_files/homo_sap/welch_2019

ids=(SN_MD5534e.bam.1
SN_MD5840a.bam.1
SN_MD6060a.bam.1
SN_MD5534a.bam.1
SN_MD5534f.bam.1
SN_MD5840b.bam.1
SN_MD6060b.bam.1
SN_MD5534b.bam.1
SN_MD5828a.bam.1
SN_MD5893a.bam.1
SN_MD6063a.bam.1
SN_MD5534c.bam.1
SN_MD5828b.bam.1
SN_MD5893b.bam.1
SN_MD6063b.bam.1
SN_MD5534d.bam.1
SN_MD5828c.bam.1
SN_MD5893c.bam.1
SN_MD6063c.bam.1
)


# Move to count folder
cd /home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/welch2019

cellranger count --id=${ids[SLURM_ARRAY_TASK_ID]}  --fastqs=${fastqs}/${ids[SLURM_ARRAY_TASK_ID]} --transcriptome=${reference} --include-introns 


#########################################################################

## SILETTI (44 samples)

# Dataset variable

reference=/home/hers_basak/jjiang/jack/software/ensemble_109/standard/ref_cellranger/standard_109.indexed

fastqs=/home/hers_basak/jjiang/jack/outputs/fasta_files/homo_sap/siletti_2022/


samples=(10X173-3
10X173-4
10X173-5
10X175-7
10X175-8
10X176-1
10X176-2
10X193-1
10X193-2
10X194-3
10X194-4
10X194-5
10X194-6
10X194-7
10X194-8
10X225-1
10X225-2
10X230-1
10X230-2
10X230-3
10X230-4
10X236-1
10X236-2
10X237-3
10X330-7
10X330-8
10X354-1
10X354-2
10X358-1
10X358-2
10X358-3
10X358-4
10X375-7
10X375-8
10X376-1
10X376-2
10X377-7
10X377-8
10X378-3
10X378-4
10X378-5
10X378-6
10X389-3
10X389-4
)

expect=(5193
4706
6442
6689
6442
6101
6533
4666
5040
10486
6458
8056
7941
8285
8827
7014
7401
7058
7285
4381
4547
10937
8004
9019
6460
6940
5375
4442
8540
8658
7424
7501
6869
6325
6027
6288
2372
2587
6516
7121
7553
7712
6517
7976
)

# Move to count folder
cd /home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/siletti_2022

cellranger count --id=${samples[SLURM_ARRAY_TASK_ID]} --fastqs=${fastqs}${samples[SLURM_ARRAY_TASK_ID]}*/ --transcriptome=${reference} --include-introns --expect-cells=${expect[SLURM_ARRAY_TASK_ID]}