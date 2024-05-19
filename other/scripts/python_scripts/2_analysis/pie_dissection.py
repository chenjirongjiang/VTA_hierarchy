##Siletti subtype dissection pie plot 
#Used in Jupyter notebook [loosely-coupled/dependent]

def pie_dissection(adata, save_path,siletti_subtype, title):
	"""Generate pie plot of dissection proportions of the given siletti subtype or list of siletti subtypes
    
    Parameters
    --------------------------------------------------------------------------
    adata: Anndata object 
            Contains your siletti cells with the dissection labels in .obs['siletti_dissection_abrev']
    save_path: str
            path/to/folder/<fig_name>.png
    siletti_subtype: str or list
    		String or list of siletti high resolution labels
    title: str
    		Title of plot
    
    return
    -----------------------------------------------------
    None (Changes your adata)
    """
	

	#consistent colors
	color_map = {'SN':(0.2980392156862745, 0.4470588235294118, 0.6901960784313725),
	'PAG':(0.8666666666666667, 0.5176470588235295, 0.3215686274509804),
	'SN-RN':(0.3333333333333333, 0.6588235294117647, 0.40784313725490196),
	'PTR':(0.7686274509803922, 0.3058823529411765, 0.3215686274509804),
	'RN':(0.5058823529411764, 0.4470588235294118, 0.7019607843137254),
	'SC':(0.5764705882352941, 0.47058823529411764, 0.3764705882352941),
	'IC':(0.8549019607843137, 0.5450980392156862, 0.7647058823529411),
	'':(0.5490196078431373, 0.5490196078431373, 0.5490196078431373),
	'PAG-DR':(0.8, 0.7254901960784313, 0.4549019607843137)}

	if type(siletti_subtype)==str:

		df=adata[adata.obs['cell_type_high_res']==siletti_subtype].obs['siletti_dissection_abrev'].value_counts()
		keys=df.keys().tolist()
		values=df.tolist()
		percentages=[v*100/sum(values) for v in values]


		colors = [color_map.get(key) for key in keys]
		plt.pie(values,  colors = colors,startangle=90,counterclock=False)
		plt.title(title)
		labels = [f'{l}, {s:0.1f}%' for l, s in zip(keys, percentages)]
		plt.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))
		plt.savefig(save_path)
		plt.show()
	else:
		df=adata[adata.obs['cell_type_high_res'].isin(siletti_subtype)].obs['siletti_dissection_abrev'].value_counts()
		keys=df.keys().tolist()
		values=df.tolist()
		percentages=[v*100/sum(values) for v in values]


		colors = [color_map.get(key) for key in keys]
		plt.pie(values,  colors = colors,startangle=90,counterclock=False)
		plt.title(title)
		labels = [f'{l}, {s:0.1f}%' for l, s in zip(keys, percentages)]
		plt.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))
		plt.savefig(save_path)
		plt.show()
