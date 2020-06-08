"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.

• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.

• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""

glossary = {
    "pop": "pop is a method remove things and store it to itself", 
    "append": "append is used for adding thing to a place",
    "loop" : "repeating same thing again and aging",

    }
# solution with loop 

for k,v in glossary.items():
    print("\n" + "Word: " + k + " || " + "meaning: " + "'" + v +"' ;")

# Solution without loop 

print( "\n" "Word: " + list(glossary.keys())[0] + "\n" + "meaning: " + glossary['pop'])
print( "\n" "Word: " + list(glossary.keys())[1] + "\n" + "meaning: " + glossary['append'])
print( "\n" "Word: " + list(glossary.keys())[2] + "\n" + "meaning: " + glossary['loop'])


# print(list(glossary.keys())[0])


# dic = {1 : 'a', 2 : 'b', 3 : 'c'}
 
# a = list(dic.keys())[0]
 
# print(a)