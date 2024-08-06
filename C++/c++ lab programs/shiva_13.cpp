#include<iostream>
using namespace std;
int main(){
	int *p=NULL;
	p=new(nothrow )int;
	if(!p){
		cout<<"Allocated of memory failed!...";
	}
	else{
		*p=29;
		cout<<endl<<"Value of p: "<<*p<<endl;
	}
	int n=111;
	int *q=new(nothrow)int [n];
	if(!q){
		cout<<"Allocation of memeorry failed!...";
	}
	else{
		for(int i=0;i<n;i++){
			q[i]=i+1;
		}
	}
	cout<<"\n The value stored in the block of memory ";
	for(int j=0;j<n;j++){
		cout<<q[j]<<"   ";
	}
	delete p;
	delete q;
//	delete r;
	
	
	return 0;
 }  

