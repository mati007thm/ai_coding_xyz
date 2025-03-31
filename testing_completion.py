def fibonacci(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The nth Fibonacci number.
    """
    result = 0
    a, b = 0, 1
    for i in range(n + 1):
        result = a
        a, b = b, a + b
        print(f'{i}: {result}')
    return result

fibonacci(10)

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial: " + str(factorial(5)))
