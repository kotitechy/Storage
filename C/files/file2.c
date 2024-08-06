#include<stdio.h>
#include<stdlib.h>
void main(){
	FILE *fp;
	int ch;
	fp = fopen("txt1.txt","w");
//	if(fp == NULL){
//		printf("\n File doesnot exists!");
//		exit (0);
//	}
	{
		printf("\n Enter the text: ");
		//press ctrl + z to stop reading
		while((ch))
		fputc(ch,fp);
	}
	fclose(fp);
}
