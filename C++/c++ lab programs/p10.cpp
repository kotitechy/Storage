#include<iostream>
using namespace std;

class distance{
	public:
		int feet,inch;
		
		distance(int f , int i){
			this->feet=f;
			this->inch=i;
		}
		void operator -(){
			feet--;
			inch--;
			cout<<endl<<"Feet: "<<feet<<endl<<"Inch: "<<inch;
		}
};
int main(){
	distance d1(8,9);
	-d1;
	
	return 0;
}
