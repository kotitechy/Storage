// 2d Array
#include<stdio.h>
//#include<conio.h>
int main(){
//	clrscr();
	int r, c, i, j;
//	printf("Enter No of Rows in Matrix: ");
//	scanf("%d",&r);
//	printf("Enter No of Columns in Matrix: ");
//	scanf("%d",&c);
//	int a[i][j];
//	for(i=0;i<r;i++){
//		for(j=0;j<c;j++){
//			printf("\n a[%d][%d]",a[i],a[j]);
//			scanf("%d",&a[i][j]);
//		}
//	}
	int a[2][2] = {12,13,14,15};
	printf("2D Matrix");
	for(i=0;i<2;i++){
		printf("\n");
		for(j=0;j<2;j++){
			printf("%d \t",a[i][j]);
		}
	}
	return 0;
}
