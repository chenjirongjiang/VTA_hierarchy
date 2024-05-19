# Integration of single cell transcriptomic atlases of the adult human midbrain
This project is made by Chen Ji Rong "Jack" Jiang in collaboration with the [BasakLab](https://basaklab.com/). Special thanks to Professor [Onur Basak](https://www.linkedin.com/in/onur-basak-a2b96468) for his guidance.

## Abstract

The cellular composition of the human brain has shown to be more heterogeneous than previously understood. The ventral midbrain is no exception. Advances in single-cell technologies has enable the creation of high-resolution transcriptomic datasets. However, current atlases lack representation of rare cell types, obscuring their distinction from noise in subsequent analyses. In this thesis, we present an integrated midbrain reference atlas that combines data from two midbrain atlases, three substantia nigra (SN) datasets and one ventral tegmental area (VTA) atlas. The additional data enhances the sensitivity of the dataset, allowing for more refined subtyping of the (ventral) midbrain. Additionally, we optimized the integration pipeline with harmonized realignments of the original snRNA reads, benchmarks of integration methods such as scVI, Harmony and Scanorama using batch correction metrics, and hyperparameter tuning on scVI. By investigating the hierarchical relationships between previously identified subtypes, we found agreements across datasets. Notably, we provided evidence for VTA-related combinatorial subtypes that express both gamma-aminobutyric acid (GABA) and dopamine neurotransmitters. Our findings support the existence of specialized subtypes that can be efficiently discerned through region specific atlases. We anticipate this reference genome to serve as a cornerstone for future research on the human midbrain and to expand over time with the inclusion of additional atlases. 

## Overview
Key steps involve:
- Batch effect testing to justify harmonized mapping of snRNA datasets.
- Preprocessing of atlases into AnnData objects, including quality control and normalisation.
- Benchmarking of different integration methods, including scVI, Harmony and Scanorama, with Scib.
- Hyperparameter optimisation.
- Unsupervised integration using scVI.
- Visualise hierarchical relationships with scHPL.
- Low resolution label prediction of previously unknown cells using a nearest neighbour algorithm.

## Content

The project files has been divided into three folders:

- notebooks/ contains all Jupyter notebooks used in the project and has been further divided into 0_tests, 1_preprocessing, 2_filtering, 3_normalization, 4_clustering and 5_integration.

- bash_scripts/ contains all bash scripts used in the project.

- other/ contains all deliverable produced in this project such as reports, data, images, and presentations.

![integration](https://github.com/chenjirongjiang/VTA_hierarchy/assets/70864155/358914af-7ab2-469e-962b-091f502d82b5)
