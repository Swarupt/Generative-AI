
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Data:")
print(data)

print("Row-wise Sum:", np.sum(data, axis=1))
print("Column-wise Sum:", np.sum(data, axis=0))
print("Minimum Value:", np.min(data))
print("Maximum Value:", np.max(data))
print("Overall Mean:", np.mean(data))
