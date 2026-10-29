"""
reshape(rows, columns) specify new shape
if dimensions match
"""

import numpy as np

arr = np.array( [1,2,3,4,5,6,7,8] )
new_arr = arr.reshape(2,4)
print(new_arr)