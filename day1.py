import numpy as np
import pandas as pd

a1 = np.array([1, 2, 3])

a2 = np.array([[1, 2, 3],
               [4, 5, 6]])

a3 = np.array([[[ 1, 2, 3],
                [4, 5, 6],
                [3, 5, 7]],
               [[7, 8, 9],
                [10, 11, 12],
                [3, 6, 33]],
               [[13, 14, 15],
                [16, 17, 18],
                [21, 4, 2]]])

df = pd.DataFrame(a2)

ones = np.ones((2, 3))
zeros = np.zeros((3, 3), "float32")
range_array = np.arange(0, 10, 2)
randfloat_array = np.random.random((5,3))
randfloat_array2 = np.random.rand(5, 3)

np.random.seed(5)
rar3 = np.random.rand(3, 3)

np.unique(a3)


rar4 = np.unique(randfloat_array)

ar1 = np.array([2, 3, 5, 3, 2, 3, 1, 2])
rar5 = np.unique(ar1)


a5 = np.random.randint(10, size = (2, 3, 4, 5))


