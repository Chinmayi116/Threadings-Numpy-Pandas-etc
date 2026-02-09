import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr.size)
print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(arr.itemsize)
print(arr.nbytes)
print(arr.T)
for item in arr.flat:
    print(item,end=" ")
print(arr.real)
print(arr.imag)