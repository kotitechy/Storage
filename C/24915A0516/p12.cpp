// Insert an Element to an Array
#include<stdio.h>
//#include<conio.h>
int main(){
//	clrscr();
	int n, i, j, pos = 0,num;
	printf("Enter size of array: ");
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++){
		printf("\n Enter array[%d]: ",i);
		scanf("%d",&a[i]);
	}
	printf("\n Enter an Number to be added to Array: ");
	scanf("%d",&num);
	printf("\n Enter an  position to be added in Array: ");
	scanf("%d",&pos);
	// Logic
	for(i=n-1;i>=pos;i--){
		a[i+1] = a[i];
		a[pos] = num;
		n = n+1;
	}
	
	printf("\n Array after Insertion");
	for(i=0;i<n;i++){
		printf("\n a[%d]: %d",i,a[i]);
	}
	
	return 0;
	
}
