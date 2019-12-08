# Making a number serise using range
for value in range(1,6):
    print(value)

# Making a list using range function

numbers = list(range(1,6))
print(numbers)

# Making a list of even numbers using range function
evenNumber = list(range(2,11,2))
print(evenNumber)

# making a list of even number using range  again

evenNumber02 = list(range(1,11,2))
print(evenNumber02)

evenNumber03 = list(range(0,11,1))
print(evenNumber03)

# Making a list of squares of 1 to 10 using range function 

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# Making a list of squares of 1 to 10 in less code

squares01 = []
for ami in range(1,11):
    squares01.append(ami**2)
print(squares01)

# finding minimum,maximum and sum of a numariac list 

random = list(range(1,10))

print(random)

print(min(random))
print(max(random))
print(sum(random))

# making a list of squares from 1 to 10 using single line of code

squares02 = [ value**3 for value in range(1,11)]

print(squares02)



