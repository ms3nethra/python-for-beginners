#Default Arguments
# giving default values to the parameters
# for these parameters passing value in arguments in optional

def intro(name, hobby = "Reading"):
    print("hey my name is", name)
    print("And my hobby is", hobby)

intro("Rahul")

intro("Prateek", "Swimming")