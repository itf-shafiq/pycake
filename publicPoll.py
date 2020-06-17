# all poll result will be sorted in a dictionary 
# 1st I will ask people name 
# 2nd I will ask them for there favorite language
# all favorite language will be sotored in a list for that we need to start program with empty list
#3rd I will repeat this process until someone enter word q for quite 
# if some one enter quite then I will break the loop and print out poll result for each people  
"""
allPollResult = {}
pollResult = []

def poll(k,*pollResult):
    for name,language in allPollResult.items():
     return ("\n" + name + ":" + " Your Favorite Language is: " + "'" + language + "' ;")
        
while True:
    k = str(input("What is your name? ").lower())

    if k == "q":
        break

    active = True
    while active:
        pollResult = str(input("What is your favorite Language? ").lower())

        if pollResult == 'done':
            break
    
    allPollResult[k] = pollResult



public_result = poll(k,pollResult)
print(public_result)"""

# k = str(input().lower())

names = []
favorite_languages = []
poll_result = {}

count = 0

def poll(name,*favorite_language):
    # for name,languages in poll_result.items():
    #     print( "\n" + "hey! " + name + "your favorite Languages are ")
    #     for language in languages:
    #         print("\t" + "-" + language)

    print(poll_result)

active = True

while active:
    print("Hello! Welcome to favorite language poll")
    name = input("what is your name? ").lower()
    names.append(name)


    active01 = True

    while active01:
        # print("Write 'done' when you your answer is finish")
        favorite_language = input("what is your favorite language? ").lower()
        favorite_languages.append(favorite_language)
        
        # ask user if they had any other language choice
        yes_or_not = input("Do you have any other favorite language? write 'yes' or 'no' ").lower()

        # if yes_or_not == 'yes' or yes_or_not == 'no':

            # if user had more then one language choice then run this loop
        while yes_or_not == 'yes':
            
            favorite_language = input("what is your favorite language? ").lower()
            favorite_languages.append(favorite_language)
            
            # again ask user if they had any other language choice 
            # if yes the continue the loop if no the break the loop
            yes_or_not = input("Do you have any other favorite language? write 'yes' or 'no' ").lower()
        
            if yes_or_not == 'no':
                active01 = False
        else:
            # ask user if they had any other language choice
            yes_or_not = input("Do you have any other favorite language? write 'yes' or 'no' ").lower()

    # after one persone had finish his poll add his result in poll result dictionary
    # then remove all item from name and favorite language so that we can start with a new empty list    
    for name in names:
        poll_result[name] = favorite_languages[:len(favorite_languages)]
        del names[0]

        for i in range(len(favorite_languages)):
            del favorite_languages[0]

    # ask user if they want to take part poll anymore 
    # if yes the start from the start point again 
    yes_or_not = input("Do you want to play more ? write 'yes' or 'no' ").lower()

    if yes_or_not == 'yes':
        name = input("what is your name? ").lower()
        names.append(name)


        active01 = True

        while active01:
            # print("Write 'done' when you your answer is finish")
            favorite_language = input("what is your favorite language? ").lower()
            favorite_languages.append(favorite_language)
            yes_or_not = input("Do you have any other favorite language? write 'yes' or 'no' ").lower()

            while yes_or_not == 'yes':
                
                favorite_language = input("what is your favorite language? ").lower()
                favorite_languages.append(favorite_language)
                yes_or_not = input("Do you have any other favorite language? write 'yes' or 'no' ").lower()
            
                if yes_or_not == 'no':
                    active01 = False

            yes_or_not = input("Do you want to play more ? write 'yes' or 'no' ").lower()

    if yes_or_not == 'no':

        active = False


    for name in names:
        poll_result[name] = favorite_languages[:len(favorite_languages)]
        del names[0]

        for i in range(len(favorite_languages)):
            del favorite_languages[0]

    

poll(name,favorite_language)

    










