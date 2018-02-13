# Tuples cannot be changed
x = 5,2,3,6,9,9,6
y = (2,23,123,23,2,6)

# Lists can be changed
z = [23,213,232,23,2,32]

def exampleFunc():
    return 13,5
x,y = exampleFunc()    

print(z[2])