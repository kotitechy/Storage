//shivacharan
//friend function to access member-data two objects

#include<iostream>
using namespace std;

class a{
	private:
		int x;
	
		public:
         void getx()
		 {
		 	cout<<endl<<"Enter x: ";
		 	cin>>x;
		 	friend void sum(a ob1,b ob2);
		 }
		 				
};
class b{
	private:
		int y;
		public:
			void gety(){
				cout<<endl<<"Enter y value: ";
				cin>>y;
				
			}
	friend int sum(a ob1,b ob2){
	int s;
	s=ob1.getx()+ob2.gety();
	cout<<endl<<"The sum is "<<s<<endl;
return 0;
}
};
//b::sum(a ob1,b ob2)

int main(){
	a ob1;
	b ob2;
	ob1.getx();
	ob2.gety();
	sum(ob1,ob2);
	
	return 0;
}
