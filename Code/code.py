import numpy as np
import psutil
import time
from multiprocessing import Process, cpu_count

# Ensure Python can handle large integers
import sys
sys.set_int_max_str_digits(0)  # Remove the limit on integer string conversion

def cpu_intensive_matrix_task(matrix_size):
    print("Starting matrix multiplication")
    a = np.random.rand(matrix_size, matrix_size)
    b = np.random.rand(matrix_size, matrix_size)
    result = np.dot(a, b)
    print("Finished matrix multiplication")
    return result

def fibonacci(n):
    print("Starting Fibonacci calculation")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print("Finished Fibonacci calculation")
    return a

def measure_resource_usage(matrix_size, fibonacci_number):
    process = psutil.Process()
    
    # Stabilize measurement
    time.sleep(2)  # Give time for initial measurement to stabilize

    # Record initial CPU and memory usage
    cpu_usage_before = process.cpu_percent(interval=1)
    mem_usage_before = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    # Start matrix and Fibonacci tasks using multiprocessing
    p1 = Process(target=cpu_intensive_matrix_task, args=(matrix_size,))
    p2 = Process(target=fibonacci, args=(fibonacci_number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    # Record CPU and memory usage after tasks
    time.sleep(2)  # Wait for a bit to let CPU usage settle
    cpu_usage_after = process.cpu_percent(interval=1)
    mem_usage_after = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    # Calculate average CPU usage
    avg_cpu_usage = (cpu_usage_before + cpu_usage_after) / 2
    avg_mem_usage = (mem_usage_before + mem_usage_after) / 2

    # Print results with handling for large Fibonacci results
    fib_digits = len(str(fibonacci(fibonacci_number)))  # Number of digits in the Fibonacci result
    print(f"Matrix Operation Result: Completed")
    print(f"Fibonacci Result has {fib_digits} digits")  # Print digit count instead of result
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_mem_usage} MB")

    return avg_cpu_usage, avg_mem_usage

# Adjust matrix size and Fibonacci number for longer execution
matrix_size = 3000  # Larger matrix size for increased computational load
fibonacci_number = 1500  # Increased Fibonacci number to make computation more intensive

# Collect metrics
cpu, memory = measure_resource_usage(matrix_size, fibonacci_number)
