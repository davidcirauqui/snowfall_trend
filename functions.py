import numpy as np

def linearFit(xvec, a, b):
    """
    linear fit function
    inputs:
        xvec: independent variable (or vector of independent variables)
        a: multiplicative constant
        b: additive constant
    outputs:
        a * xvec + b
    """
    return a * xvec + b




def correctSnowDepth(snowDepth):
    """
    function that reanalyzes snow depths and corrects potential errors when
    points in the input data are missing or have non-valid values, according
    to a theoretical estimate
    inputs:
        snowDepth: array containing the time evolution of the snow depth
    outputs:
        snowDepth: corrected time evolution of the snow depth
    """


    seasonEnding_idx = int(.7 * len(snowDepth))
    
    for i in range(1, len(snowDepth)):
        
        # select kappa according to temperature conditions
        if (i > seasonEnding_idx):
            kappa = 400
        else:
            kappa = 150
            
        if snowDepth[i] == 0:   # if snowDepth = 0
            if snowDepth[i - 1] > 5:    # and it has been a sudden drop, then it's probably an error
                
                # fix snowDepth according to theoretical estimate
                if snowDepth[i - 1]**2 - 2 * kappa < 0:
                    snowDepth[i] = 0
                else:
                    snowDepth[i] = int(np.sqrt(snowDepth[i - 1]**2 - 2 * kappa))
                    

    return snowDepth




def countsInRange(vec, bins, normalizationCriteria = 'none'):
    """
    function that counts the number of values that a given vector has within each of 
    the specified intervals
    inputs:
        vec: array containing the values to be cunted
        bins: array of values defining the intervals
        normalizationCriteria: set the normalization criteria fot the output values. Possible
            values are:
                density: output is a probability density function
                frequency: ouput is the raw frequency of each interval
                none: value by defect, if not specified. Output is a raw count of the values 
            
    """


    counts = np.zeros(len(bins) - 1)
    for i in range(1, len(bins)):
        bin0 = bins[i-1]
        binf = bins[i]
            
        # chech in which interval falls the current value
        for v in vec:
            if (v >= bin0):
                if (v < binf):
                    # increase interval's count
                    counts[i-1] += 1
        

    # if specified, apply normalization criteria
    if (normalizationCriteria == 'density'):
        counts = counts / (sum(counts) * np.diff(bins))
    elif (normalizationCriteria == 'frequency'):
        counts = counts / sum(counts)

        
    return counts
    