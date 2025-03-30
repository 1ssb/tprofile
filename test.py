#!/usr/bin/env python
"""
test_profile_only.py: Test script for tprofiler that prints only time and memory profiles.

Each function is decorated with verbose set to False so that only the profiling details
(time elapsed and memory usage) are printed.
"""

from tprofiler.core import profile
import time
import numpy as np

# Using line-by-line profiling for compute_heavy
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

# Function with line-by-line profiling accepting variable arguments.
@profile.line
def variadic_line_profile(*args, **kwargs):
    # Simulate some processing: sum numbers, and process keyword values.
    total = sum(arg for arg in args if isinstance(arg, (int, float)))
    # Process kwargs: if a value is a list, sum its elements
    for key, value in kwargs.items():
        if isinstance(value, list):
            total += sum(value)
        elif isinstance(value, (int, float)):
            total += value
    return total

# Standard function with profiling accepting variable arguments.
@profile(enable_memory=True, enable_time=True, verbose=True)
def variadic_function(*args, **kwargs):
    # Return all positional arguments and keyword arguments as a tuple
    return args, kwargs

def test_variadic():
    print("=== Testing Variadic Functions with tprofiler ===\n")
    
    print("Test 1: variadic_line_profile with multiple inputs")
    result_line = variadic_line_profile(10, 20, 30, extra=[1, 2, 3], factor=2)
    print("\n")
    
    print("Test 2: variadic_function with multiple inputs")
    result_var = variadic_function("hello", "world", a=100, b=[4, 5, 6], c={"key": "value"})
    print("Returned from variadic_function:", result_var)
    print("\n")
    
    print("=== Variadic Tests Completed ===")

    
if __name__ == "__main__":
    test_profile_only()
    test_variadic()
