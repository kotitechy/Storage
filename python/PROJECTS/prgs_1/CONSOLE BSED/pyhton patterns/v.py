for row in range(7):
    for col in range(5):
        if (row in {0,1,2,3,4} and col in {0,4}) or(row == 5 and col in {1,3} ) or (row==6 and col == 2):
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()