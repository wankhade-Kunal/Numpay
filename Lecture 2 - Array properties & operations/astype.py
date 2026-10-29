# Uses:- Conversion int -> float, float ->int, str -> float, int

import numpy as np
arr = np.array([1.2, 2.5, 6.7])
new_arr = arr.astype(int)

print(new_arr)
print(new_arr.dtype)