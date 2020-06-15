# all poll result will be sorted in a dictionary 
# 1st I will ask people name 
# 2nd I will ask them for there favorite language
# all favorite language will be sotored in a list for that we need to start program with empty list
#3rd I will repeat this process until someone enter word q for quite 
# if some one enter quite then I will break the loop and print out poll result for each people  

allPollResult = {}
pollResult = []

def poll(k,*pollResult):
        
    while True:
        k = str(input("What is your name? ").lower())
        pollResult = str(input("What is your favorite Language? ").lower())

        allPollResult[k] = pollResult

        if k == "q" or pollResult == "q":
            for name,language in allPollResult.items():
                print( "\n" + name + ":" + " Your Favorite Language is: " + "'" + language + "' ;")
            break 
        else:
            continue

# k = str(input().lower())




