#!/usr/bin/env python
"""
tprofile: A combined time and memory profiling library using psutil.

Usage as a decorator:
    from tprofile.core import profile
    @profile
    def my_function(...):
        ...

Usage as a command-line tool:
    tprofile script.py [script arguments...]
"""

import sys
import time
import psutil
import functools
import runpy

def profile(func):
    """
    Decorator that profiles memory and time usage of the wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        mem_before = process.memory_info().rss / (1024 ** 2)  # in MB
        time_before = time.time()
        result = func(*args, **kwargs)
        time_after = time.time()
        mem_after = process.memory_info().rss / (1024 ** 2)
        print("=" * 40)
        print(f"Function: {func.__name__}")
        print(f"Time elapsed: {time_after - time_before:.6f} seconds")
        print(f"Memory usage: before: {mem_before:.2f} MB, after: {mem_after:.2f} MB, diff: {mem_after - mem_before:.2f} MB")
        print("=" * 40)
        return result
    return wrapper

def main():
    """
    Command-line entry point for tprofile.

    Usage:
         tprofile script.py [script arguments...]
    """
    if len(sys.argv) < 2:
        print("Usage: tprofile <script.py> [script arguments...]")
        sys.exit(1)
    
    script = sys.argv[1]
    # Adjust sys.argv so that the target script sees its own args.
    sys.argv = sys.argv[1:]
    
    process = psutil.Process()
    mem_before = process.memory_info().rss / (1024 ** 2)  # in MB
    time_before = time.time()
    
    # Execute the target script in __main__ namespace.
    runpy.run_path(script, run_name="__main__")
    
    time_after = time.time()
    mem_after = process.memory_info().rss / (1024 ** 2)
    
    print("\n" + "=" * 40)
    print("Overall Profiling Summary:")
    print(f"Total Time elapsed: {time_after - time_before:.6f} seconds")
    print(f"Memory usage: before: {mem_before:.2f} MB, after: {mem_after:.2f} MB, diff: {mem_after - mem_before:.2f} MB")
    print("=" * 40)
