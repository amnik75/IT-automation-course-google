#!/usr/bin/env python3
import re
import operator,csv

user = {}
error = {}


with open('syslog.log') as f:
  for line in f:
    line = line.strip()
    r = re.search(r'INFO.+\(([\w\.]+)\)',line)
    if r:
      if r.group(1) in user:
        user[r.group(1)][0] += 1
      else:
        user[r.group(1)] = [1,0]
    r = re.search(r'ERROR ([\w \']+) \(([\w\.]+)\)',line)
    if r:
      if r.group(2) in user:
        user[r.group(2)][1] += 1
      else:
        user[r.group(2)] = [0,1]
      error[r.group(1)] = error.get(r.group(1),0) + 1

user = sorted(user.items())
error = sorted(error.items(),key=operator.itemgetter(1),reverse=True)
us = []
er = []
keys1 = ['Error','Count']
key2 = ['Username','INFO','ERROR']

#print(user)
for u in user:
  us.append([u[0],u[1][0],u[1][1]])
us.insert(0,key2)
for e in error:
  er.append([e[0],e[1]])
er.insert(0,keys1)

with open('user_statistics.csv','w') as f:
  w = csv.writer(f)
  w.writerows(us)

with open('error_message.csv','w') as f:
  w = csv.writer(f)
  w.writerows(er)