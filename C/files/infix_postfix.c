#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define MAX 100

char stack[MAX], postfix[MAX], infix[MAX];
int top = -1;

void push(char c) {
    if(top == MAX-1) {
        printf("Stack is full.\n");
        return;
    }
    top++;
    stack[top] = c;
}

int isempty() {
    return (top == -1);
}

char pop() {
    if(top == -1) {
        printf("Stack underflow.\n");
        exit(1);
    } else {
        char c = stack[top];
        top--;
        return c;
    }
}

int precedence(char symbol) {
    switch(symbol) {
        case '^': return 3;
        case '*':
        case '/': return 2;
        case '+':
        case '-': return 1;
        default: return 0;
    }
}

int space(char c) {
    if(c == ' ' || c == '\t'){
    	return 1;
	}else{
		return 0;
	}
}

void intopost() {
    int i, j = 0;
    char next, symbol;
    for(i = 0; i < strlen(infix); i++) {
        symbol = infix[i];
        if(!space(symbol)) {
            switch(symbol) {
                case '(':
                    push(symbol);
                    break;

                case ')':
                	next = pop()
                    while(next != '(') {
                        postfix[j++] = next;
                    }
                    break;

                case '+':
                case '-':
                case '*':
                case '/':
                case '^':
                    while(!isempty() && precedence(stack[top]) >= precedence(symbol)) {
                        postfix[j++] = pop();
                    }
                    push(symbol);
                    break;

                default:
                    postfix[j++] = symbol;
            }
        }
    }
    while(!isempty()) {
        postfix[j++] = pop();
    }
    postfix[j] = '\0'; // Null-terminate the postfix expression
}

void print() {
    printf("Postfix expression: %s\n", postfix);
}
int check_parentheses() {
    int i;
    char symbol;
    
    for(i = 0; i < strlen(infix); i++) {
        symbol = infix[i];
        if(symbol == '(') {
            push(symbol);
        } else if(symbol == ')') {
            if(isempty()) {
                return 0; // Mismatched closing parenthesis
            }
            pop(); // Match the closing parenthesis
        }
    }
    
    return isempty(); // If stack is empty, parentheses are balanced
}


int main() {
    printf("Enter infix expression: ");
    gets(infix);
    
     if(!check_parentheses()) {
        printf("Error: Unbalanced parentheses in the infix expression.\n");
        return 1;
    }
    intopost();
    print();
    
    return 0;
}

