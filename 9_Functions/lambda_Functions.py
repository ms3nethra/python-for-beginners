# lambda Functions

# these are mainly used when we need nameless functions for short period of time

def add(a, b):
    return a + b

print(add(3, 4))


c = (lambda a, b : a + b) (3, 4)
print(c, type(c))


func = (lambda a, b : a + b)
print(func(5, 4))


def larger(a, b):
    if a > b:
        return a
    else:
        return b

z = larger(10, 5)
print(z)

l = (lambda x, y : x if x > y else y) (55, 5)
print(l)

large = lambda x, y : x if x > y else y
print(large(66, 6))

lst = [(12, 56), (2, 4), (5, 3)]
lst.sort()
print(lst)


def k(x):
    return x[1]

lst.sort(key = k)
print(lst)