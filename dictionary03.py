"""
6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.

• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.

If they have not yet taken the poll, print a message inviting them to take
the poll.
"""

favoriteLanguage = {
    'shafiq' : 'python',
    'sumon' : 'php',
    'anam' : 'javascript',
    'basar': 'ruby',
}
  
peoples = ['limon','tonmoy','arman','anam','afnan','sumon','shafiq','rayhan']

for people in peoples:
    if people in favoriteLanguage.keys():
        print( "\n" + "Congratulation!  " + people + " You have take part in poll and thanks for that")
    else:
        print( "\n" + "Hi! " + people + ", I think you should take part in the favorite language poll" )



