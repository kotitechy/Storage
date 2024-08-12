// Delete an Element from given  Location
#include<stdio.h>
#include<conio.h>
int main(){
//	clrscr();
	int n, i, j, pos = 0;
	printf("Enter size of array: ");
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++){
		printf("\n Enter array[%d]: ",i);
		scanf("%d",&a[i]);
	}
	printf("\n Enter an  position to be deleted from Array: ");
	scanf("%d",&pos);
	// Logic
	for(i=pos;i<n-1;i++){
		a[i] = a[i+1];
		n--;
	}
	
	printf("\n Array after Deletion");
	for(i=0;i<n;i++){
		printf("\n a[%d]: %d",i,a[i]);
	}
	
	return 0;
	
}
