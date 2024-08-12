// Display 3X3 Matrix
#include<stdio.h>
//#include<conio.h>
int main(){
//	clrscr();
	int r, c, i, j;
	int a[3][3] = {12,13,14,15,16,17,18,19,20};
	printf("3X3 Matrix ");
	for(i=0;i<3;i++){
		printf("\n");
		for(j=0;j<3;j++){
			printf("%d \t",a[i][j]);
		}
	}
	return 0;
}
