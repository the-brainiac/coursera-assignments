import sys
def problem3_6(file1,file2):
	f=open(file1)
	f2=open(file2,'w')
	for i in f.readlines():
		f2.write(str(len(i.strip()))+'\n')
	f.close()
	f2.close()
file1,file2=sys.argv[1],sys.argv[2]
problem3_6(file1,file2)
