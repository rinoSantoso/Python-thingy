output = []  # Create empty list for storage


# Define a function that accepts the input names and create the output
def KMP (names):
    lNames = list(names)
    output.append(lNames[0])
    i = 0
    while i < len(lNames):
        if lNames[i] == "-":
            output.append(lNames[i + 1])
        i += 1

    names = ''.join(output)
    print (names)


# Input part
while True:  # Status loop if the user wants to use the program
    status = str(input("Would you like to use the name shortening program? (Y/N) "))
    if status.upper() == "Y":
        names = str(input("Please insert names separated by hyphens (-) "))
        KMP(names)

    elif status.upper() == "N":
        print ("Thank you for using this program!")
        break