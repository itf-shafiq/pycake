'''
You've finished eating at a restaurant, and received this bill:
Cost of meal: $44.50
Restaurant tax: 6.75%
Tip: 15%
You'll apply the tip to the overall cost of the meal (including tax).'''

mealCost = 44.50 
tax = 6.75/100
tip = 15/100

totalcost = (mealCost + (mealCost*tax))
totalcost = (totalcost+ (totalcost*tip))

print("Your Total bill is: " + str(totalcost) + "$")


