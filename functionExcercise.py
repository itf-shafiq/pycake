#1. Write a Python function to find the Max of three numbers.
"""
def FindMax(a,b,c):
    if a < b & b > c :
        print("Max Number is B = " + str(b))
    elif a > b & a > c:
        print("Max Number is A = " + str(a))
    elif c > a & b < c:
        print(" Max Number is C = " + str(c))
    

FindMax(55,12,25)"""

def max_of_two(x,y):
    if x > y:
        return x
    else:
        return y

"""def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))

maxed_value = max_of_three(55,85,45)
print(maxed_value)"""

def max_of_four(x,y,z,a,b):
    return max_of_two(b,max_of_two(max_of_two(x,y),max_of_two(z,a)))

print(max_of_four(25,18,10,9,122))

    


# Write a Python function to sum all the numbers in a list. 
#Sample List : (8, 2, 3, 0, 7)

