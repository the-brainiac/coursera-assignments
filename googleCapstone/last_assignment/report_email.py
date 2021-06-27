#!/usr/bin/env python3
import reports
import os, glob
import requests

t = []
for f in glob.glob("~/supplier-data/descriptions/*"):
        file = open(f)
        data = file.readlines()
        im_name = os.path.basename(f).replace('txt','jpeg')
        d = [data[0].strip(),int(data[1].strip()[:-3])]
        t.append(d)

# t =[['name', 'weight'], ['Watermelon', 500], ['Mango', 300], ['Grape', 200], ['Kiwifruit', 250], ['Plum', 150], ['Lemon', 300], ['Blackberry', 150], ['Strawberry', 240], ['Avocado', 200], ['Apple', 500]]
para = ''
for lis in t:
  para += '<br/>name:{}<br/>weight:{} lbs<br/>'.format(lis[0],lis[1])
# print(para) 
if __name__ == '__main__':
	reports.generate("report.pdf", "Processed Update on July 8, 2020", para)
	
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

	message = emails.generate(sender, receiver, subject, body, "report.pdf")
	emails.send(message)

