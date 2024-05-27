# Scope of a variable

"""
two types - global and local

globle variable can be used anywhere in the program

local variable can only be used locally inside a program
"""

# a can be used anywhere in the program

a = 5

def func():
    print(a)

func()
print(a)


b = 5

def func():
    x = 3
    print(x)

func()
print(a)
##print(x)

m = 5

def func():
    m = 50
    print(m)

func()
print(m)


q = 5

def func():
    global q
    q = 20
    print(q)

#print(q)
func()
print(q)


