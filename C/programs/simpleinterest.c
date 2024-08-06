/*
caluclate the simple intrest 
date-11-09-2022
*/
#include<stdio.h>
int main(){
	 float p,t,r,i;
	 printf("Enter the principle amount ");
	 scanf("%f",&p);
	 printf("Enter the time period ");
	 scanf("%f",&t);
	 printf("Enter the rate of intrest  ");
	 scanf("%f",&r);
	 i = (p*t*r)/100;
	 printf("The simple intrest is %f",i);
	 
	 return 0;
	
}
