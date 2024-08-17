import os
import time
import psutil

# Function to calculate the Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function to perform disk I/O
def disk_io_test(file_name, size_in_mb):
    data = os.urandom(1024 * 1024)  # 1 MB of random data
    with open(file_name, 'wb') as f:
        for _ in range(size_in_mb):
            f.write(data)
    with open(file_name, 'rb') as f:
        f.read()

# Function to perform memory allocation
def memory_allocation_test(size_in_mb):
    data = []
    for _ in range(size_in_mb):
        data.append(os.urandom(1024 * 1024))  # 1 MB of random data
    time.sleep(5)  # Keep the memory allocated for a while

if __name__ == "__main__":
    # Measure CPU usage by calculating Fibonacci
    start_time = time.time()
    fib_number = fibonacci(30)  # Change the number to increase/decrease CPU load
    end_time = time.time()
    print(f"Fibonacci result: {fib_number}, Time taken: {end_time - start_time} seconds")

    # Measure Disk I/O
    disk_io_test("test_file.bin", 100)  # 100 MB file
    os.remove("test_file.bin")

    # Measure Memory usage
    memory_allocation_test(500)  # 500 MB memory allocation

    # Print resource usage
    process = psutil.Process(os.getpid())
    print(f"CPU usage: {process.cpu_percent(interval=1)}%")
    print(f"Memory usage: {process.memory_info().rss / 1024 / 1024} MB")
