import psutil
import time

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
    cpu_usage = []
    mem_usage = []

    # Start matrix operation
    start_time = time.time()
    matrix_result = cpu_intensive_matrix_task(matrix_size)
    matrix_time = time.time() - start_time
    time.sleep(2)  # Wait to ensure CPU usage measurement is accurate
    cpu_usage.append(process.cpu_percent(interval=1))
    mem_usage.append(process.memory_info().rss / 1024 / 1024)  # Memory usage in MB

    # Busy-wait loop to ensure CPU is in use
    busy_start_time = time.time()
    while time.time() - busy_start_time < 5:  # Keep the CPU busy for 5 seconds

    # Start Fibonacci calculation
    start_time = time.time()
    fib_result = fibonacci(fibonacci_number)
    fib_time = time.time() - start_time
    cpu_usage.append(process.cpu_percent(interval=1))
    mem_usage.append(process.memory_info().rss / 1024 / 1024)  # Memory usage in MB

    avg_cpu_usage = sum(cpu_usage) / len(cpu_usage)
    avg_mem_usage = sum(mem_usage) / len(mem_usage)

    print(f"Matrix Operation Result: {matrix_result[0][0]}")
    print(f"Fibonacci Result: {fib_result}")
    print(f"Total Time taken: {matrix_time + fib_time} seconds")
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_mem_usage} MB")

    return avg_cpu_usage, avg_mem_usage, matrix_time + fib_time

# Adjust matrix size and Fibonacci number for longer execution
matrix_size = 1000  # Adjust this size to control the computation time
fibonacci_number = 100000  # Adjust this number to control the computation time

# Collect metrics
cpu, memory, time_taken = measure_resource_usage(matrix_size, fibonacci_number)
    
    # Start Fibonacci calculation
    start_time = time.time()
    fib_result = fibonacci(fibonacci_number)
    fib_time = time.time() - start_time
    
    # Measure CPU and Memory usage during the Fibonacci task
    cpu_usage.append(process.cpu_percent(interval=2))  # Measure for 2 seconds
    mem_usage.append(process.memory_info().rss / 1024 / 1024)  # Memory usage in MB

    avg_cpu_usage = sum(cpu_usage) / len(cpu_usage)
    avg_mem_usage = sum(mem_usage) / len(mem_usage)

    print(f"Matrix Operation Result: {matrix_result[0][0]}")
    print(f"Fibonacci Result (limited): {fib_result}")
    print(f"Total Time taken: {matrix_time + fib_time} seconds")
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_mem_usage} MB")

    return avg_cpu_usage, avg_mem_usage, matrix_time + fib_time

# Adjust matrix size and Fibonacci number for longer execution
matrix_size = 1000  # Adjust this size to control the computation time
fibonacci_number = 5000  # Adjust this number to control the computation time

# Collect metrics
cpu, memory, time_taken = measure_resource_usage(matrix_size, fibonacci_number)

