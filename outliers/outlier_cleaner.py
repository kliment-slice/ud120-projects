#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np
    res_err = np.sort(abs(net_worths - predictions), axis = 0)[-9]
    networth81 = []
    ages81 = []
    predictions81 = []
    for nw in range(len(net_worths)):
        if abs(net_worths[nw] - predictions[nw]) < res_err:
            networth81.append(net_worths[nw][0])
            ages81.append(ages[nw][0])
            predictions81.append(predictions[nw][0])
    
    error = tuple(abs(np.array(networth81) - np.array(predictions81)))
    ages81       =  tuple((np.reshape( np.array(ages81), (len(ages81), 1))))
    networth81 = tuple((np.reshape( np.array(networth81), (len(networth81), 1))))
    cleaned_data = [ages81, networth81, error]
    

    ### your code goes here

    
    return cleaned_data

