import time 

score = 0
def wel():
	name = input("What's your name : ")
	print("Hey {}".format(name))

def ins_sc():
	score = 0
	score+=1
	print('Score: ',score)
	
def q1():
	global score 
	print('\nwhat use of pass ')
	time.sleep(1)
	print('\na. decalre function and eliminate code')
	print('b. check conditional statements')
	print('c. breaking a loop')
	
	ans = input('\nwhat is the right answer: ')
	if ans == 'a':
		print('well done you are correct')
		ins_sc()
	else: 
		print('Sorry That wasn\'t correct one')

wel()
q1()