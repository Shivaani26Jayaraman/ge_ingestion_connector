def fibonacci(n):
    """
    Generates a Fibonacci sequence up to the n-th element.
    Time Complexity: O(n)
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.
    Time Complexity: O(n)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # Sample execution to test the functions
    sample_n = 10
    print(f"Fibonacci series (first {sample_n} terms): {fibonacci(sample_n)}")
    print(f"Factorial of {sample_n}: {factorial(sample_n)}")
