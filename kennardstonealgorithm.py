# select samples using Kennard-Stone algorithm
import numpy as np

# --- input ---
# X : dataset of X-variables (samples x variables)
# k : number of samples to be selected
#
# --- output ---
# selectedsamplenumbers : selected sample numbers (training data)
# remainingsamplenumbers : remaining sample numbers (test data)

def kennardstonealgorithm( X, k ):
    X = np.array( X )
    originalX = X
    distancetoaverage = ( (X - np.tile(X.mean(axis=0), (X.shape[0], 1) ) )**2 ).sum(axis=1)
    maxdistancesamplenumber = np.where( distancetoaverage == np.max(distancetoaverage) )
    maxdistancesamplenumber = maxdistancesamplenumber[0][0]
    selectedsamplenumbers = list()
    selectedsamplenumbers.append(maxdistancesamplenumber)
    remainingsamplenumbers = np.arange( 0, X.shape[0], 1)
    X = np.delete( X, selectedsamplenumbers, 0)
    remainingsamplenumbers = np.delete( remainingsamplenumbers, selectedsamplenumbers, 0)
    for iteration in range(1, k):
        selectedsamples = originalX[selectedsamplenumbers,:]
        mindistancetoselectedsamples = list()
        for mindistancecalculationnumber in range( 0, X.shape[0]):
            distancetoselectedsamples = ( (selectedsamples - np.tile(X[mindistancecalculationnumber,:], (selectedsamples.shape[0], 1)) )**2 ).sum(axis=1)
            mindistancetoselectedsamples.append( np.min(distancetoselectedsamples) )
        maxdistancesamplenumber = np.where( mindistancetoselectedsamples == np.max(mindistancetoselectedsamples) )
        maxdistancesamplenumber = maxdistancesamplenumber[0][0]
        selectedsamplenumbers.append(remainingsamplenumbers[maxdistancesamplenumber])
        X = np.delete( X, maxdistancesamplenumber, 0)
        remainingsamplenumbers = np.delete( remainingsamplenumbers, maxdistancesamplenumber, 0)

    return selectedsamplenumbers, remainingsamplenumbers
