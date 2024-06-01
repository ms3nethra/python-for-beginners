"""
Binary data
- to read binary data we open file in "rt" mode
- to write binary data we open file in "wt" mode

"""

with open("monkey.jpg", "rb") as f:
    data = f.read()
    
    with open("monkey01.jpg", "wb") as d:
        d.write(data)
