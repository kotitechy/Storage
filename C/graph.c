#include<stdio.h>
#include<stdlib.h>
#define max 7
#include <stdbool.h>

struct Graph{
	int adj[max][max];
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
	printf("Graph Resetted Sucessfully.\n");
}

void set_data(struct Graph *g){
    int data[max][max] = {
        {0, 0, 1, 1, 1, 0, 0},
        {0, 0, 1, 0, 0, 1, 0},
        {1, 1, 0, 0, 1, 1, 1},
        {1, 0, 0, 0, 0, 0, 0},
        {1, 0, 1, 0, 0, 0, 0},
        {0, 1, 1, 0, 0, 0, 0},
        {0, 0, 1, 0, 0, 0, 0}
    };
    int i,j;
    for(i = 0; i < max; i++){
        for(j = 0; j < max; j++){
            g->adj[i][j] = data[i][j];
        }
    }
    g->vertices[0] = 'a';
    g->vertices[1] = 'b';
    g->vertices[2] = 'c';
    g->vertices[3] = 'd';
    g->vertices[4] = 'e';
    g->vertices[5] = 'f';
    g->vertices[6] = 'g';
    printf("Vertices set successfully.\n");
    printf("Graph initialized with predefined data.\n");
}
void display(struct Graph *g){
	printf("Adjacency Matrix Initial \n");
	int i ,j;
	for(i =0;i<max;i++){
	for(j =0;j<max;j++){
		printf("%d ",g->adj[i][j]);
		}
		printf("\n");
	}
	printf("\nVertex: \n");
	for(i=0;i<max;i++){
		printf("%c, ",g->vertices[i]);
	}
    printf("\n");

}

void dfsutil(struct Graph *g, int v, bool visited[]){
	visited[v]=true;
	printf("%c->",g->vertices[v]);
	int i;
	for(i=0;i<max;i++){
		if(g->adj[v][i]==1 && !visited[i]){
			dfsutil(g,i,visited);
		}
	}
}

void dfs(struct Graph *g, char starting){
	bool visited[max]={false};
		int index;
		int i;
		for(i=0;i<max;i++){
			if(g->vertices[i]==starting){
				
				index=i;
				printf("%d",i);
				break;
			}
		}
		dfsutil(g, index, visited);
        printf("0\n");
}
int main(){
	struct Graph g;
    int ch,ele;
    char data;
    while(1){
    	printf("1. Reset_MaTrixand Vertices\n2. set_Auto_data\n3. Dispay\n4. DFS\n5. clear_screen\n6. exit\n");
        scanf("%d",&ch);
        switch(ch){
        	case 1:
				initG(&g);
            	break;
            case 2:
				set_data(&g);
                break;
            case 3:
            	display(&g);
            	break;
            case 4:
            printf("Enter the starting Element: ");
            scanf(" %c",&data);
            dfs(&g,data);
            break;
            case 5:
                system("cls");
                break;
            case 6:
                exit(0);
                break;
            default:
                printf("Invalid Option.\n");
                break;
        }
    }

return 0;
}