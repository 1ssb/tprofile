# tprofiler

tprofiler is a lightweight Python library for total profiling—combining time and memory profiling using `psutil` with optional line-by-line profiling using `line_profiler`. It provides a decorator for profiling individual functions, a context manager for profiling code blocks, and a command-line tool for profiling entire scripts.

## Features

- **Combined Time and Memory Profiling:**
  Track execution time and process memory (RSS) before and after function or code block execution.
- **Easy-to-Use Decorator:**
  Simply add `@profile` to any function to get detailed profiling output.
- **Line-by-Line Profiling:**
  Use `@profile.line` to obtain a detailed, line-by-line performance analysis (requires `line_profiler`).
- **Context Manager:**
  Profile arbitrary code blocks with the provided `ProfileContext`.
- **Command-Line Tool:**
  Run any Python script with `tprofiler` to obtain an overall profiling summary.

## Installation

tprofiler is available on PyPI. Install it using pip:

```bash
pip install tprofiler
```

## Usage

### 1. As a Decorator

Add profiling to any function by importing and applying the decorator:

```python
from tprofiler.core import profile

@profile(enable_memory=True, enable_time=True, verbose=True)
def my_function(n):
    total = sum(range(n))
    return total

result = my_function(1000000)
```

When `my_function` is called, tprofiler prints the execution time and memory usage details, along with the function's return value if `verbose` is enabled.

### 2. Line-by-Line Profiling

For a detailed line-by-line analysis, use the line profiling decorator:

```python
from tprofiler.core import profile

@profile.line
def compute_heavy(n):
    data = [i for i in range(n)]
    return sum(data)

compute_heavy(10_000_000)
```

This will output detailed line-by-line performance statistics for `compute_heavy` (ensure `line_profiler` is installed).

### 3. As a Command-Line Tool

You can profile an entire script by running:

```bash
tprofiler your_script.py [script arguments...]
```

For example, if you have a script named `example.py`, run:

```bash
tprofiler example.py --option value
```

This command executes the script and prints an overall profiling summary including total time elapsed and memory consumption.

### 4. Using the Context Manager

To profile a block of code without decorating a function, use the `ProfileContext`:

```python
from tprofiler import ProfileContext

with ProfileContext(enable_memory=True, enable_time=True):
    # Place the code you want to profile here
    total = sum(range(1000000))
    print(total)
```

## How It Works

* **Time Profiling:**

  Uses Python's `time` module to capture the execution time before and after function calls or code blocks.
* **Memory Profiling:**

  Uses `psutil` to measure the process's memory usage (RSS) before and after execution.
* **Line Profiling:**

  Integrates with `line_profiler` to provide detailed per-line execution statistics.

## Contributing

Contributions and improvements are welcome! Feel free to open issues or submit pull requests on [GitHub](https://github.com/1ssb/tprofiler).

## License

This project is licensed under the MIT License.
