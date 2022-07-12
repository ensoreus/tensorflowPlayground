import numpy as np
import pandas as pd

ones = np.ones(3)

power_a2 = np.square(a2)
power_a3 = a2 ** 2

sum = a2 + ones

exponent_a2 = np.exp(a1)

modulo = a2 % 2



## Aggregation

listy_list = [1, 2, 3]
listy_sum = np.sum(listy_list)

massive_array = np.random.random(100000)


hi_var_array = [10, 100, 400, 1000, 10000]
low_var_array = [2, 4, 6, 8, 10]
import matplotlib.pyplot as plt
plt.hist(low_var_array)
plt.show()


hmean = np.mean(hi_var_array)
lmean = np.mean(low_var_array)


