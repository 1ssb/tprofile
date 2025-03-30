# tprofiler

tprofiler is a lightweight Python library that combines time and memory profiling using `psutil`. It provides both a decorator for profiling individual functions and a command-line tool for profiling entire scripts.

## Features

- **Combined Time and Memory Profiling:**
  Track execution time and process memory (RSS) before and after function execution.
- **Easy-to-Use Decorator:**
  Simply add `@profile` to any function to get detailed profiling output.
- **Command-Line Tool:**
  Run any Python script with `tprofiler` to obtain an overall profiling summary.

## Installation

tprofile is available on PyPI. Install it using pip:

```bash
pip install tprofiler
```

## Usage

### 1. As a Decorator

Add profiling to any function by importing and applying the decorator:

```python
from tprofile import profile

@profile
def my_function(n):
    total = sum(range(n))
    return total

result = my_function(1000000)
```

When `my_function` is called, tprofile will print the execution time and memory usage details.

### 2. As a Command-Line Tool

You can profile an entire script by running:

```bash
tprofiler your_script.py [script arguments...]
```

For example, if you have a script named `example.py`, run:

```bash
tprofiler example.py --option value
```

This command executes the script and prints an overall profiling summary including total time elapsed and memory consumption.

## How It Works

* **Time Profiling:**

  Uses Python's `time` module to capture the execution time before and after function calls or script runs.
* **Memory Profiling:**

  Uses `psutil` to measure the process's memory usage (RSS) before and after execution.

## Contributing

Contributions and improvements are welcome! Feel free to open issues or submit pull requests on GitHub.

## License

This project is licensed under the MIT License.
