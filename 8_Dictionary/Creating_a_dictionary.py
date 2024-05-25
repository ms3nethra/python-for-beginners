# dictionary

d = {}
print(type(d))
print(d)

d1 = dict()
print(type(d1))
print(d1)


fruits = {
    "apple" : 120,
    "mango" : 100,
    "pineapple" : 90
}

print(type(fruits))
print(fruits)


# zip

name = ["apple", "Mango", "Oranges"]
prices = [120, 100, 130]
fruits2 = dict(zip(name, prices))
print(fruits2)
print(len(fruits2))