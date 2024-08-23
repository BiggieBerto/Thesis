import psutil
import time
import subprocess

def measure_cpu_usage(interval=30, sample_duration=1):
    cpu_usage = []
    
    # Measure CPU usage over the specified interval
    end_time = time.time() + interval
    while time.time() < end_time:
        cpu_usage.append(psutil.cpu_percent(interval=sample_duration))

    # Calculate average CPU usage
    avg_cpu_usage = sum(cpu_usage) / len(cpu_usage)
    return avg_cpu_usage

def run_build():
    # Replace this command with your build command
    subprocess.run(["your_build_command_here"], check=True)

if __name__ == "__main__":
    # Start CPU measurement in a separate process
    avg_cpu_before_build = measure_cpu_usage(interval=30, sample_duration=1)
    
    # Start the build process
    run_build()
    
    # Output the average CPU usage
    print(f"Average CPU usage during the build: {avg_cpu_before_build}%")
