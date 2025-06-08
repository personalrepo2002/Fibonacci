# Fibonacci Calculator

A simple Python project to calculate Fibonacci numbers.

## Usage

To use the Fibonacci calculator, import the `calculate_fibonacci` function from the `fibonacci.fibonacci` module.

Here's an example:

```python
from fibonacci.fibonacci import calculate_fibonacci

result = calculate_fibonacci(10)
print(f"The 10th Fibonacci number is: {result}")
# Expected output: The 10th Fibonacci number is: 55
```

The `calculate_fibonacci(n)` function takes an integer `n` as input and returns the nth Fibonacci number. If `n` is negative, it will raise a `ValueError`.

## Running Tests

Unit tests are located in the `tests` directory and use Python's built-in `unittest` framework.

To run the tests, navigate to the root directory of the project in your terminal and execute the following command:

```bash
python -m unittest discover
```

Make sure that the project's root directory is in your `PYTHONPATH` or that you are running the command from the root directory for the imports to work correctly. For example:

```bash
export PYTHONPATH=$PYTHONPATH:. # If running from the root directory
python -m unittest discover tests
```
