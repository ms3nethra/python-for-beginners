# Arbitrary arguments

"""
- when number of values you want to pass is not know
- like we pass multiple values in print functions
- the values are being stored in tuple
"""


def test(*args):
    print(args)
    print(type(args))

    for i in args:
        print(i, end= " ")
        print(i * i, end= " ")


test(2, 3, 4)