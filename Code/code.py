import psutil
import time

def cpu_usage_test():
    process = psutil.Process()
    
    # Stabilize measurement
    time.sleep(1)
    
    # Record initial CPU usage
    cpu_usage_before = process.cpu_percent(interval=1)
    print(f"Initial CPU usage: {cpu_usage_before}%")

    # Perform a simple CPU task
    start_time = time.time()
    while time.time() - start_time < 5:  # Run for 5 seconds
        _ = sum(i * i for i in range(10000))  # Simple CPU task

    # Record CPU usage after task
    cpu_usage_after = process.cpu_percent(interval=1)
    print(f"CPU usage after task: {cpu_usage_after}%")

cpu_usage_test()

