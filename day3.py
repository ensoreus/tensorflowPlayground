import numpy as np
import pandas as pd
import matplotlib as pl

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



mat1 = np.random.randint(10, size=(5, 3))
mat2 = np.random.randint(10, size=(5, 3))


# matrixmultiplication.xyz

mat3 = np.dot(mat1.T, mat2)


# Nut sales

np.random.seed(0)
sales_amount = np.random.randint(20, size=(5, 3))

sales_weekly = pd.DataFrame(sales_amount,
                            index = ["Mon", "Tue", "Wen", "Thirs", "Fri"],
                            columns = ["Almund Butter", "Peanut butter", "Cashew Butter"])


#Prices

prices = np.array([10, 8, 12])
butter_prices = pd.DataFrame(prices.reshape(1, 3),
                             index = ["Price"],
                             columns = ["Almund butter", "Peanut", "Cashew"])

total_sales = prices.dot(sales_amount.T) # pure np array

#daily_sales = butter_prices.dot(sales_weekly.T)

# Image read

from matplotlib.image import imread
cat = imread("covered_cat.jpg")


