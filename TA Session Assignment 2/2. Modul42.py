lOutput = []  # Create empty list for storage


# Define a function that accepts the input number list and create the output
def mod42 (inNum):
    for i in inNum:
        lOutput.append(i%42)
    output = set(lOutput)
    print (len(output))


# Input part
while True:  # Status loop if the user wants to use the program
    status = str(input("Would you like to use the program? (Y/N) "))
    if status.upper() == "Y":
        inNum = []

        while True:  # Input loop
            num = int(input("Please input your number (input '-1' to end) "))
            if num >= 0:
                inNum.append(num)
            elif num == -1:
                break
        mod42(inNum)  # Calls the function

    elif status.upper() == "N":
        print("Thank you for using this program!")
        break
