#include <iostream>
using namespace std;

template <class T>
class Stack
{
    T s[10];
    int top, n, elt;

public:
    Stack()
    {
        top = -1;
        cout << endl
             << "Enter the size of the stack: ";
        cin >> n;
    }

    void push(T elt)
    {
        if (top < n - 1)
        {
            cout << endl
                 << "Enter the element to push: ";
            cin >> elt;
            s[++top] = elt;
        }
        else
            cout << endl
                 << "Stack is full!..";
    }

    void pop()
    {
        if (top < 0)
        {
            cout << endl
                 << "Stack is empty!..";
        }
        else
        {
            cout << endl
                 << "popped " << s[top--];
        }
    }
    void Stack_operation();
    void display()
    {
        cout << endl
             << "The stack elemnts are: ";
        for (int i = 0; i < n; i++)
        {
            cout << "\t " << s[i];
        }
    }
};

template <class T>
void Stack<T>::Stack_operation()
{
    int choice = 1, i;
    T elet;
    while (choice > 0 && choice < 3)
    {
        cout << endl
             << "1.push" << endl
             << "2.pop"
             << "\t Pressany key to exit" << endl
             << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "\n Enter the element:";
            cin >> elt;
            push(elt);

            display();
            break;

        case 2:
            pop();
            display();
            break;
        }
    }
}

int main()
{
    cout << endl
         << "Stack operations usin class templates";
    cout << endl
         << "INT DATATYPE";
    Stack<int> stk1;
    cout << endl
         << "FLOAT DATATYPE";
    Stack<float> stk2;
    int ch;
    while (1)
    {
        switch (ch)
        {
            {

            case 1:
                stk1.Stack_operation();
                break;

            case 2:
                stk2.Stack_operation();
                break;

            deafult:
                exit(0);
            }
        }
        return 0;
    }}
