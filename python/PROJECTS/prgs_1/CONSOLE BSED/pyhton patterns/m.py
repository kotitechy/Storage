for row in range(7):
    for col in range(5):
        if (row in {0,3,4,5,6} and col in {0,4}):
         print("*",end=" ")
        elif(row == 2 and col % 2 == 0):
           print("*",end=" ")
        elif(row==1 and col in {0,1,3,4}):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()