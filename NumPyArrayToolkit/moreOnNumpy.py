import numpy as np

# Define two 2D arrays
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
arr3 = np.array([100, 200, 300])

# Vertical stacking of arr1 and arr2
print(np.vstack((arr1, arr2)))  # Stacks arr2 below arr1

# Horizontal stacking of arr1 and arr2
print(np.hstack((arr1, arr2)))  # Stacks arr2 beside arr1

# Depth stacking of arr1 and arr2
print(np.dstack((arr1, arr2)))  # Stacks arr2 behind arr1

# Split arr1 into 2 parts
print(np.array_split(arr1, 2))  # Splits arr1 into two sub-arrays

# Split arr1 into 10 parts (some empty)
print(np.array_split(arr1, 10))  # Splits arr1 into 10 sub-arrays (some will be empty)

# Define a new array for searching and sorting
newarr = np.array([10, -5, 0, 20, 15, -20, 30])

# Search for elements equal to 20
print(np.where(newarr == 20))  # Returns indices where elements are 20

# Search for elements greater than 4
print(np.where(newarr > 4))  # Returns indices where elements are greater than 4

# Sort the array in ascending order
print(np.sort(newarr))  # Sorts newarr in ascending order

# Sort the array in descending order
print(np.sort(newarr)[::-1])  # Sorts newarr in descending order

# Define a 1D array for resizing
a = np.arange(12)

# Resize the array to a 3x5 array
print(np.resize(a, (3, 5)))  # Resizes array 'a' to 3x5, filling with repeated elements

# Delete element at index 1 from newarr
print(np.delete(newarr, 1))  # Deletes the element at index 1

# Delete the second row from arr1
print(np.delete(arr1, 1, axis=0))  # Deletes the second row of arr1

# Calculate LCM of 12 and 20
print(np.lcm(12, 20))  # Returns the LCM of 12 and 20

# Define another array for LCM and GCD calculations
arr4 = np.array([2, 4, 6, 8, 10])

# Calculate the LCM of all elements in arr4
print(np.lcm.reduce(arr4))  # Returns the LCM of all elements in arr4

# Calculate the GCD of 16 and 32
print(np.gcd(16, 32))  # Returns the GCD of 16 and 32

# Calculate the GCD of all elements in arr4
print(np.gcd.reduce(arr4))  # Returns the GCD of all elements in arr4
