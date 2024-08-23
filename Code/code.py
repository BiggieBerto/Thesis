import time
import numpy as np
import psutil
import os

def measure_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)  # Convert to MB

def matrix_multiplication(size):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.dot(A, B)

def main():
    size = 1000  # Change this size for more computation
    print(f"Matrix size: {size}x{size}")

    start_time = time.time()
    
    initial_memory = measure_memory()
    matrix_multiplication(size)
    final_memory = measure_memory()

    elapsed_time = time.time() - start_time
    memory_usage = final_memory - initial_memory

    print(f"Elapsed time: {elapsed_time:.2f} seconds.")
    print(f"Memory usage: {memory_usage:.2f} MB")

if __name__ == "__main__":
    main()
