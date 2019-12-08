#make a list 
car = ["BMW","Toyota","alion","Road Rorar","ferari"]

#add items using append function

car.append("suzuki")

print(car)

# add items using insert function

car.insert(2,"wagati")

print(car)

# Remove items using del function 

del car[1]

print(car)

# Remove items using pop function

expensive = car.pop(2)

print(car)
print("This" + " " + expensive + " " + "is too  expensive")

# Remove itens using remove functions

car.remove("BMW")

print(car)

# organize items alphabetically 

car.sort()

print(car)

# Print items reversely 

car.reverse()

print(car)

