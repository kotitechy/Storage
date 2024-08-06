#include<iostream>
using namespace std;

class a{
	public:
		int a1;
};

class b:public virtual a{
	public:
		int a2;
};

class c:public virtual a{
	public:
		int a3;
};
class d:public b,public c{
	public:
int a4;
void get(){
	cout<<"\n Enter a1,a2,a3,a4 values: ";
	cin>>a1>>a2>>a3>>a4;
}
void put(){
	cout<<"\n a1= "<<a1
	<<"\n a2= "<<a2
    <<"\n a3= "<<a3
    <<"\n a4= "<<a4;
}
};

int main(){
	d ob;
	ob.get();
	ob.put();
}
