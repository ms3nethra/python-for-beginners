# append

l = [1, 2, 3, 4, 5]

l.append("rahul")
print(l)

l.append("2")
print(l)

l1 = [6, 7, 8]
l.append(l1)
print(l)

# extend

l = [1, 2, 3, 4, 5]
l1 = [6, 7, 8]
l.extend(l1)
print(l)


s = "rahul"

for i in s:
    print(i)

l.extend(s)
print(l)