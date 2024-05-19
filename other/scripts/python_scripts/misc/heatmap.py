##Heatmap of distance matrix (used in Jupyter Notebook)
#works but is not useful as you only want to measure distance of identical data in the tests
def distance_heatmap(adata,color,group,values,save):
    from scipy.spatial import distance_matrix
    subset=adata[adata.obs[group]==values[0]]
    subset_intron=adata[adata.obs[group]==values[1]]

    matrix1_pca=subset.obsm['X_pca']
    matrix2_pca=subset_intron.obsm['X_pca']
    correlation_base= distance_matrix(matrix1_pca, matrix2_pca)

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_base,cmap=color)

    # Add group labels as y-axis tick labels
    plt.xticks(ticks=[5754/2,5754 + (10948/2)],
               labels=['Hey', 'Zhong'])

    # Add group labels as y-axis tick labels
    plt.yticks(ticks=[4129/2,4129+(8312/2)],
               labels=['Hey', 'Zhong'])

    # Set labels for axes
    plt.xlabel('Include intronic mapping')
    plt.ylabel('Exonic mapping')
    plt.title('Correlation Heatmap')

    plt.show()
    plt.savefig(save)