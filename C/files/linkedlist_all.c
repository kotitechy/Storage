#include<stdio.h>
#include<stdlib.h>

struct node{
	int data;
	struct node *next;
	
};

struct node*  create_node(int data){
    struct node * ptr = malloc(sizeof(struct node));
    ptr->data=data;
    printf("Initial Node Created");
    ptr->link=NULL;
    return ptr;
}
struct node* add_beg(int data,struct node *ptr1) {
    struct node * ptr = malloc(sizeof(struct node));
    ptr->data=data;
    printf("\n %d added",ptr->data);
    ptr->link=ptr1;
    return ptr;

}
struct node delete_l(struct node *head){
	struct node *temp = head;
	struct node *temp2 = head;
	if(head==NULL){
	printf("Head is Empty.\n");
	}else if(head->next==NULL){
		printf("%d is removed.\n",head->data);
		free(head);
	}else{
		while(temp!=NULL){
		temp2=temp;
		temp=temp->next;
	}
	printf("%d is removed.\n",temp2->data);
	temp2->next=NULL;
	free(temp);
	temp=NULL;
	}
	return *head;
}
struct node insert_b(int data,struct node *head){
	struct node *ptr = malloc(sizeof(struct node));
	ptr->data=data;
	ptr->next=NULL;
	head->next=ptr;
	return *head;
}


void display(struct node *head){
	if(head==NULL){
		printf("List is empty.\n");
	}else{
	printf("List elements are: ");
	while(head!=NULL){
		printf("%d\t",head->data);
		head=head->next;
	}
	printf("\n");
}
}



int main(){
	struct node *head = malloc(sizeof(struct node));
	insert(10,head);
//	insert(20,head);
//	delete_l(head);
	display(head);
	
	
	return 0;
}

