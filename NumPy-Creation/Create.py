import numpy as np  # Import the NumPy library for numerical operations and array manipulation.

# Create a 10-dimensional array using ndmin=10
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], ndmin=10)
# Replace the array with a 3-dimensional array
arr = np.array([[[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [10, 11, 12, 13, 14]]])

print(arr.ndim)  # Print the number of dimensions of the array (expected output: 3).
print(arr)  # Print the content of the array.

# Create a 2x2 array filled with zeros
arr = np.zeros((2, 2))
print(arr)  # Print the 2x2 array filled with zeros.

# Create a 1D array of length 10 filled with zeros
arr = np.zeros([10])
print(arr)  # Print the 1D array filled with zeros.

# Create a 1D array of length 10 filled with ones
arr = np.ones([10])
print(arr)  # Print the 1D array filled with ones.

# Create a 2x3 array filled with uninitialized values (default memory state)
arr = np.empty([2, 3])
print(arr)  # Print the 2x3 array filled with uninitialized values.

# Create a 2x2 array filled with the constant value 5
arr = np.full([2, 2], 5)
print(arr)  # Print the 2x2 array filled with the constant value 5.

# Create a 1D array with 10 evenly spaced values between 10 and 100
arr = np.linspace(10, 100, 10)
print(arr)  # Print the 1D array with evenly spaced values.
