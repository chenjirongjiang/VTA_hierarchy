##Calculate expected doublet rate based on recovered cells according to https://uofuhealth.utah.edu/huntsman/shared-resources/gcb/htg/single-cell/genomics-10x
#Note after 10k recovered cells the resource stops, so I continued in a linear fashion (+0.7, +0.8)
#this calculator recommended by Scrublet uses loaded amount of cells, which is not always known https://demultiplexing-doublet-detecting-docs.readthedocs.io/en/latest/test.html
#Used on personal laptop


def doublet_rate(recovered_cells:list[int])->list[float]:
    """Calculated the expected doublet rate given the # of recovered cells
    
    Parameters
    -------------------------------------------------------------
    recovered_cells: List[int]
        List of # recovered cells
    
    return
    -----------------------------------------------------------------
    List of expected doublet rates
    """
    multiplet_rates=[0.4, 0.8, 1.6, 2.3, 3.1, 3.9, 4.6, 5.4, 6.1, 6.9, 7.6, 8.3,9.1,9.8,10.6,11.3,12.1,12.8,13.6,14.3,15.1,15.8,16.6,17.3,18.1,18.8,19.6,20.3,21.1,21.8,22.6,23.3,24.1]
    result = []
    for cells in recovered_cells:
        index = cells//1000

        res_factor = (cells%1000) /1000
        diff = multiplet_rates[index+1] - multiplet_rates[index] 

        rate = multiplet_rates[index] + diff * res_factor

        result.append(round(rate*0.01,4))
    return(result)
print(doublet_rate([5253,4802,6547,13726,8348,7040,7461,4774,5159,6894,8496,8380,8718,9319,7346,7720,7283,7542,4697,4785,11347,8338,10214,6544,7033,5559,4861,8878,8956,7588,7679,6967,6415,6176,6415,2625,2872,6804,7379,7975,8040,8179,10515]))