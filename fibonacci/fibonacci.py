# This is the Fibonacci library.
# It will contain functions to calculate Fibonacci numbers.
def calculate_fibonacci(n):
  """
  Calculates the nth Fibonacci number.
  """
  if n < 0:
    raise ValueError("Input must be a non-negative integer")
  elif n <= 1:
    return n
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      a, b = b, a + b
    return b
