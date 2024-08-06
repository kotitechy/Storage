/*
caluclate the area and perimeter of the Rectangle
date-11-09-2022
*/
#include<stdio.h>
int main(){
	float l,b,a,p;
	printf("Enter the length ");
	scanf("%f",&l);
	printf("\n Enter the breadth  ");
	scanf("%f",&b);
	a = l * b;
	printf("\n The area of the rectangle is %f",a);
	p = 2*(l+b);
	printf("\n The perimeter of the rectangle is %f",p);
	return 0;
}
