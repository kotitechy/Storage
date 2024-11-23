#include<stdio.h>
#include<stdlib.h>
#define max 5

struct Graph{
	int adj[max][max];
	char data;
    char vertices[max];
};

void initG(struct Graph *g){
	int i,j;
	for(i =0;i<max;i++){
	for(j =0;j<max;j++){
		g->adj[i][j]=0;
	}
    g->vertices[i]='\0';
	}
	g->data='\0';
	printf("Adjacency Matrix Initial \n");
	for(i =0;i<max;i++){
	for(j =0;j<max;j++){
		printf("%d ",g->adj[i][j]);
		}
		printf("\n");
	}
}

void set_path(struct Graph *g, int i , int j){
	g->adj[i][j]=1;
    printf("Adjacency Matrix Initial \n");
	for(i =0;i<max;i++){
	for(j =0;j<max;j++){
		printf("%d ",g->adj[i][j]);
		}
		printf("\n");
	}
}
int main(){
	struct Graph g;
    int ch,i,j;
    char data;
    while(1){
    	printf("1. Initial 2. set_path 3. display 4. exit\n");
        scanf("%d",&ch);
        switch(ch){
        	case 1:
				initG(&g);
            	break;
            case 2:
            	printf("Enter i");
            	scanf("%d",&i);
            	printf("Enter j");
    		    scanf("%d",&j);
                printf();
	            set_path(*g,i,j);
                break;
        }
    }
    
	return 0;
}
