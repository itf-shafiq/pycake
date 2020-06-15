""" Problem: 
  
Solution:
"""


""" Problem:   8-1. 
  8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.

Solution:
"""

"""
def message():
    print("Hello everyone, In this chapter we are going to learn python Functions.")

message()

"""

""" Problem: 8-2.
  8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
Solution:
"""

"""
def favorite_book(title):
    print("My favorite Book is " + title + ".")

    return

favorite_book("puthon crash course")

"""


# Positional argument practice 
"""
def dog(dog_name,dog_type = "dog"):
    print("I have a " + dog_type + " and its name is " + dog_name + "." )

dog("walli","hamster")"""


""" Problem: 8-3.
  8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
Solution:
"""
"""def make_shirt(size,message):
    print("\n" + "You have ordered a T-shirt that is " + size.title() + " size and the message printed on T-shirt is "
     + "\n" + "\t" + "'" + message.capitalize() + "'" )

make_shirt("small","I love python")

make_shirt(size = "medium" , message= "I am learing python")"""


""" Problem: 8-4.
  8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.

Solution:
"""
"""
def make_shirt01(size = "large",message = "I love python"):
    print("\n" + "You have ordered a T-shirt that is " + size.title() + " size and the message printed on T-shirt will be " 
    + "\t" + message.capitalize() + "." )


make_shirt01()
make_shirt01(size = "medium")
make_shirt01(size = "small", message = "python is awesome")"""


""" Problem: 
  8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
Solution:
"""
"""
def describe_city(city_name,country_name = "bangladesh"):
    return ("\n" + city_name.title() + " is in " + country_name.title() + ".")

print(describe_city("dhaka"))

print(describe_city("barlin","germany"))

print(describe_city(city_name = "silicon valley", country_name= "america"))"""

# Loop practice in function

def get_formated_name(first_name,last_name):
    full_name = first_name + " " + last_name

    return full_name

while True:
    print("Tell me your name")
    print("enter q if you want to quit")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatedName = get_formated_name(f_name, l_name)
    print("Your formated name is " + formatedName)
    print(type(l_name))



