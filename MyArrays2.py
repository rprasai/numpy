import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# ROWS - grades for each student
# COLS - grades for each test
a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(
    axis=0
)  # calculate the mean based on the axis so its giving by test/column avg of each test
print("Avg of each test", g)

h = grades.mean(
    axis=1
)  # calcualte the mean based on the axis so its giving avg of each student
print("Avg of each student", h)

numbers = np.array([1, 4, 9, 16, 25, 36])
sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1, 7) * 10
add = np.add(numbers, numbers2)
print(add)

multiply = np.multiply(numbers2, 5)
print(multiply)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])
multiply2 = np.multiply(numbers3, numbers4)
print(multiply2)
"""This works because numbers4 has the same length as each row of numbers3, so Numpy can apply th multiply
operation by treating numbers4 as if it were the following array:
array([[2,4,5],[2,4,6]])"""

# Indexing and Slicing
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

a = grades[0, 1]
print(a)

b = grades[1]
print(b)

# select multiple sequential rows

fisrttworows = grades[0:2]  # doesn't include upper limit
print(fisrttworows)


# select multiple non-sequential rows

c = grades[[1, 3]]  # second element and fourth element
print(c)

# all rows and only first column
d = grades[:, 0]
print(d)
d = grades[:2, 0]
print(d)

d = grades[:, 1:3]
print(d)


# or specific columns using a list of column indices:

c = grades[:, [0, 2]]
print(c)

import random

grade = np.array([random.randint(60, 101) for i in range(12)])
regrade = grade.reshape(3, 4)
grade = np.random.randint(60, 101, 12).reshape(3, 4)

avgallgrades = grade.mean()
print(avgallgrades)

avgpertest = grade.mean(axis=0)
print(avgpertest)

avgperstudent = grade.mean(axis=1)
print(avgperstudent)
print(grade)


# shallow copies (view of original array)
numbers = np.arange(1, 6)
numbers2 = numbers.view()

numbers[1] *= 10

print(numbers2)

numbers2[1] /= 10
print(numbers)

# slice views
# slices also create views. Let's make numbers2 a slice that views only the first
# three elements of numbers:

numbers2 = numbers[0:3]

# to verify it is a view, lets modify an element in the original array and see
# the view array

numbers[1] *= 20

print(numbers2)


# Deep Copies(copy)
# the array method copy return a new array object with deep
# copy of the origina array

numbers = np.arange(1, 6)
numbers2 = numbers.copy()

numbers[1] *= 10
print(numbers)  # numbers get modified but numbers2 remains the same
print(numbers2)

"""the array mehtods reshape and resize both enable youy to change an array's dinensions. 
Method reshapy returns a view (shallow copy) of the original array with the new dimensions.
It does not modify the original array:"""

grades = np.array([[87, 96, 70], [100, 87, 90]])
a = grades.reshape(1, 6)
print(a)
print(grades)


b = grades.resize(1, 6)
print(grades)

# MEthod flatten deep copies the original array's data:
grades = np.array([[87, 96, 70], [100, 87, 90]])
flatten = grades.flatten()

# alternatively, Method ravel produces a view (shallow copy) of the original array.
# which shares the grades array's data:
grades = np.array([[87, 96, 70], [100, 87, 90]])
raveled = grades.ravel()

raveled[0] = 100
raveled[5] = 99

print(grades)


grades = np.array([[87, 96, 70], [100, 87, 90]])
transposed = grades.T
print(transposed)

# horizontal stacking or verticle stackig or adding rows or columns

grades = np.array([[87, 96, 70], [100, 87, 90]])
grades2 = np.array([[87, 96, 70], [100, 87, 90]])

h_grades = np.hstack((grades, grades2))
print(h_grades)

print(grades)

v_grades = np.vstack((grades, grades2))
print(v_grades)
print(grades)