/*
program to of employe monthly salary
date-11-09-2022
designed-by-shiva
*/
#include<stdio.h>
#include<conio.h>
int main(){
	
	int eno;
	char name[10],mon[0];
	float da,bs,ta,hra,it,pf,tot,net;
	/*
	da-                     5%         
	ta-transport charges    4%
	hra-house rent charges  8%
	it-                     2%
	pf-pension fund         12%
	bs-basic salary 
	tot-total 
	et-net worth
	*/
	printf("\n Enter the Emploooye name:");
	scanf("%s",&name);
		printf("\n Enter the month:");
	scanf("%s",&mon);
	printf("\n Enter the emplooye no:");
	scanf("%d",&eno);
	printf("\n Enter the emplooye salary:");
	scanf("%f",&bs);
	ta=bs*4/100;
	da=bs*5/100;
	hra=bs*8/100;
	tot=bs*12/100;
	it=bs*2/100;
	tot=bs+ta+da+hra+it+pf;
	net=tot-it-pf;
	
	    printf("\n The total salary is %f ",tot);
    	printf("\n The net   salary is %f ",net);
	    system("cls");
		printf("\n Employee progress of month- %s \n",mon);
		printf("|------------------------------------------------------------------------------|\n");
        printf("|ENO   |   EMP_NAME   |  TOTAL   |     NET     |     SALARY                    |\n");
        printf("|------------------------------------------------------------------------------|\n");
        printf("   %d         %s       %f        %f        %f               \n",eno,name,tot,net,bs);
        printf("|------------------------------------------------------------------------------|\n");
	    return 0;
}
