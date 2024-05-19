'''
## Run on whole dataset
Job ID: 5680988
Cluster: ubec
User/Group: jjiang/hers_basak
State: FAILED (exit code 1)
Nodes: 1
Cores per node: 4
CPU Utilized: 1-08:58:39
CPU Efficiency: 83.24% of 1-15:37:00 core-walltime
Job Wall-clock time: 09:54:15
Memory Utilized: 189.00 GB
Memory Efficiency: 63.00% of 300.00 GB

'''
## Used in Slurm Job [tightly-coupled/independent]
## Batch corrected .X values with Scanorama, changes the count table 
#(slow, don't use unless you have to, use the one below)

import numpy as np
import pandas as pd
import anndata as ad
import scanpy as sc
import os
import torch
import scanorama

#set data path
os.chdir('/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/scanorama')

#Load files (I use list because it was faster to copy paste at the time, do not have to)
files=['/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/complete_base_hvg.h5ad']
names=['complete']
object_names_merged=list()
numberobj = len(files)

for i in range(numberobj):
    object_names_merged.append("adata"+"_"+names[i])
    locals()[object_names_merged[i]] = sc.read(files[i])

#need to separate batches for this to work
batches = adata_complete.obs['atlas'].cat.categories.tolist()
alldata = {}
for batch in batches:
    alldata[batch] = adata_complete[adata_complete.obs['atlas'] == batch,]

adatas = list(alldata.values())

#changed the values within adata.X
corrected = scanorama.correct_scanpy(adatas)

sc.pp.neighbors(corrected, use_rep='X_scanorama',n_neighbors=30,)
corrected.write('./adata_n30_scanorama.h5ad')

#########################################################

'''
#Run on whole dataset
Job ID: 5725688
Cluster: ubec
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 02:01:41
CPU Efficiency: 53.87% of 03:45:52 core-walltime
Job Wall-clock time: 00:56:28
Memory Utilized: 70.41 GB
Memory Efficiency: 28.16% of 250.00 GB
'''

## Used in Slurm Job [tightly-coupled/independent]
## Integrate with Scanorama is so much faster (doesnt change values only adds obsm)

import numpy as np
import pandas as pd
import anndata as ad
import scanpy as sc
import os
import torch
import scanorama

#set data path
os.chdir('/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/scanorama')
files=['/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/complete_base_hvg_labelled.h5ad']

##Load files (I use list because it was faster to copy paste at the time, do not have to)
names=['complete']
object_names_merged=list()
numberobj = len(files)

for i in range(numberobj):
    object_names_merged.append("adata"+"_"+names[i])
    locals()[object_names_merged[i]] = sc.read(files[i])

#need to separate batches for this to work
batches = adata_complete.obs['atlas'].cat.categories.tolist()
alldata = {}
for batch in batches:
    alldata[batch] = adata_complete[adata_complete.obs['atlas'] == batch,]

adatas = list(alldata.values())

#adds .obsm X_scanorama in the individual batches
corrected = scanorama.integrate_scanpy(adatas)

#join the batches
adata_complete_new=ad.concat(adatas, join='outer')
adata_complete_new.write('./adata_scanorama.h5ad')
