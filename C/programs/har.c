/*
program to find  the entered character
date-11-09-2022
designed-by-nanibabu
*/
#include<stdio.h>
int main(){
	char ch;
	printf("Enter the character");
	scanf("%c",ch);
	printf("\n You entered %c",ch);
	if(ch>='a'&&ch<='z'){
		printf("\n lower case");
	}
	else if(ch>='A'&&ch<='Z'){
		printf("\n upper case");
	}
	else if(ch>='0'&&ch<='9'){
		printf("\n digit ");
	}
	else{
		printf("\n special charcter");
	}
	return 0;
}
