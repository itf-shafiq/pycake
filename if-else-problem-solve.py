# Problem-01:  Take two int values from user and print greatest among them.

'''print("Enter First Value")
value01 = int(input())

print("Enter Second Value")

value02 = int(input())

if value01 > value02:
    print("First Value is greater then Second")
else:
    print("Second value is greater then first value")'''

'''# Problem-02  
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''
'''discountAmonut = 10/100 

oneUnit = 100 

print("How many Unite Do yo want? ")
requiredUnite = input()

if int(requiredUnite) >= 1000:
     totalprice = int(requiredUnite)*100 
     totalprice = totalprice - (totalprice*discountAmonut)
     print("Your Total cost is: " + str(totalprice))
else:
    totalprice = int(requiredUnite)*100
    print("Your total cost is: " + str(totalprice))'''


'''problem-03 
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
'''
'''print("How much is your salary? ")
salary = input()

print("How many year you have served?")

serviceYear = input()

if int(serviceYear) >= 5:
    bonus = int(salary)*.05
    print("Your Bonus is: " + str(bonus) + " Taka" )
else:
    print("Sorry! you are not elegable for bonus")
'''


''' Problem 04
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''

'''print("how much you have got in this exam: ")
results = int(input())

if results < 25:
    print("Sorry! you have faild ")
elif results <= 45 :
    print("You have got 'E' in this Exam") 
elif results <= 50:
    print("You have got 'D' in this Exam")
elif results <= 60 :
    print("You have got 'C' in this Exam")
elif results <= 80:
    print("You have got 'B' in this Exam")
elif results > 80 :
    print("You have got 'A' in this Exam")
'''


# Problem-05 Take input of age of 3 people by user and determine oldest and youngest among them.


age01 = int(input("First person age: "))


age02 = int(input("Second person age: "))


age03 = int(input("Third person age: "))

if age01 >= age02 and age01 >= age03:
    print("1st person is most older")
elif age02 >= age01 and age02 >= age03:
    print("2nd Person is most older")
elif age03 >= age01 and age03 >= age02:
    print("3rd person is most older")
else:
    print("You enter wrong number")


