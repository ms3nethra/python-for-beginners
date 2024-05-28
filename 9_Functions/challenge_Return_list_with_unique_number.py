# challenge 

"""
write a python function thet takes a list and return a new list with unique elements of the first list
input = [1, 2, 3, 1, 2, 4]
output = [1, 2, 3, 4]

"""

lst = [1, 2, 3, 1, 2, 4]

def uniqueElm(li):
    
    new = []
    # iterate on the li list
    for i in li:
        # we are adding only unique elements in new list
        if i not in new:
            new.append(i)

    # return new list
    return new

print(uniqueElm(lst))


