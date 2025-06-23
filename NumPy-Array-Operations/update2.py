import random as r
import numpy as np

# Create a 2D array with random integers between 10 and 500
arr1 = np.random.randint(10, 500, size=(3, 4))
print(arr1)

# Generate 20 linearly spaced numbers between 10 and 500
arr1 = np.linspace(10, 500, 20)
print(arr1)

# Create a 1D array with 63 random float numbers between 0 and 1
arr1 = np.random.rand(63)
# Reshape the 1D array into a 7x9 2D array
arr1 = np.reshape(arr1, (7, 9))
print(arr1)

# Create a 2D array
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 3, 5, 7]])

# Create two 1D arrays
arr2d = np.array([15, 16, 17, 18])
arr1d = np.array([10, 11, 12, 13])

# Append arr2d to arr1d along the first axis (row-wise)
print(np.append([arr1d], [arr2d], axis=0))
