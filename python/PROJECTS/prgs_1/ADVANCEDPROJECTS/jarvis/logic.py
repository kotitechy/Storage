from functions import recognize_speech as rs

def think():
    while True:
        print('initialising system...')
        q = rs()
        from functions import process as ps
        ps(q)

think()