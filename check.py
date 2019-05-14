#!/usr/bin/env python3

import os
import sys

if len(sys.argv) < 3:
  print ('missing parameters')
  print ('check.py <filename1> <filename2>')
  exit()

name1 = sys.argv[1]
name2 = sys.argv[2]

size1 = os.stat(name1).st_size
size2 = os.stat(name2).st_size
print ("file 1:",name1, ' size=',size1)
print ("file 2:",name2, ' size=',size2)

if size1 != size2: 
  print('\33[91m'+'files not identical'+'\033[0m')
  exit()

f1 = open(name1, 'rb')
f2 = open(name2, 'rb')

a = 0
fails = 0
while a <= size1:
  b = f1.read(1)
  c = f2.read(1)
  if b == c: 
    d = 'OK'
  else: 
    d = '<--!!' 
    fails = fails + 1
    print ('\33[33m',hex(a),b,c,d,'\033[0m')
  a = a + 1
f1.close()
f2.close()
if fails != 0: 
  print('\33[91m'+'files not identical, uncompared ',fails,'\033[0m')
else:
  print('\33[92m'+'files are identical'+'\033[0m')
