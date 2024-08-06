#include<stdio.h>
#include<stdlib.h> 

int main(){
	
	FILE *ptr;
	char array[1000];
	float marks;
	int i,id,n;
	
	printf("\n Enter the na value");
	scanf("%d",&n);
	
	ptr= fopen("test.txt","a+b");

    for (i=0;i<100;i++){
	
	fscanf(ptr, "%s",array);
	
	id = atoi(array);
	
	if(id==n){
		fgets(array, 255 ,(FILE*)ptr);
		printf("%s",array);
		break;
	}
	
	
}
	
	
	return 0;
}
