for row in range(7):
    for col in range(5):
        if (row in {0,1,2,3,4,5} and col in {0,4}) or (row == 6 and col in {1,2,3}):
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()