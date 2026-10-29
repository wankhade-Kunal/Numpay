# np.concatenate ( (arr1, arr2 ), axis = 0)

import numpy as np

arr1 = np.array( [1,2,3] )
arr2 = np.array( [4,5,6] )
print("Before np.concatenate",(arr1,arr2))
new_arr = np.concatenate( (arr1, arr2) )
print("After np.concatenate",(new_arr))