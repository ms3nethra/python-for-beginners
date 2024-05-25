"""list inbuilt methods
-count
-index
-pop
-remove
-sort
insert
append
extend

"""

bugget = [100, 200, 150, 100]

print(bugget.count(100))

print(bugget.count(500))


#index

print(bugget.index(200))


name = ["rahul" , "Emma", "harry"]
print(name.index("harry"))

#pop

drop = name.pop()
print(drop)


#remove

name.remove("Emma")
print(name)


# sort
bugget.sort()
print(bugget)


# inset

name.insert(1, "Tri")
print(name)