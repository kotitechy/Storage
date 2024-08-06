/*
program to display the swaping of two numbers
date-11-09-2022
*/
#include<stdio.h>
//#include<conio.h>
int main(){
//	clrscr();
    int a,b,c;
    printf("Enter the a,b values: \t");
    scanf("%d %d",&a,&b);
    printf("\n values before swaping \n a   b ");
    printf("\n %d   %d",a,b);
    //swaping the nubers
    //method-1
    
	c=a;  
    a=b;
    b=c;
    //method-2
     /* a=a+b;
	  a=a-b;
	  b=a;*/
	
	//method-3
	/*
	a=a*b;
	a=a/b;
	b=a/b;
	*/
    printf("\n values After swaping \n a   b ");
    printf("\n %d   %d",a,b);
    
	return 0;
}
