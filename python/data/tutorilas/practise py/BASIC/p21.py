import threading
import time

# Shared resource
shared_resource = 0

# Lock for synchronization
lock = threading.Lock()

# Function to increment the shared resource
def increment():
    global shared_resource
    for _ in range(100000):
        lock.acquire()  # Acquire the lock
        shared_resource += 1
        lock.release()  # Release the lock

# Create multiple threads to increment the shared resource
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the final value of the shared resource
print("Final value of shared resource:", shared_resource)
