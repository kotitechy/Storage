for row in range(7):
    for col in range(7):
        if ( row in {1,2,3,4,5} and  (col in {0,4}))or (row in {0,6} and col in{1,2,3})or(row-col==1): 
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()