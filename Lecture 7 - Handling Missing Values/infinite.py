# np.isinf(arr) 10^ 1000
# import numpy as np

# arr = np.array( [1, np.inf, 4, 2, -np.inf])
# print(np.isinf(arr))


# replace infinite value to finite

import numpy as np

arr = np.array( [1, np.inf, 4, 2, -np.inf])
print(np.isinf(arr))

replace_value = np.nan_to_num(arr, posinf=10, neginf=-100)
print(replace_value)