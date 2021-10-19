"""rows = 5
k = 2 * 5 - 2
for i in range(5, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

    *
   ***
  *****
 *******
"""

"""row = int(input("Enter Row Number: "))
count = 0

for i in range(0,row):
    for j in range(0,row-i):
        print(end=" ")

    count = count +1 

    for k in range(0,count+i):
        print("*", end="")
    print("")
"""

row = int(input("Enter Row Number: "))

count = 0

for i in range(row):
        
        for k in range(1,row,-1):
             print(end=" ")
             
        count = count +1 
    
        for j in range(0, row+1):
            print("*", end= "")
        print("")










