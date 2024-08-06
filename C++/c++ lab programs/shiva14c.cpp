#include<iostream>
using namespace std;
class base{
	public:
		int x;
		void getx(){
			cout<<"\n Enter x: ";
			cin>>x;
		}
};
class derived_1:public base{
	public:
		int y;
		void gety(){
			cout<<endl<<"Enter the y: ";
			cin>>y;
		}
};

class derived_2:public derived_1{
	public:
		int z;
		void getz(){
			cout<<endl<<"Enter the z: ";
			cin>>z;
		}
		void product(){
			cout<<"\n product of "<<x<<" , "<<y<<" , "<<z<<" is: "<<(x*y*z);
		}
};

int main(){
	derived_2 a;
	a.getx();
	a.gety();
	a.getz();
	a.product();
	return 0;
}
