import time
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_primes(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    start_time = time.time()
    
    # Change the limit to a larger number if you need more computation
    limit = 100000
    primes = calculate_primes(limit)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Calculated {len(primes)} primes up to {limit}.")
    print(f"Elapsed time: {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()


