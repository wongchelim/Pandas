import pandas as pd
import numpy as np

#Create a series of random numbers of 4 values
scity = pd.Series(np.random.randn(4))

#print out the random numbers
print scity

#print out the values in one line.
print scity.values
#[-0.261884    0.57930787 -0.00653143 -2.11461743]


#display the pandas series is empty or not
print scity.empty

#display the dimenstion of the object
print scity.ndim


#display the first value of the pandas series
print scity.head(1)
#0   -0.261884
#dtype: float64

#display the last value of the pandas series
print scity.tail(1)
#3   -2.114617
#dtype: float64


#how many values inside the pandas series
print scity.size 
