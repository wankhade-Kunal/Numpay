import numpy as np

arr = np.array( [1,2,np.nan, 4,np.nan])
change_val = np.nan_to_num(arr,nan=20)
print(change_val)
