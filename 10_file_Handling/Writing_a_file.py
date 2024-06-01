"""
Writing in a file

- you can write both text and binary file
- you can either write or append in a file

"""
# we are creating a new file
with open("new.txt", "w") as f:
    f.write("Hey, new file created")

# we in existing file

with open("new.txt", "w") as f:
    f.write("this is the updated content of our file\n")
    f.write("this is the new line")