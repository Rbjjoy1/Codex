import time
import random
import math

# Function to benchmark SELECT algorithm

def select_algorithm(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return select_algorithm(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return select_algorithm(highs, k - len(lows) - len(pivots))

# Function to benchmark the runtime for different group sizes

def benchmark_select(group_size):
    results = []
    for n in range(1000, 500001, 1000):  # Increase input size from 1,000 to 500,000
        i = math.floor(3 * n / 4)  # Calculate i
        arr = random.sample(range(1, n + 1), n)  # Generate random array of size n
        start_time = time.time()
        select_algorithm(arr, i)  # Benchmark SELECT algorithm
        end_time = time.time() - start_time
        results.append((n, end_time))  # Store input size and runtime
    return results

if __name__ == '__main__':
    group_sizes = [3, 5]  # Group sizes
    for group_size in group_sizes:
        print(f'Benchmarking SELECT algorithm for group size {group_size}')
        runtime_results = benchmark_select(group_size)
        for n, runtime in runtime_results:
            print(f'Input size: {n}, Runtime: {runtime:.6f} seconds')
