"""
Modes of opening a file

r - read only
w - write only
a - appending data at the end of file
wt - write text
wb - write binary
rb - read binary
rt - read text

"""

f = open("name.txt")

print(f.read())

##print(f.write("hello"))
print(f.close())


f1 = open("HelloWorld.txt", "w")
f1_write = f1.write("Hi! Hello People")
print(f1_write)
f1.close()
print(f1.closed)
