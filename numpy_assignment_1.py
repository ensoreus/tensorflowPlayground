import numpy as np
# Create a 1-dimensional NumPy array using np.array()
a1 = np.array([2,5,3,7,4,2,7,5,4])

# Create a 2-dimensional NumPy array using np.array()
a2 = np.array([[5,4,6,4,3],
               [2,5,3,6,7]])

# Create a 3-dimensional Numpy array using np.array()
a3 = np.array([[3,6,5],[67,43,76],[3,5,4]])

# Attributes of 1-dimensional array (shape, 
# number of dimensions, data type, size and type)
print(type(a1), " ", a1.shape, " ", a1.size, " ", a1.dtype)

# Attributes of 2-dimensional array
print(type(a2), " ", a2.shape, " ", a2.size)

# Attributes of 3-dimensional array
print(type(a3), " ", a3.shape, " ", a3.size)

# Import pandas and create a DataFrame out of one
# of the arrays you've created
import pandas as pd
dfa1 = pd.DataFrame(a1.reshape(1, 9), index=["Values"], columns=["1", "2", "3", "4", "5", "6", "7", "8", "9"])
dfa2 = pd.DataFrame(a2, index = ["Rows", "Cols"])

# Create an array of shape (10, 2) with only ones
ones = np.ones(shape=(10, 2))

# Create an array of shape (7, 2, 3) of only zeros
zeros = np.zeros(shape=(7, 2, 3))

# Create an array within a range of 0 and 100 with step 3
a4 = np.arange(0, 100, 3)

# Create a random array with numbers between 0 and 10 of size (7, 2)
rnd = np.random.randint(0, 10, size=(7, 2))

# Create a random array of floats between 0 & 1 of shape (3, 5)
rndf = np.random.random(size=(3, 5))

# Set the random seed to 42
np.random.seed(42)
# Create a random array of numbers between 0 & 10 of size (4, 6)
rndf1 = np.random.random(size=(4, 6))

# Create an array of random numbers between 1 & 10 of size (3, 7)
# and save it to a variable
rndi1 = np.random.randint(1, 10, size=(3, 7))

# Find the unique numbers in the array you just created
urnd = np.unique(rnd)
# Find the 0'th index of the latest array you created
first=rndi1[0,0]
# Get the first 2 rows of latest array you created
first_two = rndi1[:2,:]
# Get the first 2 values of the first 2 rows of the latest array
first2_first2 = rndi1[:2, :2]
# Create a random array of numbers between 0 & 10 and an array of ones
# both of size (3, 5), save them both to variables
ar1 = np.random.randint(0, 10, size=(3, 5))
ones2 = np.ones((3, 5), "int64")

# Add the two arrays together
ar1 + ones2
# Create another array of ones of shape (5, 3)
ones3 = np.ones((5, 3), "int64")
# Try add the array of ones and the other most recent array together
ones2 + ones3.T
# Create another array of ones of shape (3, 5)
ones4 = np.ones((3, 5), "int64")
# Subtract the new array of ones from the other most recent array
ones4 - ones3.T
# Multiply the ones array with the latest array
print(ones4 * ar1)
# Take the latest array to the power of 2 using '**'
print(ar1 ** 2)
# Do the same thing with np.square()
print(np.square(ar1))
# Find the mean of the latest array using np.mean()
print(np.mean(ar1))
# Find the maximum of the latest array using np.max()
print(np.max(ar1))
# Find the minimum of the latest array using np.min()
print(np.min(ar1))
# Find the standard deviation of the latest array
print(np.std(ar1))
# Find the variance of the latest array
print(np.var(ar1))
# Reshape the latest array to (3, 5, 1)
print(ar1.reshape(3, 5, 1))
# Transpose the latest array
print(ar1.reshape(3, 5, 1).T)
# Create two arrays of random integers between 0 to 10
# one of size (3, 3) the other of size (3, 2)
ar2 = np.random.randint(0, 10, size=(3, 3))
ar3 = np.random.randint(0, 10, size=(3, 2))
# Perform a dot product on the two newest arrays you created
print(ar2, "\n", ar3, "\n", ar2.dot(ar3))
# Create two arrays of random integers between 0 to 10
# both of size (4, 3)
ar4 = np.random.randint(0, 10, size=(4, 3))
ar5 = np.random.randint(0, 10, size=(4, 3))
# Perform a dot product on the two newest arrays you created
print(ar4.dot(ar5.T))
# Take the latest two arrays, perform a transpose on one of them and then perform 
# a dot product on them both

# Create two arrays of random integers between 0 & 10 of the same shape
# and save them to variables
ar6 = np.random.randint(0, 10, size = (5, 3))
ar7 = np.random.randint(0, 10, size = (5, 3))
# Compare the two arrays with '>'
print("ar6:", ar6, "ar7", ar7, ">", ar6 > ar7)
# Compare the two arrays with '>='
print("ar6:", ar6, "ar7", ar7, ">=", ar6 >= ar7)
# Find which elements of the first array are greater than 7
print("ar6:", ar6, "> 7", ar6 > 7)
# Which parts of each array are equal? (try using '==')
print("ar6:", ar6, "ar7", ar7, "==", ar6 == ar7)
# Sort one of the arrays you just created in ascending order
print(np.sort(ar6))
# Sort the indexes of one of the arrays you just created
print(np.argsort(ar6, axis=1))
# Find the index with the maximum value in one of the arrays you've created
print(np.argmax(ar6))
# Find the index with the minimum value in one of the arrays you've created
print(np.argmin(ar6))
# Find the indexes with the maximum values down the 1st axis (axis=1)
# of one of the arrays you created
print(np.argmax(ar6, axis=1))
# Find the indexes with the minimum values across the 0th axis (axis=0)
# of one of the arrays you created
print(np.argmin(ar6, axis=0))
# Create an array of normally distributed random numbers

# Create an array with 10 evenly spaced numbers between 1 and 100
