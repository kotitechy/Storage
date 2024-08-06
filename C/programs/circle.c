/*
caluclate the area and circumference of the cirlce
date-11-09-2022
*/
#include<stdio.h>
  //global variable
int main()
{
	int r;//local varibles
	float pi = 3.14;
	float area;
	float circum;
	printf("\n Enter the ardius of circle:  ");
	scanf("%d",&r);
	area = pi * r * r;
	circum = 2 * pi* r;

	printf("\n The AREA of the circle  = %f",area);
	printf("\n The Circumference  of the circle  = %f",circum);
	return  0;
}
