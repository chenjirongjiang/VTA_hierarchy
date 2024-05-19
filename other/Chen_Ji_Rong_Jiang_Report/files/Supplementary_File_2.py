def descend(nodes): 
    """Get the right resolution of labels -> List(str)
    
    Parameters
    -------------------------------------------------------------
    nodes: List[node]
        List of descendants nodes of the label node that you want to use as harmonized label
    
    return
    -----------------------------------------------------------------
    List of nested lists that represent all the node names that fall under the first layer of nodes.
    """
    labels=list()
    for node in nodes:
        for name in node.name:
            labels.append(name)
        if node.descendants==[]:
            continue
        else:         
            for name in descend(node.descendants):
                labels.append(name)
    return labels
    
    
def get_label_descendants(tree,level):
    """Gets the descendants at a certain level for all branches and subbranches
    
    Parameters
    --------------------------------------------------------------------------
    tree: TreeNode 
            Classification tree to take equivalent labels from (resulting from learn_tree method)
    level: Int
            Which tree depth to use to harmonize the labels (0=root only, 1: first descendants)
    
    return
    -----------------------------------------------------
    A list of nodes at a certain level
    """
    nodes=list()
    if level == 0:
        return tree
    for branch in tree.descendants:
        nodes.append(get_label_descendants(branch,level-1))
    return nodes


    
def harmonize_labels(adata,label_key,tree,level,new_key='harmonized_cell_type'):
    
    """Changes the labels to equivalent onces in all batches.
    
    Parameters
    ------------------------------------------------------
    adata: Anndata object
            Object containing the expression data as well as annotations and latent space
    label_key: str
            String for the key of the cell_type annotation that needs to be harmonized
    tree: TreeNode 
            Classification tree to take equivalent labels from (resulting from learn_tree method)
    batches: List[str]
            List of batch keys (also used for priority order in which labels is taken, need to have batch keys as suffix)
    level: Int
            Which tree depth to use to harmonize the labels (0=root only, 1: first descendants)
    new_key: str
            The new key where the harmonized cell labels will be
    return
    -------------------------------------------------------
    None, but original Anndata object will gain .obs['harmonized_celltype'] feature
    """
    
    descendants = get_label_descendants(tree[0],level)
    old_labels=list()
    new_labels=list()
    for node in descendants:
        old_labels.append(descend(node.descendants))
        node_name=node.name
        for name in node_name:
            old_labels[-1].append(name)
        new_labels.append(node_name[0])
    
    new_values=list()
    for original in adata.obs[label_key].tolist():
        unknown=True
        for i in range(len(old_labels)):
            if original in old_labels[i]:
                new_values.append(new_labels[i])
                unknown=False
                break
        if unknown ==True:
            new_values.append('unknown')
            
                
    adata.obs[new_key]=new_values
    
    return adata
    