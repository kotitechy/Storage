#include<iostream>
using namespace std;

int main(){
	int i=1,n;
	cout<<"Enter a number: ";
	cin>>n;
	
	do{
		if(n%i==0){
			cout<<endl<<i;
			
		}
		i++;
	}while(i<=n);
	return 0;
}
