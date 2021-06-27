# Uses python3
import sys


def calc_fib_fast(n):
    if n<=1:
        return n
    a = 0
    b = 1
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    return c

def fibonacci_sum_fast(n):
    return (calc_fib_fast(n+2)-1)%10

def fibonacci_sum_naive(n):
    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum%10

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))
