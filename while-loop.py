luckyNumber = int(input("Guess the Lucky number: "))

while luckyNumber != 7:
    print("You got the wrong Number" +"\n")
    answer = input("Do you want play more? : ").lower()

    if answer == "no":
        break
    else:
        luckyNumber = int(input("Guess the Lucky Number"))

else:
    print("Yes! you Got the Right Number")

# This work fine :)
