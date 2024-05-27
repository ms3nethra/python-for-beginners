# Returning multiple values

def intro(name, age, hobby):
    return name, age, hobby

c, d, e = intro("Rahul", 25, "Travelling")

print(c, d, e)

c = intro("Rahul", 25, "Travelling")

print(c, type(c))
