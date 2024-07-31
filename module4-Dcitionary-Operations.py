# Initialize an empty dictionary
grades = {}

# Assign grades to students using dictionary keys
grades['John'] = 'A-'
grades['Albert'] = 'B'

# Print the dictionary
print(grades)

# Now let's update the grades 
grades.update({'John':'A'})

# Print the dictionary
print(grades)

# Print the length with the grades
print(len(grades))

# Insert "if" John is in grades, print John got whatever the value of grades
if 'John' in grades:
    print('John got:', grades['John'])

del grades['John']
print(grades)

for el in grades:
    print(el)

for el in grades.keys():
    print(el)

for el in grades.values():
    print(el)

for person, grade in grades.items():
    print(person, 'got', grade)