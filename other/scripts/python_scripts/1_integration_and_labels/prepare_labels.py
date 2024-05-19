#Used in Jupyter Notebook so is loosely coupled (does not import dependencies on its own)

## Very hard-coded function that prepares the various resolution labels based on the original multi-level labels
# adata: your Anndataobject with cell_type_lvl1, cell_type_lvl2 and cell_type_lvl3
# Return: none, it will add .obs['cell_type_lowest_res'], .obs['cell_type_low_res'], .obs['cell_type_med_res'] and .obs['cell_type_high_res'] to existing adata

def prepare_labels(adata):    
    low=adata.obs['cell_type_lvl1'].tolist()
    med=adata.obs['cell_type_lvl2'].tolist()
    high=adata.obs['cell_type_lvl3'].tolist()
    atlas=adata.obs['atlas'].tolist()

    #Siletti supercluster resolution was too high
    siletti_supercluster=['Miscellaneous', 'Microglia', 'Vascular', 'Fibroblast', 'Oligodendrocyte precursor', 'Committed oligodendrocyte precursor', 'Oligodendrocyte', 'Bergmann glia', 'Astrocyte', 'Ependymal', 'Choroid plexus', 'Deep-layer near-projecting', 'Deep-layer corticothalamic and 6b', 'Hippocampal CA1-3', 'Upper-layer intratelencephalic', 'Deep-layer intratelencephalic', 'Amygdala excitatory', 'Hippocampal CA4', 'Hippocampal dentate gyrus', 'Medium spiny neuron', 'Eccentric medium spiny neuron', 'Splatter', 'MGE interneuron', 'LAMP5-LHX6 and Chandelier', 'CGE interneuron', 'Upper rhombic lip', 'Cerebellar inhibitory', 'Lower rhombic lip', 'Mammillary body', 'Thalamic excitatory', 'Midbrain-derived inhibitory']

    siletti_class=['MISC', 'MGL', 'ENDO', 'FIB', 'OPC', 'OLIGO', 'OLIGO', 'ASTRO', 'ASTRO', 'EPEN', 'CHRP', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR','NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR', 'NEUR']

    cell_type_lowest_res = list()
    cell_type_low_res = list()
    cell_type_med_res = list()
    cell_type_high_res = list()

    for i in range(len(adata.obs_names)):

        #check for nan values
        if low[i] in ['','None']:
            cell_type_lowest_res.append('Unknown') #lowest
            cell_type_low_res.append('Unknown') #low
            cell_type_med_res.append('Unknown') #med
            cell_type_high_res.append('Unknown') #high
        else:
            #low for all because it is the same as lvl1
            cell_type_low_res.append(str(low[i]).replace('_','-')) #low

            #high and med for all except siletti
            if atlas[i]!='siletti':
                if high[i]!= '':
                    cell_type_high_res.append(str(high[i]).replace('_','-'))#high
                    cell_type_med_res.append(str(high[i]).replace('_','-'))#med
                elif med[i]!= '':
                    cell_type_high_res.append(str(med[i]).replace('_','-'))#high
                    cell_type_med_res.append(str(med[i]).replace('_','-'))#med
                else:
                    cell_type_high_res.append(str(low[i]).replace('_','-'))#high
                    cell_type_med_res.append(str(low[i]).replace('_','-'))#med

            #lowest, med and high for siletti
            if atlas[i]=='siletti':
                cell_index=siletti_supercluster.index(low[i])
                cell_type_lowest_res.append(str(siletti_class[cell_index]).replace('_','-'))#lowest
                cell_type_high_res.append(str(high[i]).replace('_','-'))#high
                cell_type_med_res.append(str(med[i]).replace('_','-'))#med

            #lowest for all others, because labels are too high resolution
            elif atlas[i]=='welch':

                if 'ASTRO' in low[i]:
                    cell_type_lowest_res.append('ASTRO')#lowest
                elif 'ENDO' in low[i]:
                    cell_type_lowest_res.append('ENDO')#lowest
                elif 'NEURO' in low[i]:
                    cell_type_lowest_res.append('NEURO')#lowest
                elif 'OLIGO' in low[i]:
                    cell_type_lowest_res.append('OLIGO')#lowest
                elif 'OPC' in low[i]:
                    cell_type_lowest_res.append('OPC')#lowest
                elif 'MG' in low[i]:
                    cell_type_lowest_res.append('MG')#lowest
            elif atlas[i]=='smajic':
                if 'DaNs' in low[i]:
                    cell_type_lowest_res.append('Neuron')#lowest
                elif 'CADPS2+ neurons' in low[i]:
                    cell_type_lowest_res.append('Neuron')#lowest
                elif 'Excitatory' in low[i]:
                    cell_type_lowest_res.append('Neuron')#lowest
                elif 'GABA' in low[i]:
                    cell_type_lowest_res.append('Neuron')#lowest
                elif 'Inhibitory' in low[i]:
                    cell_type_lowest_res.append('Neuron')#lowest
                else:
                    cell_type_lowest_res.append(low[i])#lowest
            elif atlas[i]=='agarwal':
                if 'DaN' in low[i]:
                    cell_type_lowest_res.append('Neuron')#lowest
                elif 'GABA neurons' in low[i]:
                    cell_type_lowest_res.append('Neuron')#lowest
                else:
                    cell_type_lowest_res.append(low[i])#lowest
            else:
                cell_type_lowest_res.append(str(low[i]).replace('_','-'))#lowest
                


    adata.obs['cell_type_lowest_res'] = cell_type_lowest_res
    adata.obs['cell_type_low_res'] = cell_type_low_res
    adata.obs['cell_type_med_res'] = cell_type_med_res
    adata.obs['cell_type_high_res'] = cell_type_high_res

    adata.obs['cell_type_high_res'] = np.char.add(np.char.add(np.array(adata.obs['cell_type_high_res'], dtype= str), '-'),
                                                 np.array(adata.obs['atlas'], dtype=str))

    adata.obs['cell_type_med_res'] = np.char.add(np.char.add(np.array(adata.obs['cell_type_med_res'], dtype= str), '-'),
                                                 np.array(adata.obs['atlas'], dtype=str))

    adata.obs['cell_type_low_res'] = np.char.add(np.char.add(np.array(adata.obs['cell_type_low_res'], dtype= str), '-'),
                                                 np.array(adata.obs['atlas'], dtype=str))

    adata.obs['cell_type_lowest_res'] = np.char.add(np.char.add(np.array(adata.obs['cell_type_lowest_res'], dtype= str), '-'),
                                                 np.array(adata.obs['atlas'], dtype=str))
