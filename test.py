#!/usr/bin/env python
"""
test_profile_only.py: Test script for tprofiler that prints only time and memory profiles.

Each function is decorated with verbose set to False so that only the profiling details
(time elapsed and memory usage) are printed.
"""

from tprofiler.core import profile
import time
import numpy as np

# @profile(enable_memory=True, enable_time=True, verbose=False)
# def compute_heavy(n):
#     """Simulates heavy computation by creating a large list and summing its contents."""
#     data = [i for i in range(n)]
#     return sum(data)

@profile.line
def compute_heavy(n):
    data = [i for i in range(n)]
    return sum(data)

@profile(enable_memory=True, enable_time=True, verbose=False)
def sleep_function(duration):
    """Sleeps for a specified duration (seconds)."""
    time.sleep(duration)
    return duration

@profile(enable_memory=True, enable_time=True, verbose=False)
def memory_intensive(n):
    """Allocates a large NumPy array and computes its Frobenius norm."""
    arr = np.random.rand(n, n)
    return np.linalg.norm(arr)

def test_profile_only():
    print("=== Testing Time and Memory Profiles Only ===\n")
    
    print("Test 1: compute_heavy(n=10,000,000)")
    result1 = compute_heavy(10_000_000)
    print("\n")
    
    print("Test 2: sleep_function(duration=2)")
    result2 = sleep_function(2)
    print("\n")
    
    print("Test 3: memory_intensive(n=1000)")
    result3 = memory_intensive(1000)
    print("\n")
    
    print("=== Test Completed ===")

if __name__ == "__main__":
    test_profile_only()
