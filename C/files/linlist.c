#include<stdio.h>
#include<stdlib.h>
struct node{
	int d;
	struct node * link;
};

void main(){
//	head
	struct node * h = malloc(sizeof(struct node));
	h->d=10;
	h->link=NULL;
	printf("%d",h->d);
//	node-2
	struct node *a = malloc(sizeof(struct node));
	a->d=20;
	h->link=a;
	a->link=NULL;
	printf("%d",h->link->d);
//	node-3
	struct node *b = malloc(sizeof(struct node));
	b->d=30;
	b->link=NULL;
	a->link=b;
	printf("\n %d",h->link->link->d);
}
