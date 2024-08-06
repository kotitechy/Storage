#include<iostream>
using namespace std;

int main(){
	int n,m,i,s=0;
	cout<<"Enter the number: ";
	cin>>n;
	m=n;
    while(n>0){
    	i=n/10;
    	s=s*10+i;
    	n=n/10;
	}	
	if(m==s){
		cout<<endl<<"The number is palantrom";
		
	}
	else {
		cout<<endl<<"The number is not a palantrom";
	}
	return 0;
}
