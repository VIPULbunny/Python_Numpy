import numpy as np

# Solving a system of linear equations
# 3x + y = 9
# x + 2y = 8
a = np.array([[3, 1], [1, 2]])  # Coefficient matrix
b = np.array([9, 8])            # Constants vector

# Solve the linear equations and print the solution for x and y
print(np.linalg.solve(a, b))  # Output: [2. 3.]

# Solving a quadratic equation
# x^2 + 4x + 4 = 0
coeff = [1, 4, 4]  # Coefficients of the quadratic equation

# Find the roots of the quadratic equation
print(np.roots(coeff))  # Output: [-2. -2.]

# Calculating the mean and weighted mean
array = np.array([1, 2, 3, 4])  # Define an array of values
weight = np.array([4, 3, 2, 1])  # Define weights for the values

# Calculate and print the mean of the array
print(np.mean(array))  # Output: 2.5

# Calculate and print the weighted average of the array
print(np.average(array, weights=weight))  # Output: 2.0
