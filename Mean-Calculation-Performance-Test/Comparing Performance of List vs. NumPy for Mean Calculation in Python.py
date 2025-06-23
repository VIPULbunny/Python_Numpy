import numpy as np
import time

# Generate a large 1D array of 100 million random floats between 0 and 1
a = np.random.rand(100000000)

# Calculate the mean using Python's built-in sum and len functions
start = time.time()  # Record start time
mean_list = sum(a) / len(a)  # Calculate mean
print(time.time() - start)  # Print the time taken

# Calculate the mean using NumPy's optimized mean function
start = time.time()  # Record start time
mean_numpy = np.mean(a)  # Calculate mean
print(time.time() - start)  # Print the time taken

# Print the version of NumPy being used
print(np.__version__)