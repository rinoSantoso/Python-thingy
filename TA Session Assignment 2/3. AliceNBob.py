# Define a function that accepts the input stones taken list and create the output
def anb (numList):
    alice = 0
    bob = 0
    for i in numList:
        if i % 2 == 0:
            bob += 1
        elif i % 2 != 0:
            alice += 1

    if alice > bob:
        print("Alice is the final winner!")
    else:
        print("Bob is the final winner!")


# Input part
while True:  # Status loop if the user wants to use the program
    status = str(input("Would you like to play Game of Stones? (Y/N) "))
    if status.upper() == "Y":
        numList = []

        while True:  # Input loop
            num = int(input("Please input the number of stones taken in this round (input '-1' to end the game) "))
            if num >= 0:
                numList.append(num)
                if num % 2 == 0:
                    print ("Bob wins this round!")
                elif num % 2 != 0:
                    print("Alice wins this round!")

            elif num == -1:
                break
        anb(numList)  # Calls the function

    elif status.upper() == "N":
        print("Thank you for playing Game of Stones!")
        break
