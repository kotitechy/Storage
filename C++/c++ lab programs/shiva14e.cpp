#include<iostream>
using namespace std;
class student{
	public:
		int roll;
		void getno(int a){
		roll=a;
		}
		void putno(){
			cout<<endl<<"Enter roll no: ";
		}
};
class test:public student{
	public:
		float sub1,sub2;
		void getmarks(){
			
			cout<<endl<<"Enter the sub1 marks: ";
			cin>>sub1;
			cout<<endl<<"Enter the sub2 marks: ";
			cin>>sub2;
		}
};

class sports{
	public:
		float score;
		void getscore(){
			cout<<"\n Enter score: ";
			cin>>score;
		}
		void score1(){
			
			cout<<"\n The score is: "<<score;
		}
		
		
};

class result:public test ,public sports{
	public:
	void total(){
			int total = sub1+sub2+score;
						cout<<"\n The total score is: "<<total;
	}
	
};

int main(){
	result r;
	r.getno(1124);
	r.getmarks();
	r.getscore();
	r.score1();
	r.total();
	return 0;
}
