# Stacking
# Vertically = vstack() row wise
# Horizontally = hstack() column wise

# import numpy as np

# arr1 = np.array( [1,2,3] )
# arr2 = np.array( [4,5,6] )

# print(np.vstack( (arr1, arr2 ) ) )
# print(np.hstack( (arr1, arr2 ) ) )


# Spliting
# np.split() for equal split
# np.hsplit() for horizontal split
# np.vslipt() for vertical split

import numpy as np

arr = np.array( [10,20,30,40,50,60] )
print(np.split(arr,2))
print(np.hsplit(arr,3))
# print(np.vsplit(arr,2))