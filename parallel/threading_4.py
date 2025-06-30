import threading
import time

# Function to be executed in a thread
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate some work

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Main thread continues to execute
print("Main thread is running...")

# Wait for the thread to complete
thread.join()

print("Thread has finished execution.")
