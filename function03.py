# Make a 3D models printing simulator that will show you which design are printing and has been printed. 

# Start with some design that are need to be printed 

unPrintedDesign = ['car-model','iPhone case','rocket pendent','gun model']
printeddesigns = []

#simulate printing design until none are left 
#move each item that are printed 

while unPrintedDesign:
    currentlyPrinting = unPrintedDesign.pop()
    print( '\n'"on going printing model: " + currentlyPrinting + ";")
    printeddesigns.append(currentlyPrinting)

    # printeddesigns = printeddesigns.append(currentlyPrinting)

for printeddesign in printeddesigns:
    print('\n' + "'" + printeddesign + "'" + " has been printed ")

#########################################################

def printModels(unprintedDesign, printedDesign):

    while unprintedDesign:
        currentPrinting = unprintedDesign.pop()
        print('\n''On going printing models are: ' + '"' + currentPrinting + '" ;' )
        printedDesign.append(currentPrinting)


    for printedDesigns in printedDesign:
        print("\n" "'" + printedDesigns + "'" + " has been printed")

unprintedDesign = ['car model','gun model','rocket pendent','iPhone case']
printedDesign = []
printModels(unprintedDesign,printedDesign)