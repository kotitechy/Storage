for row in range(7):
    for col in range(7):
        if (row  and col in {0,6}):
         print("*",end=" ")
        elif(row-col==0) or (row == 0 and col == 6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()