import psutil
import time

def cpu_usage_test():
    process = psutil.Process()

    # Run an intensive CPU task
    def intensive_task():
        start_time = time.time()
        while time.time() - start_time < 10:  # Run for 10 seconds
            _ = sum(i * i for i in range(100000))  # Increase task complexity

    # Stabilize measurement
    time.sleep(2)  # Give system time to stabilize

    # Record initial CPU and memory usage
    cpu_usage_before = process.cpu_percent(interval=2)  # 2-second interval
    mem_usage_before = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    start_time = time.time()
    
    # Run the CPU-intensive task
    intensive_task()
    
    end_time = time.time()

    # Record final CPU and memory usage
    cpu_usage_after = process.cpu_percent(interval=2)  # 2-second interval
    mem_usage_after = process.memory_info().rss / 1024 / 1024  # Memory usage in MB

    avg_cpu_usage = (cpu_usage_before + cpu_usage_after) / 2
    avg_mem_usage = (mem_usage_before + mem_usage_after) / 2

    print(f"Time taken: {end_time - start_time} seconds")
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_mem_usage} MB")

cpu_usage_test()
