import psutil
import time

def simple_cpu_task():
    count = 0
    while count < 1e7:
        count += 1

def measure_resource_usage():
    process = psutil.Process()
    
    # Stabilize measurement
    time.sleep(2)

    # Record initial CPU and memory usage
    cpu_usage_before = process.cpu_percent(interval=1)
    mem_usage_before = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    start_time = time.time()
    
    # Run a CPU-intensive task
    simple_cpu_task()

    end_time = time.time()
    
    # Record final CPU and memory usage
    cpu_usage_after = process.cpu_percent(interval=1)
    mem_usage_after = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    avg_cpu_usage = (cpu_usage_before + cpu_usage_after) / 2
    avg_mem_usage = (mem_usage_before + mem_usage_after) / 2

    print(f"Time taken: {end_time - start_time} seconds")
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_mem_usage} MB")

    return avg_cpu_usage, avg_mem_usage

measure_resource_usage()


