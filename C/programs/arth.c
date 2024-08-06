/*
dispalying the arthematic operations
*/
#include<stdio.h> //header files
//#include<conio.h>
int main(){
	int a,b;
	//clrscr();
	printf("Enter  value of a: \t");
	scanf("%d",&a);
		printf("Enter  value of b: \t");
	scanf("%d",&b);
	printf("\n The sum of %d  , %d    =   %d",a,b,a+b);
    printf("\n The sub of %d  , %d    =   %d",a,b,a-b);
	printf("\n The div of %d  , %d    =   %d",a,b,a/b);
	printf("\n The mul of %d  , %d    =   %d",a,b,a*b);
	printf("\n The sub of %d  , %d    =   %d",a,b,a%b);
	printf("\n Increment  a++         =   %d",a++);
	printf("\n Increment  a++         =   %d",++a);
	printf("\n Increment  a++         =   %d",a--);
	printf("\n Increment  a++         =   %d",--a);
	return 0;

}
 
