""" Problem: 
  
Solution:
"""


""" Problem: 6-7

6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.

Solution:
"""



people01 = {
    "firstName" : "Shafiq",
    "lastName" : "Islam",
    "age" : "25",
    "city" : "cumilla",
    "profession" : "web Developer",
}

people02 = {
    "firstName" : "sumon Molla",
    "lastName" : "salim",
    "age" : "30",
    "city": "barishal",
    "profession" : "senior Software Developer ",
}

people03 = {
    "firstName" : "asif",
    "lastName" : "chowdhury",
    "age": "28",
    "city" : "bogura",
    "profession" : "front-end Developer"
}

peoples = [people01,people02,people03]

for people in peoples:
    fullName = people['firstName'] + " " + people['lastName']
    print("\n" + "Hello! I am " + fullName + "." + " I leave in " + people['city'] + "," 
    + " I am " + people['age'] + " years old." + " And I am professional " + people['profession'])




""" Problem: 6-8
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.  

Solution: Same as previous one " problem 6-7 "
"""

""" Problem: 6-9

  6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.

Solution:
"""




favoritePlaces = {}

places = []

names = []
for i in range(3):
    name01 = str(input("Hey! What's your Name? "))
    names.append(name01)
            

    for j in range(3):
        place = str(input("what's your Favorite Place to travel? "))
        places.append(place)
    
    for name in names:
        if name == names[0]:
            favoritePlaces[name] = places[:3]
        elif name == names[1]:
            favoritePlaces[name] = places[3:6]
        else:
            favoritePlaces[name] = places[6:]


print(favoritePlaces)




# second way to solve this problem with list comprehensive 

names = ['Asraf', 'Nabil', 'XYZ']
 
places = ['1', '2', '3', '4', '5', '7', '7', '8', '9', '10', '7', '12']
 
 
dic = dict()
 
 
for name in names:
    dic[name] = [i for i in places[0:4]]
    # int(len(places) / len(names) can also be used)
    [places.remove(i) for i in places[0:4]]
    # name of 12 places must be unique
   
print(dic)



""" Problem:  6-10
  6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.

Solution:
"""


favorite_number = {
    "shafiq" : [1,5,2],
    "sumon" : [5,8,4],
    "anam" : [9,7,3],

}

for name,numbers  in favorite_number.items():
    print("\n" + name + " your favorite numbers are: " )
    for number in numbers:
        print("\t" + str(number))
        


""" Problem: 6-11
  6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it
Solution:
"""


cities = {
    "dhaka" : {
        "country" : "bangladesh",
        "populations" : "200 milion",
        "fact" : "dhaka is over crowded city ",
    },
    "barlin" : {
        "country" : "germany",
        "populations" : "50 million",
        "fact" : "barlin is beautiful city",
    },
    "silicon-valley" : {
        "country" : " america",
        "populations" : " 70 million",
        "fact" : "silicon valley is mother of tech indrusty ",
    }

}

for city,infos in cities.items():
    print('\n' + city.title() + " is a city of " + infos['country'].title() + ". It has " 
    + infos['populations'].capitalize() + " population" + " and " + infos['fact'].capitalize() )



""" Problem: 
  6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.
Solution:
"""