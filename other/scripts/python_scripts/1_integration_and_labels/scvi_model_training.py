'''
#Run of integration
Job ID: 7274831
Cluster: ubec
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 10:46:18
CPU Efficiency: 95.03% of 11:20:08 core-walltime
Job Wall-clock time: 02:50:02
Memory Utilized: 15.84 GB
Memory Efficiency: 6.33% of 250.00 GB

'''
##scVI integration [tightly-coupled/independent]
#Used in slurm job

import numpy as np
import pandas as pd
import anndata as ad
import scanpy as sc
import seaborn as sns
import os
import matplotlib.pyplot as plt
import scvi
import torch

#set data path
os.chdir('/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/scvi/')

#Load files (I use list because it was faster to copy paste at the time, do not have to)
files=['/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/complete_hvg3k.h5ad']
names=['complete']
object_names_merged=list()
numberobj = len(files)

for i in range(numberobj):
    object_names_merged.append("adata"+"_"+names[i])
    locals()[object_names_merged[i]] = sc.read(files[i]) 
    print(object_names_merged[i],' is loaded')

#set up anndata and model hyperparameters
#I used the original scVI function instead of the scanpy one, because I couldn't get that one to work
scvi.model.SCVI.setup_anndata(adata_complete, layer='counts',  batch_key="atlas")

model = scvi.model.SCVI(adata_complete, n_hidden=128, n_latent=10, n_layers=1, dropout_rate=0.1, dispersion='gene', gene_likelihood='zinb', latent_distribution='normal')
model.train(check_val_every_n_epoch=1
            ,batch_size=128
           )
SCVI_LATENT_KEY = "X_scVI3k"
adata_complete.obsm[SCVI_LATENT_KEY] = model.get_latent_representation()
model.save('./models/scvi_model_3k', save_anndata=True)