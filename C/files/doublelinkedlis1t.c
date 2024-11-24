#include<stdio.h>
#include<stdlib.h>
int count=0;
struct node{
	int data;
	struct node *next,*prev;
};


struct node* insertNode_end(struct node* head, int ele){
	struct node *node = malloc(sizeof(struct node));
	struct node *last=head;
	
	node->data=ele;
	node->next=NULL;
	if(head==NULL){
		node->prev=NULL;
		head=node;
		return head;
	}
	else{
		while(last->next!=NULL){
			last=last->next;
		}
		last->next=node;
		node->prev=last;
	}
}
struct node* insertNode_beg(struct node* head, int ele){
	struct node *node = malloc(sizeof(struct node));
	node->data=ele;
	node->prev=NULL;
	node->next=head;
	if(head != NULL){
		head->prev=node;
	}
	head=node;
	printf("%d inserted.\n",ele);
	return head;
}


struct node* deleteNode_last(struct node* head){

}
struct node* deleteNode_beg(struct node *head){

}
struct node* deleteNode_spes(struct node *head, int ele){

}
void peek(struct node *head){
	if(head==NULL){
		printf("Stack is underflow.\n");
	}else{	
		while(head->next!=NULL){
			head=head->next;
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

struct node* ins_beg(struct node *head, int ele){
	struct node *node=malloc(sizeof(struct node));
	node->data=ele;
	node->next=node->prev=NULL;
	if(head==NULL){
		head = node;
	}
	 else{
	head->prev=node;
	node->next=head;
	head=node;
	}
	return head;
}
struct node* ins_last(struct node *head,int ele){
	struct node *node = malloc(sizeof(struct node));
	node->data=ele;
	node->next=node->prev=NULL;
	if(head==NULL){
		head=node;
	}
	 else{
	struct node *last=head;
	while(last->next!=NULL){
		last=last->next;
	}
	head->next=node;
	node->prev=last;
	}
	return head;
}

void display(struct node* head){
   if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    // Display in forward direction
    printf("Forward: ");
    struct node *temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");

    // Display in reverse direction
    // Find the last node first
    temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }

    printf("Reverse: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->prev;
    }
    printf("\n");
}
int main(){
	struct node *head = malloc(sizeof(struct node));
	head=NULL;
	int ch,ele;
	while(1){
	printf("1.Insert 2. Insert_last 3. delete_beg 4. delete_item 5. Display 6. size 7. Top/Front 8. rear 9. IsEmpty 0. exit 11 . Clear_Screen : ");
	scanf("%d",&ch);
	switch(ch){
		case 1:
			printf("Element to Insert : ");
			scanf("%d",&ele);
			head = ins_beg(head, ele);
			break;
		case 2:
			printf("Element to Insert : ");
			scanf("%d",&ele);
			head = ins_last(head, ele);
			break;
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
