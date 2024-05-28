"""
Keyword arguments
"""


def intro( **kwargs ):
    print(kwargs)
    print(type(kwargs))

    for key, values in kwargs.items():
        print(key, values)

intro(name = "Rahul", age = 25)

intro(name = "Rahul", age = 25, hobbies = ["Swimming", "Read", "Cycling"])



def mix(a, b, c,age = 25, *args, **kwargs):
    print(a, b, c)
    print(age)
    print(args)
    print(kwargs)

mix(2, 4, 5, 45, 6, 8, 9, name="rahul", hobby="swimming")