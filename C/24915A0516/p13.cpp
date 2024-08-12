// Merge two unsorted Arrays
#include<stdio.h>
//#include<conio.h>
int main(){
//	clrscr();
	int n1, n2, i, j;
	printf("Enter size of array1: ");
	scanf("%d",&n1);
	int a1[n1];
	printf("Enter Array-1 Elements: ");
	for(i=0;i<n1;i++){
		printf("\n arr-1[%d]: ",i);
		scanf("%d",&a1[i]);
	}
	printf("Enter size of array2: ");
	scanf("%d",&n2);
	int a2[n2];
	printf("Enter Array-2 Elements: ");
	for(i=0;i<n2;i++){
		printf("\n Enter arr-2[%d]: ",i);
		scanf("%d",&a2[i]);
	}
	int n3 = n1 + n2;
	int a3[n3];
	printf("\n new array  size: %d",n3);
	// a3 <- a1
	for(i=0;i<n1;i++){
		a3[i] = a1[i];
	}
	// a3 <- a2
	j=0;
	for(i=n1;i<n3;i++){
		a3[i] = a2[j];
		j+=1;
	}
	printf("\n Array-3: \n [");
	for(i=0;i<n3;i++){
	printf("%d,",a3[i]);
	}
	printf("]");
	
	return 0;
}
