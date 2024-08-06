/*
student progress card 
date-11-09-2022
*/
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int main(){
int roll,n,i,op;
int m[10],sum=0;
float average ;
char name[20];
int rem;
printf("\n Enter the students name ");
scanf("%s",&name);
printf("\n Enter the students roll ");
scanf("%d",&roll);
printf("How many subjects do you want ");
scanf("%d",&n);
printf("\n Enter the %d marks \n",n);
for(i = 1 ; i <= n ; i++)
{
	printf("\n Enter sub-%d marks  ",i);
    scanf("%d",&m[i]);
}
printf("\n Printing the marks ");
for(i = 1; i <= n; i++){
	printf("\n sub-%d",m[i]);
	sum+=m[i]; 
}
average=(sum/n);
for(i=1;i<n;i++){

if(m[i]<40){
	rem=1;
}
else if(rem>=40){
	rem=0;
}
}
        system("cls");
		printf("\n PROGESS CARD \n");
		printf("|--------------------------------------------------------------------|\n");
        printf("|ROLLNO   |   STU_NAME   |  TOTAL   |    AVERAGE      |  REMARKS     |\n");
        printf("|--------------------------------------------------------------------|\n");
        printf("   %d          %s           %d           %f         promoted     \n",roll,name,sum,average,rem);
        printf("|--------------------------------------------------------------------|\n");
        if(rem==0){
        printf("|-----------|\n");
     	printf("|   PASS    |\n");
     	printf("|-----------|\n");
        }
        else if(rem==1){
        printf("|-----------|\n");
     	printf("|   FAIL    |\n");
     	printf("|-----------|\n");
} 

	return 0;
}
