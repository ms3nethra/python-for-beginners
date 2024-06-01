"""
with open

- most common way to perform operation on files
- it closes the file after performing operation

"""

with open("name.txt") as f:
    print(f.read())

print(f.closed)

with open("name.txt", "w") as f:
    f2 = f.write("Hey!, i am writable")
    print(f2)

print(f.closed)