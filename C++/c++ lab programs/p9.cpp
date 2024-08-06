
//passing objects as function arguments
//pass by value and pass by reference
#include<iostream>
using namespace std;
class example{
public:
int a;
			
		public:
			void add(example e){
			a=a+e.a;	
			}
			
};

int main(){
example e1,e2;
e1.a=10;
e2.a=20;

cout<<"\n Initial values "<<endl;
cout<<"values of object-1: "<<e1.a;
cout<<endl<<"values of object-2: "<<e2.a;


return 0;
}

