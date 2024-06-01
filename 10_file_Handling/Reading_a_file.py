"""
Read
- using read() method we can read a file
- it opens in read only for

"""

with open("new.txt") as f:
    data = f.read()
    print(data)


"""
read() : reads the whole data
read(l) : reads data of the length l
tell() : tells you about the position of the file handle
seek() : it helps to re position your file handle
readlines() : reads data lines by line


"""
with open("new.txt") as f:
    # reading firet 4 chr
    data = f.read(4)
    print(data)
    print(f.tell())
    # next 10 chr
    data = f.read(10)
    print(data)

    #tell() : tells you about the position of the file handle
    print(f.tell())


    #seek() : it helps to re position your file handle
    f.seek(2)
    print(f.tell())

    print(f.read())

with open("new.txt") as f:
    
    data = f.readlines()
    print(data)

    for i in data:
        print(i)
