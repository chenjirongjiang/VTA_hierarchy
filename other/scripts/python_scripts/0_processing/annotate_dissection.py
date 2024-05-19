##Annotate siletti cells with dissection adata.obs feature
#Used in Jupyter Notebook [Loosely-coupled/dependent]

def annotate_dissection(adata,non_siletti_value=''):

	"""Adds siletti dissection annotation and abreviation, specific for their file
    
    Parameters
    --------------------------------------------------------------------------
    adata: Anndata object 
            Contains your siletti cells with the same naming convention as .obs_names: <sample_name>:<UMI>: (e.g. 10X173_3:CTCATCGTCGTTCTAT)
    non_siletti_value: str
            Value for observation that are not present or annotated in the siletti atlas
    
    return
    -----------------------------------------------------
    None (Changes your adata)
    """
	annotation = pd.read_csv('/home/hers_basak/jjiang/jack/outputs/deliverables/6_analysis/siletti_metadata_midbrain.csv')
	names =adata.obs['sample'].tolist()
	index_names = []
	for name in names:
	    if name.replace('-','_') in annotation.iloc[:, 0].tolist():
	        index_names.append(annotation.iloc[:, 0].tolist().index(name.replace('-','_')))
	        
	    else:
	        index_names.append(non_siletti_value)


	abrev= [] 
	dissect= [] 

	for i in index_names:
	    if i!=non_siletti_value:
	        abrev.append(annotation.iloc[i, 6])
	        dissect.append(annotation.iloc[i, 5])
	    else:
	        abrev.append(non_siletti_value)
	        dissect.append(non_siletti_value)

	adata.obs['siletti_dissection'] = dissect
	adata.obs['siletti_dissection_abrev'] = abrev