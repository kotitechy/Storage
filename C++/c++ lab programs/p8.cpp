
//inline functions 
#include<iostream>
using namespace std;
 
 inline cube(int a){
	 return (a*a*a);
 }
 int main(){
 	int result=0,a;
 	cout<<endl<<"Enter the value of a: ";
 	cin>>a;
 	result=cube(a);
 	cout<<endl<<"The cube of "<<a<<" is "<<result;
 	return 0;
 }
