# return

#Return vs Print

def add(a, b):
    c = a + b
    ##print(a, b)
    ##print(c)

    return c

z = add(3, 4)
print(z, type(z))

##print(type(a))


#If no return object then it returns nonetype

def func():
    return

func()

c = func()
print(c, type(c))


# code after return statement doesn't get executed

def func():
    print("Before retuen")
    return "Rahul"
    print("After return")

func()
a = func()
print(a)