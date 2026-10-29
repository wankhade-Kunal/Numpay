"""
.ravel() -> return view (modifiy original array)
.flatten() -> return copy (return copy of the array)
"""

import numpy as np

arr_2d = np.array( [ [1,2,3], [4,5,6] ] )
print(arr_2d.ravel())
print(arr_2d.flatten())