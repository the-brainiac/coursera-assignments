import random
def problem2_6():
	random.seed(431)
	a=[]
	b=[]
	for i in range(100):
		a.append(random.randint(1,6))
		b.append(random.randint(1,6))
	for i in range(100):
		print(a[i]+b[i])
