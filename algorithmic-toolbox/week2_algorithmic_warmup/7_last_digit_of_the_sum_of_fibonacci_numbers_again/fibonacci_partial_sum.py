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

def fibonacci_partial_sum_fast(from_, to):
    return (calc_fib_fast(to+2)-calc_fib_fast(from_+1))%10


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    # input = sys.stdin.read();
    from_, to = map(int, input().split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))