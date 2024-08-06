#include <stdio.h>
#include <stdlib.h>
struct ac
{
    int cd;
    int pass;
    int bal;
    char name[10];
} a = {11, 1, 5000.00, "shiva"}, b = {12, 2, 6000.00, "srisailam"}, c = {13, 3, 7000.00, "prameela"};

int main()
{
    int cd, pass, i, op, dp, wd;
    int bal;
    printf("\n HELLO WELCOME TO KOTI TECHY ATM SERVICES");
    printf("\n Enter the card number \n ");
    scanf("%d", &cd);
    if (cd == a.cd || cd == b.cd || cd == c.cd)
    {
        printf("\n Enter the password  ");
        scanf("%d", &pass);

        if (pass == a.pass || pass == b.pass || pass == c.pass)
        {
        hello:
        wel:
            if (cd == a.cd && pass == a.pass)
            {
                printf("\n mr. %s welcome to koti techy bank", a.name);
                printf("\n  ---------------------------------");
                printf(" \n | 1-> deposit                   |");
                printf(" \n | 2-> with draw                 |");
                printf(" \n | 3-> check balance             |");
                printf(" \n | 4-> exit                      |");
                printf("\n  ---------------------------------");
                printf("\n CHOOSE AN OPTION ");
                scanf("%d", &op);
                switch (op)

                {
                case 1:

                {
                    printf("\n Enter the amount to deposit");
                    scanf("%d", &dp);
                    a.bal = dp + a.bal;
                    printf("\n The total balance is %d", a.bal);
                    printf("\n Thank you for visiting");
                    exit(0);
                }
                case 2:

                {
                    printf("\n Enter the amount to withdraw");
                    scanf("%d", &wd);
                    if (wd > a.bal - 1000)
                    {
                        printf("\n No enough balance");
                        printf("\n The total balance in your ac is %d", a.bal);
                        printf("\n Thank you for visiting");
                        exit(0);
                    }
                    else if (wd < a.bal - 1000)
                    {
                        a.bal = a.bal - wd;
                        printf("\n collect your amount \n The amount you had withdrawn is %d", wd);
                        printf("\n The total balance is %d", a.bal);
                        printf("\n Thank you for visiting");
                        exit(0);
                    }
                }
                case 3:
                {
                    printf("\n The balance is %d", a.bal);

                    printf("\n Thank you for visiting");
                    exit(0);
                }
                case 4:
                {
                    printf("\n Thank you for visiting ");
                    exit(0);
                }
                }
            }

            else if (cd == b.cd && pass == b.pass)
            {
                printf("\n mr. %s welcome to koti techy bank", b.name);
                printf("\n  ---------------------------------");
                printf(" \n | 1-> deposit                   |");
                printf(" \n | 2-> with draw                 |");
                printf(" \n | 3-> check balance             |");
                printf(" \n | 4-> exit                      |");
                printf("\n  ---------------------------------");
                printf("\n CHOOSE AN OPTION ");
                scanf("%d", &op);
                switch (op)

                {
                case 1:

                {
                    printf("\n Enter the amount to deposit");
                    scanf("%d", &dp);
                    b.bal = dp + b.bal;
                    printf("\n The total balance is %d", b.bal);
                    printf("\n Thank you for visiting");
                    exit(0);
                }
                case 2:

                {
                    printf("\n Enter the amount to withdraw");
                    scanf("%d", &wd);
                    if (wd > b.bal - 1000)
                    {
                        printf("\n No enough balance");
                        printf("\n The total balance in your ac is %d", b.bal);
                        printf("\n Thank you for visiting");
                        exit(0);
                    }
                    else if (wd < b.bal - 1000)
                    {
                        b.bal = b.bal - wd;
                        printf("\n collect your amount \n The amount you had withdrawn is %d", wd);
                        printf("\n The total balance is %d", b.bal);
                        printf("\n Thank you for visiting");
                        exit(0);
                    }
                }
                case 3:
                {
                    printf("\n The balance is %d", b.bal);

                    printf("\n Thank you for visiting");
                    exit(0);
                }
                case 4:
                {
                    printf("\n Thank you for visiting ");
                    exit(0);
                }
                }
            }
            else if (cd == c.cd && pass == c.pass)
            {
                printf("\n mr. %s welcome to koti techy bank", c.name);
                printf("\n  ---------------------------------");
                printf(" \n | 1-> deposit                   |");
                printf(" \n | 2-> with draw                 |");
                printf(" \n | 3-> check balance             |");
                printf(" \n | 4-> exit                      |");
                printf("\n  ---------------------------------");
                printf("\n CHOOSE AN OPTION ");
                scanf("%d", &op);
                switch (op)

                {
                case 1:

                {
                    printf("\n Enter the amount to deposit");
                    scanf("%d", &dp);
                    c.bal = dp + c.bal;
                    printf("\n The total balance is %d", c.bal);
                    printf("\n Thank you for visiting");
                    exit(0);
                }
                case 2:

                {
                    printf("\n Enter the amount to withdraw");
                    scanf("%d", &wd);
                    if (wd > c.bal - 1000)
                    {
                        printf("\n No enough balance");
                        printf("\n The total balance in your ac is %d", c.bal);
                        printf("\n Thank you for visiting");
                        exit(0);
                    }
                    else if (wd < c.bal - 1000)
                    {
                        b.bal = c.bal - wd;
                        printf("\n collect your amount \n The amount you had withdrawn is %d", wd);
                        printf("\n The total balance is %d", c.bal);
                        printf("\n Thank you for visiting");
                        exit(0);
                    }
                }
                case 3:
                {
                    printf("\n The balance is %d", c.bal);

                    printf("\n Thank you for visiting");
                    exit(0);
                }
                case 4:
                {
                    printf("\n Thank you for visiting ");
                    exit(0);
                }
                }
            }
            else
            {
                printf("\n in correct password try again");
                exit(0);
            }
        }
    }
    else
    {
        printf("\n INCORRECT CARD NUMBERV \n TRYAGAIN");

        exit(0);
    }
}