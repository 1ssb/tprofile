#!/usr/bin/env python
"""
test.py: Test script for tprofile.

This script tests the tprofile library by profiling several functions
that vary in time and memory usage.

Functions Tested:
- compute_heavy: Performs heavy computation (list allocation and summing).
- sleep_function: Sleeps for a specified duration.
- memory_intensive: Allocates and processes a large NumPy array.
"""

from tprofile import profile
import time
import numpy as np

@profile
def compute_heavy(n):
    """
    Simulates heavy computation by allocating a large list and summing its contents.
    """
    data = [i for i in range(n)]
    return sum(data)

@profile
def sleep_function(duration):
    """
    Sleeps for a given duration (seconds) to simulate time delay.
    """
    time.sleep(duration)
    return duration

@profile
def memory_intensive(n):
    """
    Allocates a large NumPy array and computes its Frobenius norm.
    """
    arr = np.random.rand(n, n)
    return np.linalg.norm(arr)

def main():
    print("=== Running tprofile tests ===\n")
    
    print("Test 1: compute_heavy(n=10,000,000)")
    result1 = compute_heavy(10_000_000)
    print("Result of compute_heavy:", result1, "\n")
    
    print("Test 2: sleep_function(duration=2)")
    result2 = sleep_function(2)
    print("Result of sleep_function:", result2, "\n")
    
    print("Test 3: memory_intensive(n=1000)")
    result3 = memory_intensive(1000)
    print("Result of memory_intensive:", result3, "\n")
    
    print("=== All tests completed ===")

if __name__ == "__main__":
    main()
