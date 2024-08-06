#include<iostream>
using namespace std;
class base{
	public:
		int a,b;
		void getdata(){
			cout<<"Enter length and width: ";
			cin>>a>>b;
		
		}
		
	
		
		
};
class rect:public base{
	public:
	area(){
	cout<<"\n The area of the rectangle = "<<(a*b);
}
};
int main(){
	rect ob;
	ob.getdata();
	ob.area();
	return 0;
}
