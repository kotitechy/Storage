// Find Duplicates in an Array
#include<stdio.h>
int main(){
	int n, i, j, flag = 0;
	printf("Enter size of array: ");
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++){
		printf("\n Enter array[%d]: ",i);
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			if (a[i] == a[j] && i!= j){
				flag = 1;
				printf("\n Duplicates Found at locations %d and %d",i,j);
			}
			}
		if(flag==0){
				printf("\n No Duplicates Found");
		}
	}
	return 0;
}
