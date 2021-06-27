import re
f=open('reg.txt')
l=f.read()
r=re.findall('\d+',l)
print(sum([int(i) for i in r]))
f.close()