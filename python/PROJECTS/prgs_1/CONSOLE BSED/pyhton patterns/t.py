for row in range(7):
    for col in range(5):
        if (row == 0) or (row in {1,2,3,4,5} and col == 2):
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()