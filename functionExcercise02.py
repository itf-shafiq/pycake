"""
2. Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20


def sumOfAllNumber(numbList):
    sum = 0
    for i in numbList:
        sum += i
        #numbList.remove(i)
    return sum

numbers = (8, 2, 3, 0, 7,4)
print(sumOfAllNumber(numbers))

"""
"""
 Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336

"""

def multiAllNum(allNum):
    result = 1
    for i in allNum:
        result = result*i
        
    return result

numbers = (8, 2, 3, -1, 7)

print(multiAllNum(numbers))
