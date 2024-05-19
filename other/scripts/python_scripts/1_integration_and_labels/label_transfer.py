##K-nn model for label transfer/prediction (see https://docs.scarches.org/en/latest/hlca_map_classify.html)
#Used in Jupyter Notebook [Loosely-coupled/dependent]

knn_transformer_scanorama = sca.utils.knn.weighted_knn_trainer(
    train_adata=adata_ref,
    train_adata_emb="X_scanorama",  # location of our joint embedding
    n_neighbors=50,
)
labels_scanorama, uncert_scanorama = sca.utils.knn.weighted_knn_transfer(
    query_adata=adata_query,
    query_adata_emb="X_scanorama",  # location of our embedding, query_adata.X in this case
    label_keys="harmonized_cell_type",  # (start of) obs column name(s) for which to transfer labels
    knn_model=knn_transformer_scanorama,
    ref_adata_obs=adata_ref.obs,
)
uncertainty_threshold = 0.2
labels_scanorama.rename(
    columns={
        "harmonized_cell_type": "harmonized_cell_type_unfiltered_scanorama"
    },
    inplace=True,
)
uncert_scanorama.rename(
    columns={
        "harmonized_cell_type": "harmonized_cell_type_uncert_scanorama"
    },
    inplace=True,
)
adata_combined.obs = adata_combined.obs.join(labels_scanorama)
adata_combined.obs = adata_combined.obs.join(uncert_scanorama)

adata_combined.obs['harmonized_cell_type_filtered_02_scanorama'] = adata_combined.obs[
    "harmonized_cell_type_unfiltered_scanorama"
].mask(
    adata_combined.obs["harmonized_cell_type_uncert_scanorama"] > uncertainty_threshold,
    "Unknown",
)
print(
    f"Percentage of unknown for scanorama, with uncertainty_threshold={uncertainty_threshold}:"
)
print(
    f"Filtered: {np.round(sum(adata_combined.obs['harmonized_cell_type_filtered_02_scanorama'] =='Unknown')/adata_query.n_obs*100,2)}% of previously unknown"
)
