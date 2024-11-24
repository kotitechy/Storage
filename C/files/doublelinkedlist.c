#include<stdio.h>
#include<stdlib.h>
struct node{
	int d;
	struct node * n;
	struct node *p;
};

void main(){
//	head
	struct node * h = malloc(sizeof(struct node));
	//	n1
	struct node * n1 = malloc(sizeof(struct node));
	//	n2
	struct node * n2 = malloc(sizeof(struct node));
	//	n3
	struct node * n3 = malloc(sizeof(struct node));
	//	n4
	struct node * n4 = malloc(sizeof(struct node));
	//	5
	struct node * n5 = malloc(sizeof(struct node));
	
	h->d=10;
	n1->d=20;
	n2->d=30;
	n3->d=40;
	n4->d=50;
	n5->d=60;

	h->n=NULL;
	h->p=NULL;

	n1->n=NULL;
	n1->p=NULL;

	n2->n=NULL;
	n2->p=NULL;

	n3->n=NULL;
	n3->p=NULL;

	n4->n=NULL;
	n4->n=NULL;

	n5->p=NULL;
	n5->p=NULL;

	h->n=n1;
	n1->n=n2;
	n2->n=n3;
	n3->n=n4;
	n4->n=n5;
	n5->n=NULL;

	h->p=NULL;
	n1->p=h;
	n2->p=n1;
	n3->p=n2;
	n4->p=n3;
	n5->p=n4;
	printf("\nTravesal-1");
	printf("\n%d ",h->d);
	printf("%d ",h->n->d);
	printf("%d ",h->n->n->d);
	printf("%d ",h->n->n->n->d);
	printf("%d ",h->n->n->n->n->d);
	printf("%d",n5->d);
	printf("\nReverse Traversal\n");
	printf("%d ",n5->d);
	printf("%d ",n5->p->d);
	printf("%d ",n5->p->p->d);
	printf("%d ",n5->p->p->p->d);
	printf("%d ",n5->p->p->p->p->d);
	printf("%d ",n5->p->p->p->p->p->d);

}
