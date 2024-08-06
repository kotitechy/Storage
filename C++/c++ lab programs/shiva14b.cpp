#include<iostream>
using namespace std;
class a{
	public:
		int x;
		void getx(){
			cout<<"\n Enter x: ";
			cin>>x;
		}
};
class b{
	public:
		int y;
		void gety(){
			cout<<endl<<"Enter the y; ";
			cin>>y;
		}
};
class c:public a,public b{
	public: 
	void sum(){
		cout<<"\n The sum is: "<<(x+y);
	}
};
int main(){
	c ob1;
	ob1.getx();
	ob1.gety();
	ob1.sum();
}
