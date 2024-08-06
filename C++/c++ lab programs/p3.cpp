#include<iostream>
using namespace std;
int main(){
	int a[10],i,n;
	cout<<endl<<"Enter a number: ";
	cin>>n;
	
	for(i=0;i<n;i++){
		cout<<endl<<"Enter a["<<i<<"]";
		cin>>a[i];
	}
	for(i=0;i<n;i++){
		cout<<a[i]<<"\t";
	}
	return 0;
}
