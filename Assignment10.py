import numpy as np

arr = np.arange(1,11)
print("The array is:", arr)

print("Slicing:")
print(arr[0:5:2])

print("Stastical Operations")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:",np.max(arr))
print("Min:", np.min(arr))

print("Broadcasting Operations")
print("Adding 5 to every element in array:", arr + 5)
