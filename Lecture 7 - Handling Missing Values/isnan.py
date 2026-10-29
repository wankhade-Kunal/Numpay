# No we can not compare it directly
# print(np.nan == np.nan)

import numpy as np

arr = np.array( [1,2,np.nan, 4,np.nan])
print(np.isnan(arr))




