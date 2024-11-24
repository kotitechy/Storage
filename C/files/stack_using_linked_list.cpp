#include<stdio.h>
#include<stdlib.h>
int count=0;
struct node{
	int data;
	struct node *link;
};

struct node* createNode(int ele){
	struct node *temp = malloc(sizeof(struct node));
	temp->data=ele;
	temp->link=NULL;
	return temp;
}
struct node* insertNode(struct node* head, int ele){
	struct node *temp = createNode(ele);
	if(head==NULL){
		head = temp;
	}else{
		struct node *current = head;
		while(current->link!=NULL){
			current = current->link;	
		}
		current->link=temp;
	}
	printf("%d added to list.\n",ele);
	count++;
	return head;
}


void display(struct node* head){
	if(head==NULL){
		printf("List is empty.\n");
		return;
	}
	printf("Elements in the list are: ");
	struct node * temp = head;
	while(temp!=NULL){
		printf("%d ",temp->data);
		temp=temp->link;
	}
	printf("\n");
}
struct node* deleteNode_last(struct node* head){
	if(head == NULL){
		printf("List is empty.\n");
		head=NULL;
		return head;
	}
	if(head->link==NULL){
		free(head);
		count--;
		return NULL;
	}
	struct node *temp = head;
	struct node *temp1 = head;
	while(temp->link!=NULL){
		temp1=temp;
		temp=temp->link;
	}
	temp1->link=NULL;
	printf("%d deleted from list.\n",temp->data);
	free(temp);
	count--;
	return head;
}

void peek(struct node *head){
	if(head==NULL){
		printf("Stack is underflow.\n");
	}else{	
		while(head->link!=NULL){
			head=head->link;
		}
		printf("%d is at top.\n",head->data);
	}	
}
void size(){
	if(count<=0){
		count=0;
	}
	printf("Size of list is %d.\n",count);
	
}
void isEmpty(){
	if(count<=0){
		printf("List is Empty.\n");
		return;
	}
	else{
		printf("list is not empty.\n");
		return;
	}
}
int main(){
	struct node *head = NULL;
	head=NULL;
	int ch,ele;
	while(1){
	printf("1.PUSH 2. POP 3. DISPLAY 4. SIZE 5. TOP  6. IsEmpty 7. exit 8. Clear_Screen : ");
	scanf("%d",&ch);
	switch(ch){
		case 1:
			printf("Element to PUSH : ");
			scanf("%d",&ele);
			head = insertNode(head, ele);
			break;
		case 2:
			head = deleteNode_last(head);
			break;

		case 3:
			display(head);
			break;
		case 4:
			size();
			break;
		case 5:
			peek(head);
			break;
		case 6:
			isEmpty();
			break;
		case 7:
			exit(0);
			break;
		case 8:
			system("cls");
			break;
		default:
			printf("Please choose an valid option.\n");
			break;
	}
	}
	return 0;
}
