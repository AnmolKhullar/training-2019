import numpy as np

a = np.array([1, 2, 3])
print(a.ndim)
a = np.array([(1, 2, 3), (2, 3, 4)])
print(a.ndim)
print(a.itemsize)
print(a.dtype)
a = np.array([1, 2, 3])
print(a.size)
a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a.size)
a = np.array([1, 2, 3])
print(a.shape)
a = np.array([(1, 2, 3), (2, 3, 4)])
print(a.shape)