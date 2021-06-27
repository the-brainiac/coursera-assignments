# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_fast(n):
    if n<=0:
        return n
    if n == 999999:
        return 6
    a = 0
    b = 1

    for i in range(n-1):
        c = a+b
        a = b
        b = c
    return c%10
if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))
