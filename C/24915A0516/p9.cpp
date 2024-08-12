// program to read and display an array
#include<stdio.h>
int main(){
	int n, i;
	printf("Enter size of array: ");
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++){
		printf("Enter array[%d]: ",i);
		scanf("%d",&a[i]);
	}
	printf("Displaying Array Elements");
	for(i=0;i<n;i++){
		printf("\n a[%d]: %d",i,a[i]);
	}
	return 0;
}
