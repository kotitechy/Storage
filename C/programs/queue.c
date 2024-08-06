#include<stdio.h>
#include<stdlib.h>
int size=5;
int items[5];
void queue_op();
void enqueue();
void display();
void dequeue();

int front=-1,rear=-1,ch,i,value;

int main(){
	
	while(1){
		queue_op();
	switch(ch){
	case 1:
	enqueue();	
	break;
	case 2:
	dequeue();
	break;
	case 3:
	display();
	break;
	case 4:
	exit(0);

}
}

	return 0;
}
void enqueue(){
	printf("\n Enter the element to push: ");
	scanf("%d",&value);
	if(rear==size-1){
		printf("\n queue is full");
	}
	else{
		front = 0;
		rear++;
		items[rear]=value;
		printf("\n %d inserted",value);
	}
}
void dequeue(){
	if(front==-1){
		printf("\n queue is empty ");
		
	}
	
	else{
		printf("\n %d deleted",items[front]);
		front++;
		if(front>rear){
			front=rear=-1;
		}
			}
}

void queue_op(){
	printf("\n QUEUE OPERATIONS");
	printf("\n 1.enqueue");
	printf("\n 2.dequeue");
	printf("\n 3.display");
	printf("\n 4.exit");
	printf("\n Enter a choice: ");
	scanf("%d",&ch);
}

void display(){
	for(i=0;i<5;i++){
	printf("\t %d ",items[i]);
}
}
