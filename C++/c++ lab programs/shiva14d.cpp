#include<iostream>
using namespace std;
class side{
	public:
		int l;
		void setvalue(int x){
			l=x;
		}
};

class square:public side{
	public:
//		int sq;
		void sq(){
			cout<<"\n The square is: "<<(l*l);
		}
};

class cube:public square{
	public:
//		int z;
		cube1(){
			cout<<endl<<"The cube is: "<<(l*l*l);
		}
};

int main(){

     cube s;
    s.setvalue(5);
    s.sq();
    s.cube1();
	return 0;
}
