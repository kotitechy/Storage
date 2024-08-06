for row in range(7):
    for col in range(5):
        if (row in {0,1,2,3}) and (col in {0,4}) or (row in {4,5} and col in{0,2,4}) or (row == 6 and col != 2):
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()