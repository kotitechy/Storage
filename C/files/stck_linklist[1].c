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
	if(head==NULL){
		free(head);
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
struct node* deleteNode_beg(struct node *head){
	if(head==NULL){
		printf("List is empty.\n");
		head = NULL;
		return head;
	}
	struct node *temp = head;
	printf("%d Deleted from list.\n",head->data);
	head=head->link;
	free(temp);
	count--;
	return head;
}
struct node* deleteNode_spes(struct node *head, int ele){
	if(head == NULL){
		printf("List is empty.\n");
		head=NULL;
		return head;
	}
	if(head->data==ele){
		printf("%d deleted from list.\n",head->data);
		free(head);
		head=NULL;
		count--;
		return head;
	}else{
	struct node *temp,*temp1;
	temp = head;
	while(temp!=NULL && temp->data!=ele){
		temp1=temp;
		temp=temp->link;
	}
	printf("%d deleted from list.\n",temp->data);
	temp1->link=temp->link;
	free(temp);
	count--;
	return head;
	}
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
void rear(struct node *head){
	if(head==NULL){
		printf("List is empty.\n");
		return;
	}
	printf("%d is at rear.\n",head->data);
	return;
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
	struct node *head = malloc(sizeof(struct node));
	head=NULL;
	int ch,ele;
	while(1){
	printf("1.Insert 2. Delete_last 3. delete_beg 4. delete_item 5. Display 6. size 7. Top/Front 8. rear 9. IsEmpty 0. exit 11 . Clear_Screen : ");
	scanf("%d",&ch);
	switch(ch){
		case 1:
			printf("Element to Insert : ");
			scanf("%d",&ele);
			head = insertNode(head, ele);
			break;
		case 2:
			head = deleteNode_last(head);
			break;
		case 3:
			head = deleteNode_beg(head);
			break;
		case 4:
			printf("Element to Delete: ");
			scanf("%d",&ele);
			head = deleteNode_spes(head, ele);
			break;
		case 5:
			display(head);
			break;
		case 6:
			size();
			break;
		case 7:
			peek(head);
			break;
		case 8:
			rear(head);
			break;
		case 9:
			isEmpty();
			break;
		case 0:
			exit(0);
			break;
		case 11:
			system("cls");
			break;
		default:
			printf("Please choose an valid option.\n");
			break;
	}
	}
	return 0;
}
