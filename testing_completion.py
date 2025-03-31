def fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    result = 0
    a, b = 0, 1
    for i in range(2, n + 1):
        result = a
        a, b = b, a + b
    return result

# Example usage
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

def factorial(n, memo={0: 0, 1: 1}):
    """
    Calculate the factorial of a given number using recursion with memoization.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the number.
    """
    if n in memo:
        return memo[n]
    else:
        memo[n] = n * factorial(n-1, memo)
        return memo[n]

# Example usage
n = 5
print(f"The factorial of {n} is: {factorial(n)}")
