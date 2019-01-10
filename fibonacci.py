# Various algorithms for finding the n'th number of the fibonacci sequence, implemented in Python 3
# January 9 2019

import cProfile

# Basic recursive implementation
def fibonacciRecursive(n):
    if n < 2:
        return n
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

# Iterative implementation, with linear memory usage
def fibonacciIterative(n):
    fibonacciNumbers = [0, 1]
    for i in range(2, n + 1):
        fibonacciNumbers.append(fibonacciNumbers[i - 1] + fibonacciNumbers[i - 2])
    return fibonacciNumbers[n]

# Another iterative implementation, with constant memory usage
def fibonacciSwap(n):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(2, n + 1):
        fib2, fib1 = fib1 + fib2, fib2
    return fib2

# Closed form expression for calculating the n'th fibonacci number
def fibonacciClosedForm(n):
    golden_ratio = (1 + (5 ** 0.5)) / 2
    return int(((golden_ratio ** n) - ((1 - golden_ratio) ** n)) / (5 ** 0.5))

def test():
    n = 35
    format_string = "{:<" + str(len(str(n))) + "} : {}"
    for i in range(0, n):
        r1 = fibonacciRecursive(i)
        r2 = fibonacciIterative(i)
        r3 = fibonacciSwap(i)
        r4 = fibonacciClosedForm(i)
        assert(r1 == r2 and r2 == r3 and r3 == r4)
        print(format_string.format(i + 1, r1))

if __name__ == "__main__":
    cProfile.run("test()")
