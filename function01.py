def get_formated_name( first_name, last_name, middle_name=""):
    formatedName = first_name + " " + middle_name + " " + last_name

    return formatedName 

myName = get_formated_name('shafiqul', 'islam')
myName_2 = get_formated_name('shafiqul', 'shafiq', 'islam')

print(myName)
print(myName_2)


def getFormatedName(firstName, lastName, middleName= ""):
    if middleName:
        fullName = firstName + " "+ middleName + " " + lastName
    else:
        fullName = firstName + " " + lastName 
    
    return fullName 

myName01 = getFormatedName('shafiqul','shafi','islam')
print(myName01)
myName02 = getFormatedName('shafiqul','islam')
print(myName02)