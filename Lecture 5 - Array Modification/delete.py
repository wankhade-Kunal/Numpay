# np.delete(arr, index, axis = None)

# delete 1D Array
# import numpy as np
# arr = np.array( [10, 20, 30, 40] )
# print("Before np.delete: ", (arr))
# new_arr = np.delete(arr,0)
# print("After np.delete: ", (new_arr))


# delete 2D Array
import numpy as np
arr_2d = np.array( [ [1,2,3], [4,5,6] ] )
print("Before np.delete for 2D arr :", (arr_2d))

new_arr_2d = np.delete(arr_2d,0, axis = 0)
print("After np.delete for 2D arr :", (new_arr_2d))