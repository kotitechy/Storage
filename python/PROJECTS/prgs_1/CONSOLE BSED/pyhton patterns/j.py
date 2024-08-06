for row in range(7):
    for col in range(5):
        if (row in {0}):
         print("*",end=" ")
        elif (row in {1,2,3,4,5} and col in {2}):
            print("*",end=" ")
        elif(row == 6 and col == 1):
           print("*",end=" ")
        elif(row in {4,5} and col == 0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()