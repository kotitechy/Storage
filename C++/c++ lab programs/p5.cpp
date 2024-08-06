//objects and classes
#include<iostream>
using namespace std;

class student{
	private:
		int rollno;
		string name;
		float marks;
		
		public:
			void getdata();
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

void student::putdata(){
	cout<<endl<<"The student details are: ";
	cout<<endl<<"Name  : "<<name;
	cout<<endl<<"Rollno: "<<rollno;
	cout<<endl<<"Marks : "<<marks;
}

int main(){
	
student ob;

ob.getdata();
ob.putdata();


return 0;
}
