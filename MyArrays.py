# read evaluate print loop (REPL)
import numpy as np

integers = np.array([1, 2, 3])

print(type(integers))
print(integers)


# LIST comprehension
# crate one dimensiional array

integers = np.array([i for i in range(2, 21, 2)])
print(integers)

# multiple dimensional array of integers

integers = np.array([[1, 2, 3], [4, 5, 6]])
print(type(integers))
print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size
print()

for row in integers:
    print(type(row))
    print(row)
    for col in row:
        print(
            col, end=" "
        )  # end on print statemtn changes the new line default to space

# iterating through all value in array
for i in integers.flat:
    print(i)


import random

a = np.array(
    [
        [random.randint(1, 10) for i in range(5)],
        ([random.randint(1, 10) for i in range(5)]),
    ]
)

b = np.array(np.random.randint(1, 10, size=(2, 5)))

shape = a.shape
size = a.size
print(a)
print(b)


c = np.zeros(5)  # create and array of 5 elements of zeors
print(c)
print(np.ones(5))  # create and array of 5 elements of 1s(by default float type)
print(np.ones((2, 4), dtype=int))  # create an array of 2 by 4 of ones of type int

print(np.full((3, 5), 13))  # 3 rows 5 column 13

print(np.arange(5))  # like th erange function using integers

print(np.arange(5, 10))  # include lower limit but not upper limit

print(np.arange(10, 1, -2))  # step value for descending order

print(np.linspace(0.0, 1.0, num=5))  # evenly spaced float range

array1 = np.arange(1, 21)
array2 = array1.reshape(4, 5)

print(array1)
print(array2)


array3 = np.arange(1, 100001).reshape(
    4, 25000
)  # doesn'r dispaly everything in output ... represents there are some data in it
print(array3)


numbers = np.arange(1, 6)

numbers += 10  # adds 10 to each element in the array

print(numbers)


# Broadcasting
print(numbers * 2)
# numbers*[2,2,2,2,2]
print(numbers ** 3)
# numbers is unchanged by arithemetic operators
print(numbers)


# multiplying integer arrays with floating pt arrays(resulting is floating pt)

numbers2 = np.linspace(1.1, 5.5, 5)
a = numbers * numbers2
print(a)


# comparing arrays
print(numbers >= 13)
print(numbers2 < numbers)
print(numbers == numbers2)