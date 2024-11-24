#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX 100

char stack[MAX];
char infix[MAX], postfix[MAX];
int i, j = 0;
int top = -1;

void intopost();
int space(char c);
void print();
void push(char c);
char pop();
int isempty();
int precedence(char symbol);

int main() {
    printf("Enter an infix Expression: ");
    fgets(infix, MAX, stdin);
    intopost();
    print();
    return 0;
}

void intopost() {
    char next, symbol;
    for(i = 0; i < strlen(infix); i++) {
        symbol = infix[i];
        if(!space(symbol)) {
            switch(symbol) {
                case '(': // Corrected from "(" to '('
                    push(symbol);
                    break;
                case ')': // Corrected from ")" to ')'
                    while((next = pop()) != '(') { // Corrected from "(" to '(' and removed the extra space in "! ="
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
                    break;
            }
        }
    }
    while(!isempty()) {
        postfix[j++] = pop();
    }
    postfix[j] = '\0'; // Added null terminator to make it a valid string
}

int space(char c) {
    return (c == ' ' || c == '\t'); // Corrected from "\t" to '\t'
}

void print() {
    int i = 0;
    printf("The equivalent postfix expression is: ");
    while(postfix[i]) {
        printf("%c", postfix[i++]);
    }
    printf("\n");
}

void push(char c) {
    if(top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = c; // Combined increment and assignment
}

char pop() {
    if(top == -1) {
        printf("Stack Underflow\n");
        exit(1);
    }
    return stack[top--]; // Combined decrement and return
}

int isempty() {
    return (top == -1);
}

int precedence(char symbol) {
    switch(symbol) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return 0;
    }
}

