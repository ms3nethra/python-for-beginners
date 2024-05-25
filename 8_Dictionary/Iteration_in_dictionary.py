# Iteration in dictionary 


fruits = {
    "Apple" : 120,
    "Mango" : 100,
    "Pineapple" : 90,
    "Grapes" : 120

}

for i in fruits:
    print(i)


for i in fruits:
    print(fruits[i])
    print(i, fruits[i])


# using dict.items()

for key, value in fruits.items():
    print(key, value)


