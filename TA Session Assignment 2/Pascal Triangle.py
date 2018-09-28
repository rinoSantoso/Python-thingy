while True:
    status = str(input("Would you like to use the Pascal Triangle Generator program? (Y/N) "))
    if status.upper() == "Y":
        list = [1]
        size = int(input("Please input the size of the Pascal Triangle "))
        listCount = 0
        tempCount = 0
        while listCount <= size:
            print (list)
            tempList = []
            tempList.append(list[0])
            for tempCount in range ((len(list) - 1)):
                tempList.append(list[tempCount] + list[tempCount + 1])
            tempList.append(list[-1])
            list = tempList
            listCount += 1

    elif status.upper() == "N":
        print("Thank you for using the Pascal Triangle Generator program!")
        break
