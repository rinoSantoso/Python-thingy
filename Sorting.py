def sort(unsorted):
    sorted = []
    sorted.append(unsorted[0])
    i = 1
    while i < len(unsorted):
        for j in range(len(sorted)):
            if unsorted[i] < sorted[j]:
                sorted.insert(j, unsorted[i])
                break
            elif j == len(sorted) - 1:
                sorted.insert(j + 1, unsorted[i])
        i += 1

    return sorted

while True:  # Status loop if the user wants to use the program
    status = str(input("Would you like to use the sorting program? (Y/N) "))
    if status.upper() == "Y":
        numList = []
        type = input("Would you like to do an ascending or descending sort? ")
        while True:  # Input loop
            num = int(input("Please input the numbers you wish to sort (input '-1' to end input) "))
            if num >= 0:
                numList.append(num)
            elif num == -1:
                break

        print ("The sorted list of numbers in ascending order is")
        if type.lower() == "ascending":
            print (sort(numList))
        elif type.lower() == "descending":
            print(sort(numList)[::-1])

    elif status.upper() == "N":
        print("Thank you for using this sorting program!")
        break