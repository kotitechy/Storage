s = input("Enter your name : ")
s1=s.lower()
for i in s1:
    match i:
            case 'a':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row == 0) and (col in {1,2,3}):
                         print("*",end=" ")
                        elif (row in {1,2,4,5,6} and col in {0,4}):
                            print("*",end=" ")
                        elif (row == 3):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()
            case 'b':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,6}) and (col in {0,1,2,3}):
                         print("*",end=" ")
                        elif (row in {1,2,4,5} and col in {0,4}):
                            print("*",end=" ")
                        elif (row == 3 and col in {0,1,2,3}):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()
            case 'c':
                print()
                print()
                for row in range(7):
                     for col in range(5):
                         if (row in {0,6}) and (col in {1,2,3,4}):
                          print("*",end=" ")
                         elif (row in {1,2,3,4,5} and col in {0}):
                             print("*",end=" ")
                         else:
                             print(" ",end=" ")
                     print()
            case 'd':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,6}) and (col in {0,1,2,3}):
                         print("*",end=" ")
                        elif (row in {1,2,3,4,5} and col in {0,4}):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()
            case 'e':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,3,6}):
                         print("*",end=" ")
                        elif (row in {1,2,3,4,5} and col in {0}):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'f':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,3}):
                         print("*",end=" ")
                        elif (row in {1,2,3,4,5} and col in {0}):
                            print("*",end=" ")
                        elif (row == 6 and col == 0):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'g':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,6}) and (col in {1,2,3}):
                         print("*",end=" ")
                        elif (row in {4,5} and col in {0,4}):
                            print("*",end=" ")
                        elif (row in {1,2} and col == 0):
                           print("*",end=" ")
                        elif (row in {4,5} and col in {0,6}):
                           print("*",end=" ")
                        elif (row == 3 and col in {0,3,4,5}):
                           print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'h':
              print()
              print()
              for row in range(7):
                    for col in range(5):
                        if (row in {0,1,2,4,5,6}) and (col in {0,4}):
                         print("*",end=" ")
                        elif (row == 3):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()  
                

            case 'i':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,6}):
                         print("*",end=" ")
                        elif (row in {1,2,3,4,5} and col in {2}):
                            print("*",end=" ")

                        else:
                            print(" ",end=" ")
                    print()

            case 'j':
                print()
                print()
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

            case 'k':
                print()
                print()
                for row in range(7):
                        for col in range(5):
                            if (col == 0):
                             print("*",end=" ")
                            elif (row+col==4):
                                print("*",end=" ")
                            elif (row-col==2):
                                print("*",end=" ")
                            else:
                                print(" ",end=" ")
                        print()
            case 'l':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (col == 0):
                         print("*",end=" ")
                        elif(row == 6):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()
            case 'm':
                print()
                print()
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

            case 'n':
                print()
                print()
                for row in range(7):
                    for col in range(7):
                        if (row  and col in {0,6}):
                         print("*",end=" ")
                        elif(row-col==0) or (row == 0 and col == 6):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'o':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if ( row in {1,2,3,4,5} and  (col in {0,4}))or (row in {0,6} and col in{1,2,3}): 
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'p':
               print()
               print()
               for row in range(7):
                for col in range(5):
                    if (row in {3} and col in {1,2,3}) or (row == 0 and col !=4):
                     print("*",end=" ")
                    elif (row in {3,4,5} and col in {0}):
                        print("*",end=" ")
                    elif (row == 6 and col == 0) or (row in {1,2} and col in {0,4}) :
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
                print() 

            case 'q':
                print()
                print()
                for row in range(7):
                    for col in range(7):
                        if ( row in {1,2,3,4,5} and  (col in {0,4}))or (row in {0,6} and col in{1,2,3})or(row-col==1): 
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'r':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {3} and col in {1,2,3}) or (row == 0 and col !=4):
                         print("*",end=" ")
                        elif (row in {3,4,5} and col in {0}):
                            print("*",end=" ")
                        elif (row == 6 and col == 0) or (row in {1,2} and col in {0,4}) or (row-col==2):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 's':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in [1,2] and col == 0) or (row in {4,5} and col == 4):
                         print("*",end=" ")
                        elif (row == 0 and col in [1,2,3,4]) or (row == 6 and col in [0,1,2,3]) or (row == 3 and col in {1,2,3}):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()
            case 't':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row == 0) or (row in {1,2,3,4,5} and col == 2):
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'u':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,1,2,3,4,5} and col in {0,4}) or (row == 6 and col in {1,2,3}):
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'v':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,1,2,3,4} and col in {0,4}) or(row == 5 and col in {1,3} ) or (row==6 and col == 2):
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'w':
                print()
                print()
                for row in range(7):
                    for col in range(5):
                        if (row in {0,1,2,3}) and (col in {0,4}) or (row in {4,5} and col in{0,2,4}) or (row == 6 and col != 2):
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'x':
                print()
                print()
                for row in range(7):
                    for col in range(7):
                        if (row-col==0) or (row+col==6):
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'y':
                print()
                print()
                for row in range(7):
                    for col in range(7):
                        if (row-col==0 and row<4) or (row+col==6 and row<4) or(row>3 and col==3):
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()

            case 'z':
                print()
                print()
                for row in range(7):
                    for col in range(7):
                        if (row in {0,6}) or (row+col==6):
                         print("*",end=" ")
                        else:
                            print(" ",end=" ")
                    print()


            case default:
                print()
                print()
                print("nope found")
