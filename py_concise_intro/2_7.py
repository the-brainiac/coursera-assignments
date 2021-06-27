def problem2_7():
	a=float(input('Enter length of side one: '))
	b=float(input('Enter length of side two: '))
	c=float(input('Enter length of side three: '))
	s=0.5*(a+b+c)
	area = (s*(s-a)*(s-b)*(s-c))**0.5
	print('Area of a triangle with sides',a,b,c,'is',area)
