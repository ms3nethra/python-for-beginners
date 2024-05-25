"""
Deleting Data

- pop 
- popitem
- del

"""

fruits = {
    "Apple" : 120,
    "Mango" : 100,
    "Pineapple" : 90

}

print(fruits)



# Citizenship check

print("Apple" in fruits)

print("Grapes" in fruits)


# dict.pop(key)

fruits.pop("Apple")
print(fruits)


# # dict.popitem()

fruits.popitem()
print(fruits)



# del object

del fruits

print(fruits)