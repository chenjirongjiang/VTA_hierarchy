'''
##Hierarchy tree learning for lowest resolution, all cells with labels
#More memory is needed than noted, as the whole dataset needs to be loaded in. 
#If the job crashes without explanation most like need more memory.
Job ID: 10966444
Cluster: ubec
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 14:14:32
CPU Efficiency: 99.09% of 14:22:22 core-walltime
Job Wall-clock time: 07:11:11
Memory Utilized: 1.82 GB
Memory Efficiency: 1.82% of 100.00 GB


##Hierarchy tree learning for highest resolution, neuron only
Job ID: 12106143
Cluster: ubec
User/Group: jjiang/hers_basak
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 03:58:15
CPU Efficiency: 99.15% of 04:00:18 core-walltime
Job Wall-clock time: 02:00:09
Memory Utilized: 1.04 GB
Memory Efficiency: 1.04% of 100.00 GB
'''



## Used in Slurm Job [tightly-coupled/independent]
## Learns hiearchy tree and saves it in a pickle file; labels failed to be placed in the tree were also saved in a separate file
## Note that the hierarchy tree contains the failed labels as separate branches. (can change by using attach_missing=False)

import scarches as sca
from scarches.dataset.trvae.data_handling import remove_sparsity
import os
import pickle

#To make reproducible plots
np.random.seed(41)

#set data path
os.chdir('/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/')
sc.settings.figdir = '/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/scarches/'
np.random.seed(41)

#Load h5ad file
source_latent=sc.read_h5ad('/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/scvi/models/scvi_model_final_astro_all/latent_known_high5.h5ad')

#Learn tree hiearchy
tree_ref, mp_ref = sca.classifiers.scHPL.learn_tree(data = source_latent,
                batch_key = 'atlas',
                batch_order = ['siletti', 'altena','welch', 'smajic', 'agarwal'],
                cell_type_key='cell_type_high_res',
                classifier = 'knn', dynamic_neighbors=True,
                dimred = False, print_conf= False,attach_missing=True)

#Save hierarchy tree and missing labels
with open('/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/scvi/models/scvi_model_final_astro_all/tree_ref_high_5.pkl', 'wb') as file:

    # A new file will be created
    pickle.dump(tree_ref, file)

with open('/home/hers_basak/jjiang/jack/outputs/deliverables/5_integration/data/scvi/models/scvi_model_final_astro_all/mp_ref_high_5.pkl', 'wb') as file:

    # A new file will be created
    pickle.dump(mp_ref, file)
