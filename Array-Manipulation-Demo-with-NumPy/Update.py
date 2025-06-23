import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
# Print the 1D array
print(arr)

# Create a 2D array
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Print the 2D array
print(arr1)

# Access and print the element at the 2nd row, 3rd column of arr1
print(arr1[1, 2])

# Create another 2D array
arr2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Create a 3D array
arr3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
# Print the 3D array
print(arr3)

# Access and print the element at the 1st layer, 2nd row, and 3rd column of arr3
print(arr3[0, 1, 2])

# Modify the value at the 1st layer, 2nd row, 3rd column of arr3
arr3[0, 1, 2] = 777
# Print the modified 3D array
print(arr3)

# Print a slice of the 3D array, showing the first two elements in the 1st layer, 2nd row
print(arr3[0, 1, 0:2])
