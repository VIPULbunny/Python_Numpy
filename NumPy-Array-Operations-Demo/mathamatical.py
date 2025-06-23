import numpy as np

# Define two 2D arrays
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr2 = np.array([[10, 9, 8, 7, 6], [5, 4, 3, 2, 1]])

# Print the first array
print(arr1)

# Print the second array
print(arr2)

# Element-wise addition of two arrays
print(arr1 + arr2)

# Add 10 to each element of the first array
print(arr1 + 10)

# Element-wise subtraction of the second array from the first array
print(arr1 - arr2)

# Element-wise division of the first array by the second array
print(arr1 / arr2)

# Element-wise division of the first array by itself (resulting in an array of ones)
print(arr1 / arr1)

# Divide each element of the first array by 4
print(arr1 / 4)

# Element-wise exponentiation (first array raised to the power of the second array)
print(arr1 ** arr2)

# Square each element in the first array
print(arr1 ** 2)
