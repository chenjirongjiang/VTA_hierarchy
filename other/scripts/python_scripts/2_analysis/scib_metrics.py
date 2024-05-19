'''
## Hyperparameter optimization evaluation
Job ID: 7881157
Cluster: ubec
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 04:50:34
CPU Efficiency: 86.94% of 05:34:14 core-walltime
Job Wall-clock time: 02:47:07
Memory Utilized: 22.54 GB
Memory Efficiency: 15.03% of 150.00 GB

## Integration method evaluation
Job ID: 7760263
Cluster: ubec
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 1-14:57:04
CPU Efficiency: 97.44% of 1-15:58:22 core-walltime
Job Wall-clock time: 19:59:11
Memory Utilized: 67.15 GB
Memory Efficiency: 44.77% of 150.00 GB

'''
## Scib to evaluate integrations
# Used in Slurm Job [tightly-coupled/independent]


import numpy as np
import pandas as pd
import anndata as ad
import scanpy as sc
import seaborn as sns
import os
import matplotlib.pyplot as plt
from scib_metrics.benchmark import Benchmarker, BioConservation, BatchCorrection
import torch

os.environ['R_HOME'] = "/home/hers_basak/jjiang/jack/miniconda/envs/scarches/lib/R/"

sc.settings.verbosity = 0             # verbosity: errors (0), warnings (1), info (2), hints (3)
sc.settings.set_figure_params(dpi=80, facecolor='white') #figure resolution and background color

import faiss

from scib_metrics.nearest_neighbors import NeighborsOutput

# These two functions are needed if you want to utilize GPU

def faiss_hnsw_nn(X: np.ndarray, k: int):
    """Gpu HNSW nearest neighbor search using faiss.

    See https://github.com/nmslib/hnswlib/blob/master/ALGO_PARAMS.md
    for index param details.
    """
    X = np.ascontiguousarray(X, dtype=np.float32)
    res = faiss.StandardGpuResources()
    M = 32
    index = faiss.IndexHNSWFlat(X.shape[1], M, faiss.METRIC_L2)
    gpu_index = faiss.index_cpu_to_gpu(res, 0, index)
    gpu_index.add(X)
    distances, indices = gpu_index.search(X, k)
    del index
    del gpu_index
    # distances are squared
    return NeighborsOutput(indices=indices, distances=np.sqrt(distances))


def faiss_brute_force_nn(X: np.ndarray, k: int):
    """Gpu brute force nearest neighbor search using faiss."""
    X = np.ascontiguousarray(X, dtype=np.float32)
    res = faiss.StandardGpuResources()
    index = faiss.IndexFlatL2(X.shape[1])
    gpu_index = faiss.index_cpu_to_gpu(res, 0, index)
    gpu_index.add(X)
    distances, indices = gpu_index.search(X, k)
    del index
    del gpu_index
    # distances are squared
    return NeighborsOutput(indices=indices, distances=np.sqrt(distances))

#set data path
os.chdir('/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/')
sc.settings.figdir = '/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/'
np.random.seed(41)

#load files
adata_integrated = sc.read_h5ad('./complete_integrated_n30.h5ad') 
print('adata_integrated is loaded')

import time

#make unintegrated .obsm
adata_integrated.obsm["Unintegrated"] = adata_integrated.obsm["X_pca"]

#set bioconservation and batch correction metrics
biocons = BioConservation(isolated_labels=False,
    nmi_ari_cluster_labels_leiden=False, 
    nmi_ari_cluster_labels_kmeans=False, 
    silhouette_label=False, 
    clisi_knn=False)

batchcor=BatchCorrection(silhouette_batch=True, 
    ilisi_knn=True, 
    kbet_per_label=True, 
    graph_connectivity=True, 
    pcr_comparison=True)

start = time.time() #timer
bm = Benchmarker(
    adata_integrated,
    batch_key="sample",
    label_key="cell_type_lvl1",
    embedding_obsm_keys=["Unintegrated", 'X_pca_harmony', 'X_scVI','X_scanorama'], #latent spaces you want to compare
    pre_integrated_embedding_obsm_key="X_pca",
    bio_conservation_metrics=biocons,
    batch_correction_metrics=batchcor,
    n_jobs=-1, #-1 = as much as given
)
bm.prepare(neighbor_computer=faiss_brute_force_nn)
bm.benchmark()
end = time.time()
print(f"Time: {int((end - start) / 60)} min {int((end - start) % 60)} sec")

#save results, min_max_scale parameter will score based on relative performance, so worst performer gets 0 and best gets 100. 
#(^ even if absolute difference is small, gives very biased end result)
path='/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/'
bm.plot_results_table(show=False, save_dir=f'{path}scib_metrics/metrics.png')
bm.plot_results_table(min_max_scale=True,show=False,save_dir=f'{path}scib_metrics/metrics_minmax.png')