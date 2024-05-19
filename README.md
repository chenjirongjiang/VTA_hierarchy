# Integration of single cell transcriptomic atlases of the adult human midbrain
This project is made by Chen Ji Rong "Jack" Jiang in collaboration with the [BasakLab](https://basaklab.com/). Special thanks to Professor [Onur Basak](https://www.linkedin.com/in/onur-basak-a2b96468) for his guidance.

## About

In this project, a computational pipeline was established to integrate several midbrain atlases into MidMAP, a unified midbrain atlas. This repository focuses on the analysis of the hierarchical relationships between previously established subtype labels, visualised by [scHPL](https://github.com/lcmmichielsen/scHPL).

## Overview
Key steps involve:
- Batch effect testing to justify harmonized mapping of snRNA datasets.
- Preprocessing of atlases into AnnData objects, including quality control and normalisation.
- Benchmarking of different integration methods, including scVI, Harmony and Scanorama, with Scib.
- Hyperparameter optimisation.
- Unsupervised integration using scVI.
- Visualise hierarchical relationships with scHPL.
- Low resolution label prediction of previously unknown cells using a nearest neighbour algorithm.
![Figure_3](https://github.com/chenjirongjiang/VTAmap_tests/assets/70864155/e0159fe7-4267-4ccc-b2eb-7fbefe364a2d)
