/*
Program : Swaping of 2 numbers in c++
Author : shiva charan
*/
#include<iostream>
using namespace std;

int main(){
	int a , b,c;          //3 integer variables
	cout<<"Enter a:  ";
	cin>>a;                //input a
	cout<<"Enter b:  ";
	cin>>b;                 //input b
	cout<<endl<<"a & b Before swap: \n a: "<<a<<" b: "<<b;
	 c = a;         //swapping 
	 a = b;
	 b = c;
	 cout<<endl<<"a & b After swap: \n a: "<<a<<" b: "<<b;
	/*
	method-2
	a=a+b;
	a=a-b;
	b=a-b;
	method-3
	a=a*b;
	a=a/b;
	b=a/b;
   	*/
	return 0;
}
