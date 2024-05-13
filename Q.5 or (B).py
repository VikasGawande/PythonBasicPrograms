import pandas as pd
import numpy as np

arr=np.array([22,24,56,56,95])
a=pd.Series(arr)

b=a.unique()
print("Unique Array",b)
print("Max Value in Array",b.max())
print("Min Value in Array",b.min())
