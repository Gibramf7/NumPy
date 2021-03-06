import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

#each row represents a student
#each col represents a Test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis =0)
print(g)

h = grades.mean(axis=1)
print("Average of each student", h)


numbers = np.array([1,4,9,16,25,36])

sqrt = np.array(numbers)

print(sqrt)

numbers2 = np.arange(1, 7) * 10

np_add = np.add(numbers, numbers2)

print(np_add)

np_multiply = np.multiply(numbers2, 5)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2,4,6])

np_multiply2 = np.multiply(numbers3, numbers4)

print(np_multiply2)


#Indexing and slicing 

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
# to select a single element we give it the row and the column
a = grades[0,1]

print(a)

b = grades[1]

print(b)
# to select multiple sequential rows, use slice notation
# (rememeber upper limit is not included)
c = grades[0:2]
print(c)



# to select multiple non-squential rows, use a list of row indices:
d = grades[[1,3]]

print(d)
# to get test1 for all students
e = grades[:,0]

print(e)

# to get test1 and test3 for all students

f = grades[:, [0,2]]

print(f)


'''Use NumPy randon-number generator to create an array of twelve random grades
in the range 60 through 100, then reshape the result into a 3X4 array.
Calculate the average of all the grades, the average of the grades for each test 
and the averages of the grades for each student.'''

grades = np.random.randint(60,101,12).reshape(3,4)

print(grades)

avg_all = grades.mean()
print(avg_all)
avg_test = grades.mean(axis=0)
print(avg_test)
avg_student = grades.mean(axis=1)
print(avg_student)

#Shallow copies (view)

numbers = np.arange(1, 6)
print(numbers)
numbers2 = numbers.view()


numbers[1] *= 10

print(numbers2)


#Slice Views
numbers2 = numbers2[0:3]

numbers[1] *= 20

print(numbers2)

# Deep copies
# The array method copy returns a new array object with a deep copy of the original aray
numbers = np.arange(1, 6)
numbers2 = numbers.copy()

numbers[1] *= 10

print(numbers)

print(numbers2)


'''The array methods reshape and resize both enable you to change an array's 
dimensions, Method shape returns a view (shallow copy) of the original array
with the new dimensions. It does not modify the original array
'''

grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1,6)

print(grades)

b = grades.resize(1,6)

print(grades)
print(b)

# produces a deep copy
flattened = grades.flatten()

#produces a shallow copy
raveled = grades.ravel()

raveled[0] = 100

print(grades)

raveled[5] = 99

print(grades)

# Transpose the columns and rows
t = grades.T

print(t)

print(grades)

grades = np.array([[87, 96, 70], [100, 87, 90]])

grades2 = np.array([[87, 96, 70], [100, 81, 82]])

h_grades = np.hstack((grades, grades2))

print(h_grades)
# h stacks adds more columns and v stack adds more rows

v_grades = np.vstack((grades, grades2))

print(v_grades)