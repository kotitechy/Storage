/*
Program : All Arithematic operations in c++
Author : shiva charan
*/
#include<iostream>
using namespace std;

int main(){
	int a , b; 
	cout<<"Enter a:  ";
	cin>>a;                //input a
	cout<<"Enter b:  ";
	cin>>b;                //input b
	cout<<"The Sum is             : "<<(a+b)<<endl;     //addition 
	cout<<"The Subtraction is     : "<<(b-a)<<endl;     //subtraction
	cout<<"The Multiplication is  : "<<(a*b)<<endl;     //multiplication
	cout<<"The Division  is       : "<<(b/a)<<endl;     //division
	cout<<"The Moduli-Division is : "<<(b%a)<<endl;     //moduli division 
	cout<<"Incremented " <<a<<" is       : "<<++a<<endl;       //increment
	cout<<"Decremented " <<a<<" is       : "<<--a<<endl;       //Decrement
	
	return 0;
}
