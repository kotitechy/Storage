import pyttsx3 as pt

def name(p, e):
    e.say("Hello There whats Your's name")
    engine.runAndWait()
    print("\t\t\t Bot : Hello There whats Your's name: ")
    n = input('')
    e.say(f'oh {n} glad to see you today')
def add(p, e):
    if p == 'c program to add 2 numbers' or p == 'c program to add two numbers' or p == 'how to add 2 numbers in c':
        e.say('Here we go c program to add two numbers')
        engine.runAndWait()
        op = ''' #include<stdio.h> //header files \n#include<conio.h> \nint main(){ \nint a,b; \nprintf("Enter  value of a: \t"); \nscanf("%d",&a); \nprintf("Enter  value of b: \t"); \nscanf("%d",&b); \nprintf("\n The sum of %d  , %d    =   %d",a,b,a+b);'''
        print(op)
def err(e):
    e.say("I am unable to answer as i have limited knownledge")
    engine.runAndWait()
    print("\t\t\t Bot : Hello There whats Your's name: ")

def prompt(p):
    if p == 'name' or p == 'hey there' or p == 'hello' or p ==  'hi':
        name(p, engine)
    elif p == 'c program to add 2 numbers' or p == 'c program to add two numbers' or p == 'how to add 2 numbers in c':
        add(p, engine)
    else:
        err(engine)

print('Chat Bot Ai')
engine = pt.init()
print('Hey There Welcome to Chat Bot ai')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.say('Hey There Welcome to Chat Bot ai')
engine.runAndWait()
engine.say('What can i help you ')
while True:
    engine.runAndWait()
    p = input('What can do next for u ')
    prompt(p)    
    engine.say('What can do next for u ')
    engine.runAndWait()
    

engine.stop()
