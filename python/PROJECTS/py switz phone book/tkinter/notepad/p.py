import time

start_time = time.time()
count = 0
while time.time() - start_time < 1:  # Run for 1 second
    count += 1
print("Iterations in 1 second:", count)
