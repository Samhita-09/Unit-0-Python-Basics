# LESSON 4 STARTER CODE: VARIABLES AND DATA TYPES

# ========================================
# PART 1: Creating Variables Practice
# ========================================
name = "Samhita"
age = 15
gpa = 3.8
grade = 10

print("Student Name: " + name)
# print("Student Age: " + age) string + integer won't work
print("Student Age:", age)

# variables can change
age = 17
# multiple assignments
subject, period = "CS", 1

# ========================================
# PART 2: Data Types Practice
# ========================================
# Four main (primitive) data types
name = "Samhita" # str(string)
age = 15 # int(integer)
gpa = 3.8 # float(decimal)
is_present = True # bool(boolean)

# Check data types via type() function
print(f"Name: {name} Type: {type(name)}")
print(f"Age: {age} Type: {type(age)}")
print(f"GPA: {gpa} Type: {type(gpa)}")
print(f"Present: {is_present} Type: {type(is_present)}")

# ========================================
# PART 3: Type Conversion Practice
# ========================================
# Convert between types
grade_text = "95"
# grade_text2 = "'95"
print(f"Original: {grade_text} {type(grade_text)}")
grade_number = int(grade_text)
print(f"AS Number: {grade_text} {type(grade_number)}")
gpa_number = float(gpa)
print(f"GPA: {gpa_number} {type(gpa_number)}")
gpa_text = str(gpa_number)
print(f"GPA: {gpa_text} {type(gpa_text)}")

# practice with bool() function
print(f"bool(0) - {bool(0)}") # Falso
print(f"bool(1) - {bool(1)}") # True
print(f"bool(10) - {bool(10)}") # True
print(f"bool('') - {bool('')}") # False
print(f"bool('hi') - {bool('hi')}") # True

# ========================================
# PART 4: Variable Operations Practice  
# ========================================
# Swapping variables
color1 = "red"
color2 = "blue"
color1, color2 = color2, color1
print(f"Color2: {color2}")