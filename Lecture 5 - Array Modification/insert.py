"""
np.insert(array, index, value, axis = None)
array - original array
axis = 0, row-wise , 1 means column-wise
"""

# 1D - Arr
# import numpy as np

# arr = np.array( [1,2,3,4,5,6] )
# print("Before np.insert", (arr))
# new_arr = np.insert(arr,1,30, axis=0)
# print("After np.insert", (new_arr))


# 2D - Arr
import numpy as np

arr_2d = np.array( [ [1, 2], [3,4] ] )
print("Before np.insert -> ", print(arr_2d))
new_arr_2d = np.insert(arr_2d, 1, [7,8], axis=None) # 0 means row , 1 means column
print("After np.insert -> ", (new_arr_2d))