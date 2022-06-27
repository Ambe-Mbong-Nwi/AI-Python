#using numpy create 2 arrays and perform sorting on them , multiplication, addition and divison

import numpy as np

arr1 = np.array([10,3,4,7,1,2])
arr2 = np.array([20,13,17,11,14,15])

print(np.sort(arr1))
print(np.sort(arr2))

print(np.add(arr1,arr2))

print(np.multiply(arr1,arr2))

outputarr = arr2/arr1
print(outputarr)
