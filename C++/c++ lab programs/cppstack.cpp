#include<iostream>
using namespace std;
#define max 4
int arr[max],top=-1;
void push(int data)
{
	if(top==max-1)
	{
		cout<<"stack overflow"<<endl;
	}
	top=top+1;
	arr[top]=data;
}
int pop()
{
	if(top==-1)
	{
		cout<<"stack underflow"<<endl;
	}
	top=top-1;
}
void show()
{
	if(top==-1)
	{
		cout<<"stack is empty"<<endl;
	}
	for(int i=top;i>=0;i--)
	{
		cout<<" "<<arr[i]<<endl;
	}
}
int main()
{
	push(3);
	push(8);
	push(7);
	push(5);
	int val=pop();
	show();
	cout<<"poped value is : "<<val<<endl;
	
}
