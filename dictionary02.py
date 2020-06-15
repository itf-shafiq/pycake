"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.

"""

glossary = {
    "pop": "pop is a method remove things and store it to itself", 
    "append": "append is used for adding thing to a place",
    "loop" : "repeating same thing again and aging",

    }

glossary['del'] = " Del is a builtin function used to delete things from a list or dictionary"
glossary['sort'] = "sort is method to sort unordered items"
glossary['revers'] = "revers is method to revers items in programing"

for word,meaning in glossary.items():
    print("\n" + "Word: " + word + "\n" + "meaning: " + meaning + ";" )






