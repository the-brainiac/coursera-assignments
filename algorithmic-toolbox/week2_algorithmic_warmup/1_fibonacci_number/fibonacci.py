# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

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

n = int(input())
print(calc_fib_fast(n))
