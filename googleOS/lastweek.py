#!/usr/bin/env python3
import re
import operator

error=dict()
per_user=dict()
info=dict()
f=open('syslog.log')
for i in f.readlines():
        line=i.strip()
        if re.search(r'ERROR \w*',line) or re.search(r'INFO \w+',line):
                user=re.findall(r'\(\w+\)',line)
                if len(user)>0:
                        user=user[0][1:-1]
                else:
                        continue
                #print(user)
                if re.search(r'ERROR \w*',line):
                        err=re.findall(r'ERROR \w*',line)[0]
                        error[err]=error.get(err,0)+1
                        per_user[user]=per_user.get(user,0)+1
                        #per_user[user]['info']=per_user[user].get('info',0)
                else:
                        info[user]=info.get(user,0)+1
                        #per_user[user]['error']=per_user[user].get('error',0)
print(error)
print(per_user)
print(info)
f.close()
f1=open('error_message.csv','w')
f2=open('user_statistics.csv','w')
f1.write('Error, Count\n')
f2.write('Username, INFO, ERROR\n')
for line in error:    
        f1.write("{}, {}\n".format(line,error[line]))
for line in per_user:
        f2.write("{}, {}, {}\n".format(line,info.get(line,0),per_user.get(line,0)))
f1.close()
f2.close()


