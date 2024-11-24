#include<stdio.h>
#include<stdlib.h>
struct bin_tree{
	int data;
	struct bin_tree *right;
	struct bin_tree *left;
};


struct bin_tree* create_node( int ele) {
    struct bin_tree *node = malloc(sizeof(struct bin_tree));
    if (!node) {
        printf("Memory allocation failed\n");
        exit(1);  // Exit if memory allocation fails
    }
    node->data = ele;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct bin_tree* insert_n(struct bin_tree *tree, int ele) {
    if (tree == NULL) {
        return create_node(ele);
    }

    if (ele < tree->data) {
        tree->left = insert_n(tree->left, ele);
    } else if (ele > tree->data) {
        tree->right = insert_n(tree->right, ele);
    }

    return tree;
}

void print(struct bin_tree *tree){
	if(tree){
	printf("%d ",tree->data);
	printf("%d ",tree->left->data);
	printf("%d ",tree->right->data);
	}else{
		printf("Tree is empty.\n");
	}
}
int main(){
	
struct bin_tree *tree = NULL;
	int ch,ele;
	tree = insert_n(tree,10);
	insert_n(tree,11);
	insert_n(tree,12);
	printf("%d ",tree->data);
	if (tree->left != NULL)
	printf("%d ",tree->left->data);
	if (tree->right != NULL)
	printf("%d ",tree->right->data);
	return 0;

}

