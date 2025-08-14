import numpy as np
import time

# Recursive Method
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



# Iterative Method
def fibonacci_iterative(n): 
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a



# Matrix Exponentiation Method
def fibonacci_matrix(n):
    F = np.matrix([[1, 1], [1, 0]])
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (F ** (n - 1))[0, 0]


def fibonacci(n, method='iterative'):   
    n = int(n)
    if method == 'recursive':
        return fibonacci_recursive(n)
    elif method == 'iterative':
        return fibonacci_iterative(n)
    elif method == 'matrix':
        return fibonacci_matrix(n)
    else:
        raise ValueError("Unknown method: {}".format(method))



if __name__ == "__main__":

    start_recursive = time.time()
    print(fibonacci(40, method='recursive'))
    end_recursive = time.time()
    print(f"Time taken (recursive): {end_recursive - start_recursive:.6f} seconds")

    start_iterative = time.time()
    print(fibonacci(40, method='iterative'))
    end_iterative = time.time()
    print(f"Time taken (iterative): {end_iterative - start_iterative:.6f} seconds")
    
    start_matrix = time.time()
    print(fibonacci(40, method='matrix'))
    end_matrix = time.time()
    print(f"Time taken (matrix): {end_matrix - start_matrix:.6f} seconds")