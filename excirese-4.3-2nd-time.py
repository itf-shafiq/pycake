print(" # print a serise of number from 1 to 20 ")

for value in range(1,21):
    print(value)

print("# print out 1 to one 1000000 ")

oneMList = list(range(1,1000001))
print(oneMList)

print("# find out a minimum,Maximum and Sum of 1 to 1000000")

print(min(oneMList))
print(max(oneMList))
print(sum(oneMList))

print(" # Make a list of odd numbers from 1 to 20 and print each number using for loop")

for value in range(1,20,2):
    print(value)

print("# Make a list of multiplise of 3 from 3 to 30 ")

threes = list(value*3 for value in range(3,30))
print(threes)

print(" # make a list of cubes of 1 to 10 number serise and print each number using for loops ")

for value in range(1,11):
    print(value**3)

print(" Make a list of cubes of 1 to 10 number serise using comprehension ( make a list of number in one line code)")

cubesList = [ value**3 for value in range(1,11)]

print(cubesList)

print( " Let's see what I have done ")