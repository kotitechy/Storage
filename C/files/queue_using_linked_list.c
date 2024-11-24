#include<stdio.h>
#include<stdlib.h>
struct queue{
	int data;
	struct queue *next;
};
typedef struct queue *Q;
Q front = NULL,rear=NULL;
void insert(){
	struct queue *node = malloc(sizeof(struct queue));
	int data;
	printf("insert Element: ");
	scanf("%d",&data);
	node->data=data;
	node->next=NULL;
	
	if(front == NULL &&rear == NULL){
		front = rear =node;
		printf("%d inserted to queue.\n");	
	}else{
		rear->next=node;
		rear=node;
		printf("%d inserted to queue.\n");	
		}

}
void delete(){
	if(front == NULL && rear==NULL){
		printf("Queue is empty.\n");
		return;
	}
	struct node *temp=front;
	printf("%d is deleted from Queue.\n",front->data);
	front=front->next;
	free(temp);
	temp=NULL;
	if(front ==NULL){
		rear=NULL;// now front and rear = null means queue is empty
	}
	
}
void display(){
	if(front == NULL && rear == NULL){
		printf("Queue is empty.\n");
		return;
	}
	struct queue *node =front;
	printf("Queue elements are: ");
	while(node != NULL){
		printf("%d ",node->data);
		node=node->next;
	}
	printf("\n");
}
void isempty(){
	
	if(front== NULL && rear == NULL){
		printf("Queue is underflow.\n");
	}else{
		printf("Queue is not empty.\n");
	}
}
void size(){
	if(front == NULL && rear == NULL){
		printf("size = 0");
		return;
	}
	struct queue *node =front;
	int count=0;
	while(node != NULL){
		count++;
		node=node->next;
	}
	printf("Queue size = %d.\n",count);
}
int main(){
	int ch;
	while(1){
	printf("1. insert 2. delete 3. display 4. isempty 5. size 6. exit\n");
	printf("Enter a choice: ");
	scanf("%d",&ch);
	switch(ch){
		case 1:
			insert();
			break;
		case 2:
			delete();
			break;
		case 3:
			display();
			break;
		case 4:
			isempty();
			break;
		case 5:
			size();
			break;
		case 6:
			exit(0);
	}
	}
	return 0;
}
