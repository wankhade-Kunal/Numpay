# Uses:- extracting subset of data
"""
Slicing
array[start:stop:step]

negative step, -1 reverse
"""

import numpy as np

arr = np.array( [10,20,30,40,50,0] )
print(arr[1:5]) #index 1 to 4
print(arr[:4]) #index 0 to 3
print(arr[::2]) #every second ele
print(arr[::-1]) # reverse array