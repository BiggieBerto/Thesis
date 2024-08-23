import numpy as np
import psutil
import time
from concurrent.futures import ThreadPoolExecutor

# Ensure Python can handle large integers
import sys
sys.set_int_max_str_digits(0)  # Remove the limit on integer string conversion

# Matrix multiplication function
def cpu_intensive_matrix_task(matrix_size):
    a = np.random.rand(matrix_size, matrix_size)
    b = np.random.rand(matrix_size, matrix_size)
    result = np.dot(a, b)
    return result

# Fibonacci calculation function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Measure resource usage
def measure_resource_usage(matrix_size, fibonacci_number):
    process = psutil.Process()
    
    # Stabilize measurement
    time.sleep(2)  # Ensure initial CPU usage is stable

    # Record initial CPU and memory usage
    cpu_usage_before = process.cpu_percent(interval=1)
    mem_usage_before = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    # Start matrix and Fibonacci tasks concurrently
    with ThreadPoolExecutor() as executor:
        future_matrix = executor.submit(cpu_intensive_matrix_task, matrix_size)
        future_fib = executor.submit(fibonacci, fibonacci_number)
        
        # Wait for tasks to start
        time.sleep(5)  # Wait a bit to let the tasks really start running
        
        # Record CPU and memory usage after tasks started
        cpu_usage_during = process.cpu_percent(interval=1)
        mem_usage_during = process.memory_info().rss / 1024 / 1024  # Memory usage in MB
        
        # Wait for tasks to complete
        matrix_result = future_matrix.result()
        fib_result = future_fib.result()
    
    # Record final CPU and memory usage
    time.sleep(2)  # Wait for CPU usage to settle
    cpu_usage_after = process.cpu_percent(interval=1)
    mem_usage_after = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    # Calculate average CPU usage
    avg_cpu_usage = (cpu_usage_before + cpu_usage_during + cpu_usage_after) / 3
    avg_mem_usage = (mem_usage_before + mem_usage_during + mem_usage_after) / 3

    # Print results with handling for large Fibonacci results
    fib_digits = len(str(fib_result))  # Number of digits in the Fibonacci result
    print(f"Matrix Operation Result: {matrix_result[0][0]}")
    print(f"Fibonacci Result has {fib_digits} digits")  # Print digit count instead of result
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_mem_usage} MB")

    return avg_cpu_usage, avg_mem_usage

# Adjust matrix size and Fibonacci number for longer execution
matrix_size = 3000  # Larger matrix size for increased computational load
fibonacci_number = 1500  # Increased Fibonacci number to make computation more intensive

# Collect metrics
cpu, memory = measure_resource_usage(matrix_size, fibonacci_number)

