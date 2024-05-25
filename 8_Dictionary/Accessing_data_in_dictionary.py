# Accessing elements
# - Dictionaries doesn't support indexing

# Using key

fruits = {
    "Apple" : 120,
    "Mango" : 100,
    "Pineapple" : 90

}

print(fruits)

print(fruits["Apple"])

print(fruits["Mango"])


# get method: To  avoid error

#fruits.get("Apple")
print(fruits.get("Apple"))