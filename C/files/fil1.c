#include<stdio.h>
void main(){
	FILE *fp;
	int ch;
	fp = fopen("txt.txt","w");
	for(ch=65;ch<91;ch++){
		fputc(ch,fp);  //puts characters with the above ch
	}
	fclose(fp);
}
