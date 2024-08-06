#include<iostream>
using namespace std;
#include<conio.h>
#include<stdlib.h>
int main(){
	char sentence[1000];
	int i,n;
	FILE *ptr;
	ptr=fopen("New Text.c","wb");
	if(ptr==NULL){
		cout<<"\n An error has occured"<<endl;
		exit (1);
	}
	cout<<"How many sentences do you want to write"<<endl;
	cin>>n;
	cout<<"\n Enter "<<n<<"sentences"<<endl;
	for(i=0;i<n;i++){
	fgets(sentence ,sizeof(sentence),stdin);
	fprintf(ptr,"%s",sentence);
	fclose(ptr);
	
                  }      
		
	return 0;
	
	
	
}
