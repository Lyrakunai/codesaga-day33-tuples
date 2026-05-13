# Day 33 - Tuples Practice

# 1. Basic tuple
student = ("Riya", 23, "Patna")
print("Student Tuple:", student)

# 2. Accessing tuple values
student = ("Riya", 23, "Patna")
print("Name:", student[0])
print("Age:", student[1])

# 3. Single value tuple
single = (5,)
print("Single Tuple:", single)
print(type(single))

# 4. Tuple packing
employee = "Aman", 21, "Python Department"
print("Packed Tuple:", employee)

# 5. Tuple unpacking
employee = "Aman", 21, "Python Department"
name, age, department = employee
print("Department:", department)

# 6. count() method
numbers = (10, 20, 20, 30, 20)
print("Count of 20:", numbers.count(20))

# 7. index() method
numbers = (10, 20, 20, 30, 20)
print("Index of 30:", numbers.index(30))

# 8. Tuple + if condition
marks = ("Sara", 92)
name, score = marks
if score > 90:
    print("Top Performer")
else:
    print("Keep Improving")

# 9. Nested tuple with list logic
data = ([10, 20], [30, 40])
data[0][1] = 99
print("Updated Nested Data:", data)

# 10. Tuple for fixed roles
roles = ("admin", "teacher", "student")
role = "teacher"
if role in roles:
    print("Access Granted")
else:
    print("Access Denied")