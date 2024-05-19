# Jupyter notebooks

This folder contains all Jupyter notebooks used in the project. (Note that paths within the notebooks do not correspond with the current repository.) This folder contains the following subfolders:

## 0_tests/ 

contains all alignment parameter comparisons and contains description within the Jupyter notebook describing each section. To avoid redundant work the content of subsequent folders will be described here or otherwise specified where to find the information.

## 1_preprocessing/

contains a notebook for each atlas, in which the aligned h5 files are shaped with annotations and quality control metrics. This additional information will be used to filter the data and prepare it for subsequent processing. For each h5 file a <sample_name>_preprocessed.h5ad file will be made which contain all necessary annotation for subsequent filtering. The section contains the following important subsections:

  * Doublet detection 
  * Adding quality metrics and mitochondrial gene removal
  
## 2_filtering/

contains a notebook for each atlas, in which various quality control metric values are visualized and data is filtered based on threshold made on the observations/domain knowledge. The section contains the following important subsections:

  * Doublet filtering 
  * UMIs and gene counts filtering 

## 3_normalization/

contains a notebook for each atlas, in which the data is normalized based on sequencing depth and gene length so the cells are comparable. Subsequently dimensional reduction and clustering are performed to visualize samples separately. The section contains the following important subsections:

  * Normalization 
  * Dimensional reduction 
  * Marker genes and property annotation visualizations 

## 4_merging/

contains a notebook for each atlas, in which the different samples within a dataset are merged and visualized. The section contains the following important subsections:

  * Merging 
  * Alignment parameter visualization 

## 5_integration/

contains various notebooks used for the final integration and subsequent analyses. Details are provided within the notebooks.