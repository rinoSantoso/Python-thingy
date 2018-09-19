mult = 1
sym = '*'
space = " "
count = int(input("Enter the rows of triangles "))
while mult <= count:
    print (space*(count-mult)+sym*mult)
    mult += 1