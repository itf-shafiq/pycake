# Take 10 integers from keyboard using loop and print their average value on the screen.

inputNumber = 10 
sum = 0 
i = 1

while i <=  10:
    number = int(input("Please Enter you numbers: "))
    sum = sum + number 
    i += 1
else:
    print("Total Sum of all numbers is " + str(sum))