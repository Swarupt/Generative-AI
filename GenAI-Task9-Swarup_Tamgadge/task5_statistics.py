
import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))
print("Minimum Marks:", np.min(marks))
print("Maximum Marks:", np.max(marks))

marks_range = np.max(marks) - np.min(marks)
print("Range:", marks_range)
