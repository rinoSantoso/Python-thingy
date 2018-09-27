cups = [1, 0, 0] # Create list representing the cups and ball


# Define a function that accepts the input swaps and create the output
def cnb (swaps):
    lSwaps = list(swaps)
    for i in lSwaps:
        if i.upper() == "A":
            cups[0], cups[1] = cups[1], cups[0]
        elif i.upper() == "B":
            cups[1], cups[2] = cups[2], cups[1]
        elif i.upper() == "C":
            cups[0], cups[2] = cups[2], cups[0]

    for j in range(len(cups)):
        if cups[j] == 1:
            print ("The ball in in cup number " + str(j + 1))


# Input part
while True:  # Status loop if the user wants to use the program
    status = str(input("Would you like to use the Cups and Ball program? (Y/N) "))
    if status.upper() == "Y":
        swaps = str(input("Please insert the swap operations "))
        cnb(swaps)  # Calls the function

    elif status.upper() == "N":
        print ("Thank you for using this program!")
        break