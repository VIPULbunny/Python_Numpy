import numpy as np

# Define a 2D NumPy array
statarray = np.array([[20, -9, -40], [0, 10, -1], [7, 6, 34]])

# Find the maximum value in the entire array
print(np.max(statarray))  # Output: 34

# Find the maximum values along each column
print(np.max(statarray, axis=0))  # Output: [20 10 34]

# Find the minimum value in the entire array
print(np.min(statarray))  # Output: -40

# Find the minimum values along each column
print(np.min(statarray, axis=0))  # Output: [ 0 -9 -40]

# Find the minimum values along each row
print(np.min(statarray, axis=1))  # Output: [-40 -1 6]

# Calculate the sum of all elements in the array
print(np.sum(statarray))  # Output: 27

# Calculate the sum of elements along each column
print(np.sum(statarray, axis=0))  # Output: [27 7 -7]

# Find the index of the maximum value in the entire array
print(np.argmax(statarray))  # Output: 8

# Find the indices of the maximum values along each column
print(np.argmax(statarray, axis=0))  # Output: [0 1 2]

# Find the index of the minimum value in the entire array
print(np.argmin(statarray))  # Output: 2

# Find the indices of the minimum values along each column
print(np.argmin(statarray, axis=0))  # Output: [1 0 0]

# Define a 1D NumPy array with float values
arr = np.array([-1.7, -4.2, 4.6, -0.87])

# Apply the ceiling function to round up each element
print(np.ceil(arr))  # Output: [-1. -4. 5. -0.]

# Apply the floor function to round down each element
print(np.floor(arr))  # Output: [-2. -5. 4. -1.]

# Define another 2D NumPy array
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Iterate over each element in the second row of the array
for i in np.nditer(arr1[1]):
    print(i)  # Output: 6 7 8 9 10
