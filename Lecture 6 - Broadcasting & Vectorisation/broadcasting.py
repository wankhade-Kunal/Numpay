# import numpy as np

# prices = np.array( [100, 20, 300] )
# discount = 10

# final_prices = prices - (prices * discount/100)
# print(final_prices)


# Broadcasting on single element
# import numpy as np

# arr = np.array( [100, 20, 300] )
# result = arr * 2
# print(result)


# 1D array to 2D
# import numpy as np
# matrix = np.array( [ [1,2,3], [4,5,6] ] ) # 2D array
# vector = np.array( [10,20,30] ) # 1D array

# result = matrix + vector
# print(result)


# Incompetable size (error comes)
# import numpy as np

# arr1 = np.array( [ [1,2,3], [4,5,6] ] ) #shape (2,3)
# arr2 = np.array( [1,2] ) #shape (2,)
# arr2 = arr2.reshape(2,1)
# print(arr2)

# result = arr1 + arr2
# print(result)



# Vectorization
# Addition
# import numpy as np

# arr1 = np.array( [1,2,3] )
# arr2 = np.array( [4,5,6] )
# result = arr1 + arr2
# print(result)

# Multiplication

import numpy as np
arr = np.array( [10,20,30] )
result = arr * 3
print(result)