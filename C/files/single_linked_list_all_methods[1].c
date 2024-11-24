#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node * link; 
};
struct node* create_node(int data);
struct node* add_beg(int data,struct node *ptr1);
struct node* del_beg(struct node *ptr);
void traversal(struct node *ptr);
//struct node(int data,struct node *ptr);
int main(){
    struct node* head = NULL;
    int ch,data;
    printf("\n LINKED LIST\n");
	while(1){
		printf("\n 1. push \n 2. pop \n 3. printall items \n 4. exit \n");
		scanf("%d",&ch);
		switch(ch){
			case 1:
				printf("\n Enter item to push:  ");
				scanf("%d",&data);
				head = add_beg(data, head);
				break;
			case 2:
    			head = del_beg(head);
    			break;
    		case 3:
				traversal(head);
				break;
			case 4:
				printf("\n Final list is\n");
				traversal(head);
				exit(0);
				break;
			default:
				printf("\nselect valid case\n");
				break;
		}
	}
    
    return 0;
}

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
void traversal(struct node *ptr){
	printf("\nElements in Linked list\n");
	if(ptr==NULL){
		printf("\n List is empty\n");
	}else{
    while(ptr!=NULL){
        printf("%d\t",ptr->data);
        ptr= ptr->link;
    }
}
}
struct node*  del_beg(struct node *ptr){
	if(ptr==NULL){
		printf("\nList is empty!");
		return NULL;
	}else{
	struct node * temp = ptr;
	printf("%d is deletd from list",ptr->data);
	ptr=temp->link;
	free(temp);
	temp = NULL;
	return ptr;
	}
}
//
//struct node(int data,struct node *ptr){
//	struct node *ptr = malloc(sizeof(struct node));
//	struct node *temp = malloc(sizeof(struct node));
//}
