"""
Challenge

Take an input and find the freq of each letter and return the letter and their freq

example - " Thrinethra"



"""

d = {"T" : 1, "T" : 3}
print(d)


name = "Thrinethra"

for i in name:
    print(i)

freq = {}
for i in name:
    #check for presence
    if i not in freq:
        freq[i] = 1
        #check present increment the freq by factor of 1
    else:
        freq[i] += 1

print(freq)
