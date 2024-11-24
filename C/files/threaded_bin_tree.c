/* Binary Tree
1. Insert
2. Delete
3. Search
4. Display
5. Find MIn
6. Find Max
7. Size
*/

#include<stdio.h>
#include<stdlib.h> // for memeory allocation

struct node{
	int data;
	struct node *left;
	struct node *right;
};
int count;
struct node *Insert(struct node *root,int data){
	if(root==NULL){
		struct node *temp = malloc(sizeof(struct node));
		temp->data=data;
		temp->left=temp->right=NULL;
		return temp;
	}
	if(data==root->data){
		printf("Element already exists.\n");
		return root;
	}
	else if(data < (root->data)){
		root->left = Insert(root->left,data);
	}else{
		root->right = Insert(root->right,data);
	}
	return root;
}
void preorder(struct node *root){
	if(root!=NULL){
	printf("%d ",root->data);
	preorder(root->left);
	preorder(root->right);
	}
}
void postorder(struct node *root){
	if(root!=NULL){
	postorder(root->left);
	postorder(root->right);
	printf("%d ",root->data);
	}
}
void inorder(struct node *root){
	if(root!=NULL){
	inorder(root->left);
	printf("%d ",root->data);
	inorder(root->right);
	}
}
struct node* Search(struct node *root, int data){
	if(root==NULL || root->data==data){
		return root;
	}
	if(data > root->data)
		return Search(root->right,data);
	if(data < root->data)
		return  Search(root->left,data);
}
struct node* Min(struct node *root){
	int min;
	if(root == NULL){
		return root;
	}
	if(root->left){
		return Min(root->left);
	}
	return root;
	
}
struct node* Max(struct node *root){
	if(root==NULL ){
		return root;
	}
	if(root->right){
		return Max(root->right);
	}
	return root;
}

struct node* del_node(struct node *node,int ele){
	if(node==NULL) return node; 
	if(ele < node->data){
		node->left = del_node(node->left, ele);
	}else if(ele > node->data){
		node->right = del_node(node->right,ele);
	}else{
		if(node->left==NULL){
			struct node * temp = node->right;
			free(node);
			return temp;
		}else if(node->right==NULL){
			struct node * temp = node->left;
			free(node);
			return temp;
		}
		struct node*  temp = Min(node->right);
		node->data = temp->data;
		node->right = del_node(node->right, temp->data);
	}
	return node;
}
int main(){
	struct node *root=NULL,*temp;
	int ch,data;
	while(1){
		printf("1. Insert 2. Delete 3. Search 4. Display 5. Find_MIn 6. Find_Max 7. nodes 0. exit: ");
		scanf("%d",&ch);
		switch(ch){
			case 1:
				printf("Element to Insert: ");
				scanf("%d",&data);
				root = Insert(root,data);
				count++;
				printf("%d Inserted.\n",data);
				break;
			case 2:
					printf("Element to Delete: ");
				scanf("%d",&data);
				struct node * temp = Search(root,data);
				if(!temp){
					printf("Elemet not found in tree.\n");
				}else{
				root = del_node(root,data);
				printf("%d deleted from tree.\n",data);
				count--;
				}
				break;
			case 3:
				printf("Element to Search: ");
				scanf("%d",&data);
				temp = Search(root,data);
				if(!temp){
					printf("Elemet not found in tree.\n");
				}else{
					printf("Element Found in Tree.\n");
				}
				break;
			case 4:
				if(root==NULL){
					printf("Tree is empty.\n");
				}else{
					printf("Tree Traveral.\n");
					printf("Pre-order: ");
					preorder(root);
					printf("\n");
					printf("Post-order: ");
					postorder(root);
					printf("\n");
					printf("In-order: ");
					inorder(root);
					printf("\n");
				}
				break;
			case 5:
				temp = Min(root);
				if(temp==NULL){
					printf("Tree is empty.\n");
				}else{
					printf("%d is the min in tree.\n",temp->data);
				}
				break;
			case 6:
				temp = Max(root);
				if(temp==NULL){
					printf("Tree is empty.\n");
				}else{
					printf("%d is Max of Tree.\n",temp->data);
					break;
				}
			case 7:
				if(count<=0){
					printf("Tree has 0 nodes.\n");
					count=0;
			}
				else{
					printf("%d nodes in Tree.\n",count);
			}
			break;
			case 0:
				exit(0);
			case 9:
				system("CLS");
			default:
				printf("Enter valid option.\n");
				break;
		}
	}
}

//inorder acsencing order
