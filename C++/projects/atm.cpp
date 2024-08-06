#include <iostream>
#include<stdlib.h>
using namespace std;


/* run this program using the console pauser or add your own getch, system("pause") or input loop */
//This willthe atm class objects


class atm
{
private:
    float cdno, phno;
    char d, cn;
    string name, acty, pass0, pass1;
    float dpbal, wdbal, bal, wd;
    int i;

public:
    void newac();

    void gaetdata();

    void checkbal();

    void withdraw();

    void deposit();

    void welcome();

    void out();

    void dpprint();

    void wdprint();

    void clearscn();

    void secu();

    void crepass();
};

void atm ::welcome()
{
    atm ob1;
    int op;

    cout << endl
         << "\t \t \t \t \t \t"
         << "---------------------------------------------" << endl;
    cout << "\t \t \t \t \t \t"
         << "|     Welcome to ktc bank services          |" << endl;
    cout << "\t \t \t \t \t \t"
         << "---------------------------------------------" << endl;

    cout << "1. REGISTER AN ACCOUNT" << endl;
    cout << "2. CHECK BALANCE" << endl;
    cout << "3. DEPOSIT" << endl;
    cout << "4. WITH DARW" << endl;
    cout << "5. CHANGE PASSWORD" << endl;
    cout << "5. EXIT" << endl;
    cout << endl
         << "CHOOSE ANY OF ONE SERVICE: ";
    cin >> op;
    cout << endl;

    switch (op)
    {
    case 1:
    {
        ob1.newac();
        ob1.crepass();
        ob1.deposit();
        ob1.dpprint();
        out();
        clearscn();
        break;
    }

    case 2:
    {
        ob1.secu();
        ob1.dpprint();
        out();
        clearscn();
        break;
    }

    case 3:
    {
        ob1.secu();
        ob1.deposit();
        ob1.dpprint();
        out();
        clearscn();
        break;
    }
    case 4:
    {
        ob1.secu();
        ob1.withdraw();
        ob1.wdprint();
        out();
        clearscn();
        break;
    }
    case 5:
    {
        cout << "change the password here";
    }
    case 6:
    {
        out();
        clearscn();
        break;
        break;
    }
    }
}

void atm::clearscn()
{

    cout << "DO YOU WANT TO CLEAR THE SCREEN";
    cin >> cn;
    if (cn == 's' || cn == 'S')
    {
        system("cls");
    }
    else
    {
        cout << "YOU MUST CLEAR THE SCREEN BEFORE LEAVING ";
        system("cls");
    }
}
void atm::newac()
{
    system("cls");
    int act;
    cout << endl
         << "1. MAJOR" << endl
         << "2. MINOR" << endl;
    cout << "WHICH TYPE OF ACCOUNT DO YOU WANT: ";
    cin >> act; // account type
    system("cls");
    if (act == 1)
    {

        string acty = "MAJOR";
        cout << "ACCOUNT REGISTRATION PROCESS" << endl;
        cout << "ACCOUNT TYPE " << acty << endl
             << endl
             << endl;
        cout << "Enter your details:" << endl
             << endl;
        cout << "Name: ";
        cin >> name;
        cout << endl;
        cout << "Cardno: ";
        cin >> cdno;
        cout << endl;
        cout << "Phone Number: ";
        cin >> phno;
        cout << endl;
    }
    else
    {
        system("cls");
        char d; // decsicion making
        string acty = "MINOR";
        cout << "ACCOUNT REGISTRATION PROCESS" << endl;
          cout << "ACCOUNT TYPE " << acty << endl
             << endl
             << endl;
        cout << "Enter your details:" << endl
             << endl;
        cout << "Name: ";
        cin >> name;
        cout << endl;
        cout << "Cardno: ";
        cin >> cdno;
        cout << endl;
        cout << "Phone Number: ";
        cin >> phno;
        cout << endl;
        
        cout << endl;
    }
}

void atm::secu()
{

    cout << endl;
    cout << "Enter your password";
    cin >> pass0;

    if (pass1 != pass0)
    {
        cout << endl
             << "INVALID PASSWORD" << endl
             << "TRY AGAIN";
    }
    else{
    	cout<<endl<<"correct password"<<endl;
	}
}
void atm::crepass()
{
    cout << endl
         << "Your password must not contain any special characters"
         << endl
         << "password must be lessthan or equal to 8 digits";
    cout << endl
         << "USE A-Z  \n a-z \n  0-9 For creating password";
    cout << endl
         << "EG:- SHIVA1197  || koti9971" << endl;
    cin >> pass1;

    cout << "RE-ENTER THE PASSWORD" << endl;
    cin >> pass1;

    if (pass1 == pass0)
    {
        cout << endl
             << "PASSWORD CREATED SUCESSFULLY";
    }
}
void atm::dpprint()
{

    cout << endl
         << " --------------------------------------------------------------------------------------------------";
    cout << endl
         << "|    NAME OF THE BANK                        :  KTC BANK                                            |";
    cout << endl
         << " ---------------------------------------------------------------------------------------------------";
    cout << endl
         << "|    BARNCH                                  :  BARNCH NO 111                                       |";
    cout << endl
         << " --------------------------------------------------------------------------------------------------";
        cout<<endl<<"|    NAME OF THE AC HOLDER                   : "<<name;
    cout<<endl<<" --------------------------------------------------------------------------------------------------";
       cout<<endl<<"|    ACCOUNT TYPE                            : "<<acty;
    cout << endl
         << " ---------------------------------------------------------------------------------------------------";
    cout << endl
             <<"|    ACCOUNT NUMBER                          : 202122." << cdno;
    cout<<endl<<"------------------------------------------------------------------------------------------------";
   cout<<endl<<"|    PHONE NUMBER                            : "<<phno;
    cout << endl
         << " ---------------------------------------------------------------------------------------------------";
    cout << endl
         << "|    AMOUNT DEPOSITED                        : " << dpbal;
    cout << endl
         << " ---------------------------------------------------------------------------------------------------";
    cout << endl
         << "|    BALANCE AFTER DEPOSITING AMOUNT         : " << bal;
    cout << endl
         << " ---------------------------------------------------------------------------------------------------" << endl;
    cout << "COLLECT THE PRINT FROM DISPENSER" << endl;
}

void atm::wdprint()
{

    cout << endl
         << " --------------------------------------------------------------------------------------------------";
    cout << endl
         << "|    NAME OF THE BANK                        :  KTC BANK                                            |";
    cout << endl
         << " ---------------------------------------------------------------------------------------------------";
    cout << endl
         << "|    BARNCH                                  :  BARNCH NO 111                                       |";
    cout << endl
         << " --------------------------------------------------------------------------------------------------";
    cout<<endl<<"|    NAME OF THE AC HOLDER                   : "<<name<<"                                           ";
    cout<<endl<<" --------------------------------------------------------------------------------------------------";
    cout<<endl<<"|    ACCOUNT TYPE                            : "<<acty;
    cout << endl<<"------------------------------------------------------------------------------------------------";
   cout<<endl<<"|    PHONE NUMBER                            : "<<phno<<endl<<
    " ---------------------------------------------------------------------------------------------------";
;
    cout << endl
         << "|    ACCOUNT NUMBER                          : 202122." << cdno << "                                           ";
    cout << endl
         << " ---------------------------------------------------------------------------------------------------";
         
    cout << endl
         << "|    AMOUNT WITHDRAWED                        : " << wd << "                                         ";
    cout << endl
         << " ---------------------------------------------------------------------------------------------------";
    cout << endl
         << "|    BALANCE AFTER WITHDARWING AMOUNT         : " << wdbal << endl;
    cout << endl
         << " ---------------------------------------------------------------------------------------------------" << endl;
    cout << "COLLECT THE PRINT FROM DISPENSER" << endl;
}

void atm::out()
{

    cout << "---------------------------------------------" << endl;
    cout << "|      Thank you for visiting our bank      |" << endl;
    cout << "|             please visit again            |" << endl;
    cout << "---------------------------------------------" << endl;
}

void atm::deposit()
{

    cout << "\n Welcome to deposit section";
    cout << " Enter the amount you want to deposit: ";
    cin >> dpbal;
    if (dpbal <= 1000)
    {
        cout << endl
             << "PLEASE ENTER A VALID AMOUNT " << endl;
        clearscn();
    }
    else
    {

        bal = bal + dpbal;
        system("cls");
        cout << "THANK YOU SO MUCH MR/MS " << name << endl
             << "FOR DEPOSITING FUNDS IN KTC BANK";
    }
}

void atm::withdraw()
{
    system("cls");
    cout << endl
         << "WELCOME TO WITHDRAW SECTION";
    cout << endl
         << "Enter the amount you want to with-draw:  ";
    cin >> wd;
    if (wd > bal - 1000 || bal == 0)
    {
        wd = 0;
        system("cls");
        cout << "INSUFFICIENT BALANCE " << endl
             << "SO YOU CAN'T WITHDRAW THE AMOUNT" << endl;
        cout << "THANK YOU FOR USING KTC BANK" << endl;
    }
    else
    {
        system("cls");
        cout << endl
             << "RUPEES " << wd << endl
             << "DISPENSED COLLECT THEM FROM DISPENSER" << endl;
        cout << "AMOUNT WITHDRWED SUCESSFULLY" << endl;
        bal = bal - wd;
        wdbal = bal;
    }
}

int main(int argc, char** argv) {
	    cout << "JAI GANESHA";
    atm ob1;

    while (1)
    {
        atm ob1;
        int op;

        ob1.welcome();
    }
	return 0;
}
