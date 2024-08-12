#include<stdio.h>
int main(){
	// Arithmetic operators
	int a ,b;
	printf("Enter a and b : ");
	scanf("%d %d", &a,&b);
	
	printf(" %d + %d = %d",a,b,a+b);
	printf("\n %d - %d = %d",a,b,a-b);
	printf("\n %d * %d = %d",a,b,a*b);
	printf("\n %d / %d = %d",a,b,a/b);
	printf("\n %d %. %d = %d",a,b,a%b);	
	return 0;
}
