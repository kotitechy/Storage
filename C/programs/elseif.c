/*
program to show person eligible to vote or not
date-11-09-2022
designed-by-shiva
*/
#include<stdio.h>
#include<conio.h>
int main(){
	int age ;
	printf("Enter your age");
	scanf("%d",&age);
	if(age<18){
		printf("\n Age %d is not eligible to vote",age);
		
	}
	else {
		printf("\n You can vote");
	}
	return 0;
}
