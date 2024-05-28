# challenge

"""
write a python function to print the even numbers from a given list

input - [1, 2, 3, 4, 5, 6]
output - 2, 4, 6

"""

def evenNum(li):

    # iterarte on the list li
    for i in li:
        #check for even elements
        if i % 2 == 0:
            print(i)

lst = [1, 2, 3, 4, 5, 6]

print(evenNum(lst))

