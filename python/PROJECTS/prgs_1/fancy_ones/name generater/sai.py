for r in range(7):
    for c in range(18):
        if (r==0 and c in {1,2,3,4}) or (r in {1,2} and c == 0) or (r in {4,5} and c == 4) or (r==3 and c in {1,2,3}) or (r==6 and c in {0,1,2,3}) or (r==0 and c in {7,8,9,10}) or (r == 3 and c in {6,7,8,9,10,11}) or (r in {1,2,4,5,6} and c in {6,11}) or (r in {0,6} and c in {13,14,15,16,17}) or (r in {1,2,3,4,5} and c == 15):
            print("*",end=" ");
        else:
            print(" ",end=" ")
    print()