### remove ambient RNA using cellbender
Job ID: 26153659
Cluster: udac
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 00:40:09
CPU Efficiency: 52.39% of 01:16:38 core-walltime
Job Wall-clock time: 00:38:19
Memory Utilized: 3.42 GB
Memory Efficiency: 17.12% of 20.00 GB

## Parameters and activating cellbender (left out of other code to reduce redundancy)

#!/bin/bash
#SBATCH -t 12:00:00
#SBATCH --mem=20G
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --gpus-per-task=1
#SBATCH -o cellbender.out
#SBATCH -e cellbender.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=c.j.r.jiang@umcutrecht.nl

source /hpc/hers_basak/bin/miniconda3/etc/profile.d/conda.sh 
export LD_LIBRARY_PATH=/hpc/hers_basak/bin/miniconda3/lib:$LD_LIBRARY_PATH
conda activate CellBender

#--input: cellranger raw_feature_bc_matrix.h5
#--output: filtered output h5 file
#--cuda: for gpu
#--expected-cells: loaded cells
#--total-droplets-included: rows
#--fpr: threshold for multiple testing
#--epochs: training cycles

#############################################################################
#zhong

out_path=/home/hers_basak/jjiang/jack/outputs/count_files/mus_mus/zhong_2021/cellbender/



cellbender remove-background \
     --input /home/hers_basak/jjiang/jack/outputs/count_files/mus_mus/zhong_2021/ref98_cellrangerv6_intron/outs/raw_feature_bc_matrix.h5 \
     --output ./zhong_2021.h5 \
     --expected-cells 5500 \
     --total-droplets-included 20000 \
     --cuda \
     --fpr 0.01 \
     --epochs 150

######################################

#hey

out_path=/home/hers_basak/jjiang/jack/outputs/count_files/mus_mus/hey/cellbender/

cd ${out_path}

cellbender remove-background \
     --input /home/hers_basak/jjiang/jack/outputs/count_files/mus_mus/hey/ref98_cellrangerv6_intron/outs/raw_feature_bc_matrix.h5 \
     --output ./filtered_hey.h5 \
     --expected-cells 6,025 \
     --total-droplets-included 10000 \
     --cuda \
     --fpr 0.01 \
     --epochs 150

###########################################

#van regteren altena

out_path=/home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/van_regteren_altena_2023/cellranger/standard_109/

SAMPLES=(UMC-AR-g004
UMC-AR-g005
UMC-AR-g011
UMC-AR-g012
UMC-AR-g013
UMC-AR-g014
UMC-AR-g015
UMC-AR-g016
UMC-AR-g017
UMC-AR-g018_fastq
UMC-AR-g019_fastq
UMC-AR-g020_fastq
)

# expected cells, remove the comments when actually running code

expected_cells=(6824 #g004
8804 #g005
9283 #g011
2867 #g012
10777 #g013
5992 #g014
6144 #g015
2322 #g016
9505 #g017
8835 #g018
9257 #g019 !High Fraction of Reads Mapped Antisense to Genes
9366 #g020
)

# total droplets

droplets=(13000 #g004
13000 #g005
15000 #g011
8000 #g012
20000 #g013
15000 #g014
15000 #g015
7000 #g016
18000 #g017
16000 #g018
17000 #g019
17000 #g020
)

cd ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/


cellbender remove-background \
     --input ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/raw_feature_bc_matrix.h5 \
     --output ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/${SAMPLES[SLURM_ARRAY_TASK_ID]}_cellbender.h5 \
     --expected-cells ${expected_cells[SLURM_ARRAY_TASK_ID]} \
     --total-droplets-included ${droplets[SLURM_ARRAY_TASK_ID]} \
     --cuda \
     --fpr 0.01 \
     --epochs 150

###################################################

# Smajic

out_path=/home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/smajic_2021/ref109_v6.1/

SAMPLES=(SRR12621867
SRR12621868
SRR12621869
SRR12621870
SRR12621871
SRR12621872
)

expected_cells=(5773
5505
2839
5492
3534
7158
)

# total droplets

droplets=(15000 #not so clear curve
15000
10000
14000
12000
17000
)

cd ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/


cellbender remove-background \
     --input ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/raw_feature_bc_matrix.h5 \
     --output ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/${SAMPLES[SLURM_ARRAY_TASK_ID]}_cellbender.h5 \
     --expected-cells ${expected_cells[SLURM_ARRAY_TASK_ID]} \
     --total-droplets-included ${droplets[SLURM_ARRAY_TASK_ID]} \
     --cuda \
     --fpr 0.01 \
     --epochs 150

##################################

## Agarwal Done

GSM4157068: high fraction antisense to genes -> normal for snrna
GSM4157069
GSM4157070
GSM4157072
GSM4157074
GSM4157076
GSM4157078

out_path=/home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/agarwal_2021/

SAMPLES=(GSM4157068
GSM4157069
GSM4157070
GSM4157072
GSM4157074
GSM4157076
GSM4157078
)

# expected cells, remove the comments when actually running code

expected_cells=(2036
1504
1171
733
2058
1928
1400
)

# total droplets

droplets=(5000
6000
3000
5000
6000
7000
6000
)

cd ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/


cellbender remove-background \
     --input ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/raw_feature_bc_matrix.h5 \
     --output ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/${SAMPLES[SLURM_ARRAY_TASK_ID]}_cellbender.h5 \
     --expected-cells ${expected_cells[SLURM_ARRAY_TASK_ID]} \
     --total-droplets-included ${droplets[SLURM_ARRAY_TASK_ID]} \
     --cuda \
     --fpr 0.01 \
     --epochs 150

#######################################

##Wang (no droplet parameter for 09)

out_path=/home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/wang_2022

SAMPLES=(SAMN21889406
SAMN21889407
SAMN21889409
SAMN21889411
SAMN21889416
SAMN21889422
SAMN21889423
SAMN21889424
SAMN21889433
SAMN21889436
)

# expected cells, remove the comments when actually running code

expected_cells=(23445
15938
54785
8201
11383
8574
8782
6658
12484
2649
)

# total droplets

droplets=(100000
100000
150000
100000
100000
100000
100000
100000
100000
100000
)

cd ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/


cellbender remove-background \
     --input ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/raw_feature_bc_matrix.h5 \
     --output ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/${SAMPLES[SLURM_ARRAY_TASK_ID]}_cellbender.h5 \
     --expected-cells ${expected_cells[SLURM_ARRAY_TASK_ID]} \
     --total-droplets-included ${droplets[SLURM_ARRAY_TASK_ID]} \
     --cuda \
     --fpr 0.01 \
     --epochs 150

############################################################
##Welch

out_path=/home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/welch_2019

SAMPLES=(SN_MD5534a
SN_MD5534b
SN_MD5534c
SN_MD5534d
SN_MD5534e
SN_MD5534f
SN_MD5828a
SN_MD5828b
SN_MD5828c
SN_MD5840a
SN_MD5840b
SN_MD5840c
SN_MD5862a
SN_MD5862b
SN_MD5862c
SN_MD5893a
SN_MD5893b
SN_MD5893c
SN_MD6060a
SN_MD6060b
SN_MD6063a
SN_MD6063b
SN_MD6063c
)


# expected cells, remove the comments when actually running code

expected_cells=(5734
4746
2377
3354
3626
3425
2366
1798
2808
2008
5337
2893
2773
1937
3140
3537
4101
3544
5658
4569
6669
7368
6430
)

# total droplets

droplets=(15000
15000
10000
10000
10000
12000
10000
10000
14000
12500
25000
10000
10000
8000
12000
8000
15000
20000
20000
20000
25000
30000
25000
)

cd ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/


cellbender remove-background \
     --input ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/raw_feature_bc_matrix.h5 \
     --output ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/${SAMPLES[SLURM_ARRAY_TASK_ID]}_cellbender.h5 \
     --expected-cells ${expected_cells[SLURM_ARRAY_TASK_ID]} \
     --total-droplets-included ${droplets[SLURM_ARRAY_TASK_ID]} \
     --cuda \
     --fpr 0.01 \
     --epochs 150
############################################################
##Siletti

out_path=/home/hers_basak/jjiang/jack/outputs/count_files/homo_sap/siletti_2022

SAMPLES=(10X173-3
10X173-4
10X173-5
10X175-7
10X175-8
10X176-1
10X176-2
10X193-1
10X193-2
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


# expected cells, remove the comments when actually running code

expected_cells=(5253
4802
6547
13726
8348
7040
7461
4774
5159
6894
8496
8380
8718
9319
7346
7720
7283
7542
4697
4785
11347
8338
10214
6544
7033
5559
4861
8878
8956
7588
7679
6967
6415
6176
6415
2625
2872
6804
7379
7975
8040
8179
10515
)

# total droplets
10X354-1 different from others-> cellbender might not do well

droplets=(12000
12000
12000
20000
17000
15000
15000
12000
12000
15000
18000
17000
18000
20000
16000
16000
16000
16000
12000
12000
20000
18000
20000
16000
15000
30000
12000
15000
15000
15000
15000
15000
15000
13000
13000
7000
9000
13000
15000
20000
16000
17000
20000)

cd ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/


cellbender remove-background \
     --input ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/raw_feature_bc_matrix.h5 \
     --output ${out_path}/${SAMPLES[SLURM_ARRAY_TASK_ID]}/outs/${SAMPLES[SLURM_ARRAY_TASK_ID]}_cellbender.h5 \
     --expected-cells ${expected_cells[SLURM_ARRAY_TASK_ID]} \
     --total-droplets-included ${droplets[SLURM_ARRAY_TASK_ID]} \
     --cuda \
     --fpr 0.01 \
     --epochs 150
