"""
Updating a Dictionary
- using key
- update

"""



fruits = {
    "Apple" : 120,
    "Mango" : 100,
    "Pineapple" : 90

}

# updating the exiting value

print(fruits)

print(fruits["Pineapple"])

fruits["Pineapple"] = {"small" : 90, "large" : 120}

print(fruits)

fruits["Banana"] = 80
print(fruits)


#update

new = {"grapes" : 120, "oranges" : 70, "berry" : 140}
fruits.update(new)

print(fruits)