
import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

sorted_marks = np.sort(marks)

print("Sorted Marks:", sorted_marks)

print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))

average = np.mean(marks)

above_average = marks[marks > average]

print("Average Marks:", average)
print("Marks Above Average:", above_average)
print("Number of Students Above Average:", len(above_average))
