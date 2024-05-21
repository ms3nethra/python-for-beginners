"""
Finding marks of student in a class. Find topper of the class
Consider that list is non empty
"""

marks = [90, 20, 100, 50, 80, 95]

# iterate on the list

highest = marks[0]
for i in marks:
    # check the condition
    if i > highest:
        highest = i

print(highest)


#max function

high = max(marks)
print(high)

#min function
low = min(marks)
print(low)