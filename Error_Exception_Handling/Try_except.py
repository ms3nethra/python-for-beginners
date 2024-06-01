"""
Try and except
- try - this block handles the error in your code if any of it exits
- except: this book gives the output that you want to show if your code is faulty

"""

a = 5
b = 2

#put the suspect code in try block
try:
    print(a/b)
except:
    print("there is an error that you might want to look for")
    pass
print("Hello World")