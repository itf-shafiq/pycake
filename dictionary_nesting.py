
# put a dictionary's in a list: 

alion_0 = {"color": "green","points": 5}
alion_1 = {"color": "red", "points": 15}
alion_2 = {"color": "yellow", "points": 10}

alions = [alion_0,alion_1,alion_2]

for alion in alions:
    for color,point in alion.items():
        print("\n" + "color: " + color + "\n" + "points: " + str(point))


# Make a list a alions automatically using rang function 


# Make a alion list inside a dictionary using for loop and range function: 

alions = []

for alion_number in range(30):
    if alion_number%2 == 0:
        new_alion = {"color": "yellow","points": 10, "speed": "medium"}
        alions.append(new_alion)
    else:
        new_alion = {"color": "green","points": 5, "speed": "slow"}
        alions.append(new_alion)

for alion in alions[:5]:
    print(alion)

# show the total number of alion added to the alions list

print("\n" + "Total " + str(len(alions)) + " has been created and added")




# Make alion list inside a dictionary using while loop and range function:

n = 0 
alions = []
while n <= 30:
    n += 1
    if n%2 == 0:
        new_alion = {"color": "green","points": 5, "speed": "slow"}
        alions.append(new_alion)
    elif n == 8 or n == 9 or n == 14 or n ==  15 or n == 19:
        new_alion1 = {"color": "yellow","points": 10, "speed": "medium"}
        alions.append(new_alion1)
    else:
        new_alion2 = {"color": "red","points": 15, "speed": "fast"}
        alions.append(new_alion2)




print(alions[7],alions[8],alions[13],alions[14],alions[18])

for alion in alions:
    print(alion)
    




# Add a list into a dictionary 

# store information about a pizza being ordered 

pizza = {
    "curst": "thick",
    "toppings": ['mushrooms','extra cheess','extra chilis']
}

print("\n" + "You have ordered a " + pizza['curst'] + "-crust pizza with: ")

for topping in pizza['toppings']:
    print('\t' + '\t' + '\t' + '\t' + "-" +topping)
    




# Make a dictionary for favorite languages of people where each people might have multiple favorite choice

favorite_languages = {
    "sarah": ['python'],
    "sumon": ['php','javascript'],
    'mafinar': ['python','dart','goLang'],
    'marteen': ['python','shell scripts','c++']

}

for name,languages in favorite_languages.items():
    print("\n" + name + "'s favorite Languages are: ")

    for language in languages:
        print("\t" + "-" + language)



# Make a dictionary where its items also a dictionary lets call it dic dic :D 

users = {
    "its-shafiq": {
        "fastName" : "shafiq",
        "lastName" : "islam",
        "email" : "itf.shafiq@gmail.com",
        "password" : "AbCdEf123",
    },
    "sms-sumon" : {
        "fastName" : "sumon",
        "lastName" : "salim",
        "email" : "sms@gmail.com",
        "password" : "SmS123456",
    },
}

for user,info in users.items():
    print("\n" + "Your user name is: " + user + " - and your informations are: ")

    fullName = info['fastName'] + " " + info['lastName']

    print("\t" + "your name is: " + fullName )
    print("\t" + "Your Email address is: " + info['email'])
    print("\t" + "Your Password is : " + info['password'])
