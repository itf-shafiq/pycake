# Make a list of numbers from 1 to 20 using for loop 

for twenty in range(1,21):
    print(twenty)


# Make a list of numbers from 1 to 1000000 and the find out minimum,maximum and sum of those numbers 

milionList = list(range(1,1000001))

len((milionList))
print(min(milionList))
print(max(milionList))
print(sum(milionList))

print("\n" + " I am still alive ")

# Making a list of odd numbers from 1-20 using for loop 

for oddNumbers in range(1,21,2):
    print(oddNumbers)

# making a list of mulitiplies of 3 from 3-30 
threes = list( value*3 for value in range(3,30))
print(threes)

# second way of previous task 
therees01 = []
for value in range(3,30):
    therees01.append(value*3)

print(therees01)

# Print out of cubes of 1 to 10 

for value in range(1,11):
    print(value**3)

# making alist of cubes from 1 to 10  using comprehension (make a list of number in one line of code)

cubeList = [ value**3 for value in range(1,11)]
print(cubeList)




