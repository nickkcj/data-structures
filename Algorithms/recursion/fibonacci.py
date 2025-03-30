#Given a numer N, return the index value of
#the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacciRecursive(n):
    #Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
    

def fibonacciIterative(n):
    #Base cases
    if n <= 0:
        return 0
    
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b