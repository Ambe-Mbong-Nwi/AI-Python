#Convert a binary numpy array (containing only 0s and 1s) to a boolean numpy array

import numpy as np

arr = np.array([0, 1, 1, 1, 0, 1, 0])
print(f"Original array: {arr}")

arr = arr.astype(dtype=bool)
print(f"The corresponding boolean array is: {arr}")
print("We see 0 = False, and 1 = True")