def problem3_1(txtfilename):
	f=open(txtfilename)
	data=f.read()
	print(data)
	print()
	print('There are',len(data),'letters in the file.')
	f.close()