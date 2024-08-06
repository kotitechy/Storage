#include<stdio.h>
#include<stdlib.h>
int top=-3,n,ch,elt,s[12],i;
void stack(){

	
	printf("\n Enter the size of the stack: ");
	scanf("%d",&n);

}
void stack_op(){
		printf("\n STACK OPERATIONS");
	printf("\n 1.push");
	printf("\n 2.pop");
	printf("\n 3.display");
	printf("\n exit");
	printf("\n Enter a choice: ");
	scanf("%d",&ch);
}
void push(){
	printf("\n Enter the element to push: ");
	scanf("%d",&elt);
	if(top<n-1){
		s[++top]=elt;
		printf("\n %d PUSHED TO STACK",s[top]);
	
	}
	else{
		printf("\n STACK IS FULL");
		
	}
}
void pop(){
//	printf("\n ENTER THE ELEMENT TO POP:  ");
//    scanf("%d",&elt);
    if(top<0){
    	printf("\n STACK IS EMPTY");
    	
	}
	else{
		printf("\n popped %d!...",s[top--]);
			}
}
   void display(){
	for(i=0;i<n;i++){
			printf("\t %d ",s[i]);
		}
		
	}
	void exit1(){
		exit(0);
	}
int main(){
	stack();
	while(1){
		stack_op();
	switch(ch){
	case 1:
  	push();
  	break;
  	case 2:
  	pop();
  	break;
  	case 3:
  	display();
  	break;
  	case 4:
  	exit1();
}
//system("cls");
}
	return 0;
}
