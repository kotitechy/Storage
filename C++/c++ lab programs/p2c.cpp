
//else if...else if statement
#include<iostream>
using namespace std;
int main(){
int a,b,c;
cout<<"Enter 3 numbers  ";
cin>>a>>b>>c;

if(a>=b){
	if(a>=c){
	
	cout<<"\n A is big";
}
else{
	cout<<endl<<"c is big";
}
}
else if(b>=a){
	if(b>=c){
	
	cout<<"\n B is big";
}
else{
	cout<<endl<<"c is big";
}
}
}

