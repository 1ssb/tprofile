#!/usr/bin/env python
"""
tprofiler: A combined time and memory profiling library using psutil.

Usage as a decorator:
    from tprofiler.core import profile
    @profile(enable_memory=True, enable_time=True, verbose=True)
    def my_function(...):
        ...

Usage as a context manager:
    from tprofiler.core import ProfileContext
    with ProfileContext(enable_memory=True, enable_time=True):
        # Code block to profile

Usage as a command-line tool:
    tprofiler script.py [script arguments...]
"""

import sys
import time
import psutil
import functools
import runpy
import logging
from typing import Any, Callable, Optional, TypeVar

# Set up logging configuration.
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# Define a generic type for decorator return.
T = TypeVar("T", bound=Callable[..., Any])

def profile(enable_memory: bool = True, enable_time: bool = True, verbose: bool = True) -> Callable[[T], T]:
    """
    Decorator that profiles memory and time usage of the wrapped function.

    Args:
        enable_memory (bool): Enable memory profiling (default True).
        enable_time (bool): Enable time profiling (default True).
        verbose (bool): If True, logs the function's return value (default True).

    Returns:
        The wrapped function with profiling.

    Usage:
        @profile(enable_memory=True, enable_time=True, verbose=True)
        def my_function(...):
            ...
    """
    def decorator(func: T) -> T:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            process = psutil.Process()
            mem_before: Optional[float] = process.memory_info().rss / (1024 ** 2) if enable_memory else None
            time_before: Optional[float] = time.time() if enable_time else None

            result = func(*args, **kwargs)

            time_after: Optional[float] = time.time() if enable_time else None
            mem_after: Optional[float] = process.memory_info().rss / (1024 ** 2) if enable_memory else None

            logger.info("=" * 40)
            logger.info(f"Function: {func.__name__}")
            if enable_time and time_before is not None and time_after is not None:
                logger.info(f"Time elapsed: {time_after - time_before:.6f} seconds")
            if enable_memory and mem_before is not None and mem_after is not None:
                logger.info(f"Memory usage: before: {mem_before:.2f} MB, after: {mem_after:.2f} MB, diff: {mem_after - mem_before:.2f} MB")
            if verbose:
                logger.info(f"Result of {func.__name__}: {result}")
            logger.info("=" * 40)

            return result
        return wrapper  # type: ignore
    return decorator

class ProfileContext:
    """
    A context manager to profile a block of code.
    
    Usage:
        from tprofiler.core import ProfileContext
        with ProfileContext(enable_memory=True, enable_time=True):
            # Code block to profile
    """
    def __init__(self, enable_memory: bool = True, enable_time: bool = True) -> None:
        self.enable_memory = enable_memory
        self.enable_time = enable_time
        self.mem_before: Optional[float] = None
        self.time_before: Optional[float] = None
        self.process = psutil.Process()

    def __enter__(self) -> "ProfileContext":
        if self.enable_memory:
            self.mem_before = self.process.memory_info().rss / (1024 ** 2)
        if self.enable_time:
            self.time_before = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        mem_after: Optional[float] = self.process.memory_info().rss / (1024 ** 2) if self.enable_memory else None
        time_after: Optional[float] = time.time() if self.enable_time else None

        logger.info("=" * 40)
        logger.info("Code Block Profiling Summary:")
        if self.enable_time and self.time_before is not None and time_after is not None:
            logger.info(f"Time elapsed: {time_after - self.time_before:.6f} seconds")
        if self.enable_memory and self.mem_before is not None and mem_after is not None:
            logger.info(f"Memory usage: before: {self.mem_before:.2f} MB, after: {mem_after:.2f} MB, diff: {mem_after - self.mem_before:.2f} MB")
        logger.info("=" * 40)

def main() -> None:
    """
    Command-line entry point for tprofiler.

    Usage:
         tprofiler script.py [script arguments...]
    """
    if len(sys.argv) < 2:
        print("Usage: tprofiler <script.py> [script arguments...]")
        sys.exit(1)

    script = sys.argv[1]
    # Adjust sys.argv so that the target script sees its own arguments.
    sys.argv = sys.argv[1:]

    process = psutil.Process()
    mem_before = process.memory_info().rss / (1024 ** 2)
    time_before = time.time()

    try:
        runpy.run_path(script, run_name="__main__")
    except Exception as e:
        logger.error(f"Error running {script}: {e}")
        sys.exit(1)

    time_after = time.time()
    mem_after = process.memory_info().rss / (1024 ** 2)

    logger.info("\n" + "=" * 40)
    logger.info("Overall Profiling Summary:")
    logger.info(f"Total Time elapsed: {time_after - time_before:.6f} seconds")
    logger.info(f"Memory usage: before: {mem_before:.2f} MB, after: {mem_after:.2f} MB, diff: {mem_after - mem_before:.2f} MB")
    logger.info("=" * 40)

if __name__ == "__main__":
    main()
