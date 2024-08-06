/*
Program : comments and i/o functions in c++
Author : shiva charan
*/
#include<iostream>
using namespace std;

int main(){
	//single line comment
	/*This
	is 
	    an 
	    multi-line 
	           comment*/
	           int a;                                   //variable int a
	           cout<<"Enter a number: ";                //prints enter a number
	           cin>>a;                                  //reads input from the user
	           cout<<endl<<"Entered number is: "<<a;    //prints the entered number on the console
	           //endl - terminates the cout to the next line
	           return 0;
}
