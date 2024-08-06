#include<iostream>
using namespace std;

int main(){
	int n,r;
	cout<<endl<<"Enter a number: ";
	cin>>n;
	cout<<endl<<"Multiplication table of "<<n<<endl;
	for(int i=1;i<11;i++){
		r=i*n;
		cout<<"\t \t \t "<<n<<" * "<<i<<" = "<<r<<endl;
	}
	
	return 0;
}
