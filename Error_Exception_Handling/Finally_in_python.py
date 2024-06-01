"""
Finally

- this block will be excecuted in any case
- it is helpful when you want to de-allocate resources
- like closing a file, or db connection

"""

a = 5
b = 0

try:
    print("open file")
    print(a/b)
    print("close file")

except Exception as e:
    print("Error..", e)

finally:
    print("close file")