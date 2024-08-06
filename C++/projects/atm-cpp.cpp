#include<iostream>
using namespace std;


class details{
	public:
	int ifsc = 230;
		int ac_no;
		string holder_name;
		string gender;
		int ac_bal=0;
		int pass;
		string ac_type;
		public:
		void interface(){
			int ch1;
				
				cout<<endl<<"choose any of the service";
				cout<<endl<<"1.Major ac for adult";
				cout<<endl<<"2.Minor ac for child"<<endl;
				cin>>ch1;
			     if(ch1==1){
				 ac_type="MAJOR";
			}
			else if(ch1==2){
				ac_type="MINOR";
			}
		}
		void get_details(){
		
	 	cout<<endl<<"Enter ac_holder name     : ";
	 	cin>>holder_name;
	 	cout<<endl<<"Enter your gender        : ";
	 	cin>>gender;
	 	cout<<endl<<"Create a 8-digit password: ";
		cin>>pass;
	 }
		
};
class ac_s :public details {
	public:
		
		void cre_pass();
		void check_pass();
		void ac_pass_book();
		
	
};
        void ac_s :: cre_pass(){
		
		int pass_2;
		cout<<endl<<"Renter the password to confrom: ";
		cin>>pass_2;
		if(pass != pass_2){
			cout<<endl<<"Something went try again...";
		}
		else{
			cout<<endl<<"Succesfully created password...";
		}
		}
   
   void ac_s :: check_pass(){
   	int check_pass;
   	cout<<endl<<"Enter your 8-digit password:     ";
   	cin>>check_pass;
   	if(check_pass != pass){
   		cout<<endl<<"Incorrect! password try again...";
   		exit (0);
	   }
	   else{
	   	cout<<endl<<"Correct password!....";
	   }
   }
   
   void ac_s :: ac_pass_book(){
   	check_pass();
   	
    cout<<endl<<"ACCOUNT CREATED SUCCESFULLY!..  DETAILS ARE BELOW:";
   	cout<<endl<<"PASS BOOK KTC BANK ";
   	cout<<endl<<"AC_NUMBER: "<<ac_no;
   	cout<<endl<<"BRANCH   : ******"<<ifsc;
   	cout<<endl<<"NAME     : "<<holder_name;
   	cout<<endl<<"AC_TYPE  : "<<ac_type;
   	cout<<endl<<"GENDER   : "<<gender;
   	cout<<endl<<"BALANCE  : "<<ac_bal;
   }
   

   class services :public ac_s{
   	public:
   		int dp_amount;
   		int wd_amount;
   		
   		void deposit(){
   	check_pass();
   	cout<<endl<<"Enter the amonut to deposit: ";
   	cin>>dp_amount;
   	
   	if(dp_amount < 1000){
   		cout<<endl<<"Minimum amonut is RS-1000  ";
   		
	   }
	   else if(dp_amount > 1000){
	   	ac_bal+=dp_amount;
	   	cout<<endl<<"Deposited Rs-"<<dp_amount<<" in ac_no ";
	   }
   }
   		void with_draw(){
   	check_pass();
   	cout<<endl<<"Enter the amonut to withdraw:  ";
   	cin>>wd_amount;
   	if(wd_amount > (ac_bal-1000) || wd_amount < 500 || ac_bal == 0){
   		cout<<endl<<"Insufficient Balance!...;";
	   }
	   else{
	   	ac_bal-=wd_amount;
	   	cout<<endl<<"With drawed RS-"<<wd_amount;
	   }
   }
   		void check_bal(){
   			ac_pass_book();
		   }
   		void services_menu1(){
			cout<<endl<<"ACCOUNT REGISTRATION MENU ";
						interface();
						system("cls");
						get_details();
						system("cls");
						cre_pass();
		}
		void services_menu2();
};
			void services::services_menu2(){
				int ch2;
				while(1){
				cout<<endl<<"1.DEPOSIT AMOUNT";
				cout<<endl<<"2.WITH-DRAW AMOUNT";
				cout<<endl<<"3.CHECK-BALANCE";
				cout<<endl<<"Choose any option: ";
				cin>>ch2;
				switch(ch2){
					case 1:
						system("cls");
						deposit();
						break;
						
						case 2:
							system("cls");
							with_draw();
							break;
							case 3:
							system("cls");
							check_bal();
							default :
								exit(0);
				}
			}
				
			}
			
			
int main(){
	services ob,ob1,ob2;
	int acv;
	while(1){
	while(1){
	cout<<endl<<"1.SHIVA CHARAN "<<endl<<"2.VAMSHI "<<endl<<"3.RAMESH";
	cin>>acv;
	if(acv=1){

	while(1){
	int i;
	cout<<endl<<"Welcome to ktc bank";
	cout<<endl<<"1.REGISTER AN ACCOUNT"<<endl<<"2.SERVICES :  ";
	cin>>i;
      switch(i){
      	case 1:
      	ob.services_menu1();
//      	break;
      		case 2:
      	ob.services_menu2();
//      	break;
      		default :
      				exit (0);
	  }
}
}
	else if(acv=2){
		ob1.ifsc = 11101232;
	while(1){
	int i;
	cout<<endl<<"Welcome to ktc bank";
	cout<<endl<<"1.REGISTER AN ACCOUNT"<<endl<<"2.SERVICES :  ";
	cin>>i;
      switch(i){
      	case 1:
      	ob1.services_menu1();
//      	break;
      		case 2:
      	ob1.services_menu2();
//      	break;
      		default :
      				exit (0);
	  }
}
}

else if(acv=3){
ob2.ifsc = 11101233;
	while(1){
	int i;
	cout<<endl<<"Welcome to ktc bank";
	cout<<endl<<"1.REGISTER AN ACCOUNT"<<endl<<"2.SERVICES :  ";
	cin>>i;
      switch(i){
      	case 1:
      	ob2.services_menu1();
//      	break;
      		case 2:
      	ob2.services_menu2();
//      	break;
      		default :
      				exit (0);
	  }
}
}
}
}
	return 0;

}
