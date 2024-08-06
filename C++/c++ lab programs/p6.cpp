
//constructors and destructors
#include<iostream>
using namespace std;

class student{
	private:
		int rollno;
		string name;
		float marks;
		
		public:
			void getdata();
			student();
			~student();
			void putdata();
			
};
void student::getdata(){
	cout<<endl<<"Enter the student details: ";
	cout<<endl<<"Rollno: ";
	cin>>rollno;
	cout<<endl<<"Name: ";
	cin>>ws>>name;
//	getline(cin,name);
	cout<<endl<<"Marks: ";
	cin>>marks;
}
student::student(){
	
	cout<<endl<<"constructor called "<<endl;
}
student::~student(){
	cout<<endl<<"destructor called "<<endl;
}
void student::putdata(){
	cout<<endl<<"The student details are: ";
	cout<<endl<<"Name  : "<<name;
	cout<<endl<<"Rollno: "<<rollno;
	cout<<endl<<"Marks : "<<marks;
}

int main(){
	
student ob;
//student();

ob.getdata();
ob.putdata();


return 0;
}
