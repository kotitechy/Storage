for row in range(7):
    for col in range(7):
        if (row-col==0 and row<4) or (row+col==6 and row<4) or(row>3 and col==3):
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()