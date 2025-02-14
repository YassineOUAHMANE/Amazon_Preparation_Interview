import time
import random
import string

# Function to generate a random string of fixed length
def random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Function for hashing-based grouping
def compute_hash(s: str) -> int:
    return hash(s)

def group_identical_strings_hash(s: list) -> list:
    n = len(s)
    hashes = [(compute_hash(s[i]), i) for i in range(n)]
    hashes.sort()
    
    groups = []
    for i in range(n):
        if i == 0 or hashes[i][0] != hashes[i - 1][0]:
            groups.append([])
        groups[-1].append(hashes[i][1])
    
    return groups

# Function for simple comparison-based grouping
def group_identical_strings_simple(s: list) -> list:
    n = len(s)
    groups = []
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue
        current_group = [i]
        for j in range(i + 1, n):
            if s[i] == s[j]:
                visited[j] = True
                current_group.append(j)
        groups.append(current_group)
    
    return groups

# Generate large input (random strings)
input_size = 10000
strings = [random_string() for _ in range(input_size)]

# Measure time for hash-based grouping
start_time = time.time()
group_identical_strings_hash(strings)
hash_time = time.time() - start_time

# Measure time for simple comparison-based grouping
start_time = time.time()
group_identical_strings_simple(strings)
simple_time = time.time() - start_time

# Print results
print(f"Hash-based grouping took: {hash_time:.5f} seconds")
print(f"Simple comparison-based grouping took: {simple_time:.5f} seconds")
