import numpy as np
import psutil
import time

def cpu_intensive_task():
    matrix_size = 500
    a = np.random.rand(matrix_size, matrix_size)
    b = np.random.rand(matrix_size, matrix_size)
    result = np.dot(a, b)
    return result

# Measure resource usage during this task
def measure_resource_usage():
    process = psutil.Process()
    cpu_usage = []
    mem_usage = []
    
    start_time = time.time()
    result = cpu_intensive_task()
    cpu_usage.append(process.cpu_percent(interval=1))  # Increase interval to 1 second
    mem_usage.append(process.memory_info().rss / 1024 / 1024)  # Memory usage in MB
    
    end_time = time.time()
    time_taken = end_time - start_time
    avg_cpu_usage = sum(cpu_usage) / len(cpu_usage)
    avg_mem_usage = sum(mem_usage) / len(mem_usage)
    
    print(f"CPU Intensive Task Result: {result[0][0]}")
    print(f"Time taken: {time_taken} seconds")
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_mem_usage} MB")

    return avg_cpu_usage, avg_mem_usage, time_taken

# Collect metrics
cpu, memory, time_taken = measure_resource_usage()
