import numpy as np
import psutil
import time
import sys

# Ensure Python can handle large integers
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
    cpu_usage_before = process.cpu_percent(interval=None)
    mem_usage_before = process.memory_info().rss / 1024 / 1024  # Memory usage in MB
    
    # Start matrix operation
    start_time = time.time()
    matrix_result = cpu_intensive_matrix_task(matrix_size)
    matrix_time = time.time() - start_time
    
    # Measure CPU and Memory usage during the matrix task
    cpu_usage_during = process.cpu_percent(interval=10)  # Measure for 10 seconds
    mem_usage_during = process.memory_info().rss / 1024 / 1024  # Memory usage in MB
    
    # Busy-wait loop to ensure CPU is in use
    busy_start_time = time.time()
    while time.time() - busy_start_time < 10:  # Keep the CPU busy for 10 seconds
        pass
    
    # Start Fibonacci calculation
    start_time = time.time()
    fib_result = fibonacci(fibonacci_number)
    fib_time = time.time() - start_time
    
    # Measure CPU and Memory usage after Fibonacci task
    cpu_usage_after = process.cpu_percent(interval=10)  # Measure for 10 seconds
    mem_usage_after = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    avg_cpu_usage = (cpu_usage_before + cpu_usage_during + cpu_usage_after) / 3
    avg_mem_usage = (mem_usage_before + mem_usage_during + mem_usage_after) / 3

    # Print results with handling for large Fibonacci results
    fib_digits = len(str(fib_result))  # Number of digits in the Fibonacci result
    print(f"Matrix Operation Result: {matrix_result[0][0]}")
    print(f"Fibonacci Result has {fib_digits} digits")  # Print digit count instead of result
    print(f"Total Time taken: {matrix_time + fib_time} seconds")
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_mem_usage} MB")

    return avg_cpu_usage, avg_mem_usage, matrix_time + fib_time

# Adjust matrix size and Fibonacci number for longer execution
matrix_size = 2000  # Adjust this size to control the computation time
fibonacci_number = 1000  # Reduced Fibonacci number to avoid overflow

# Collect metrics
cpu, memory, time_taken = measure_resource_usage(matrix_size, fibonacci_number)
