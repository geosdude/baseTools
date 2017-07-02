#!/usr/bin/env python
# coding: utf-8
# genPasswd.py
# modified from code found on activestate
# Author: ATC


import baseTools
from baseTools import *
print
if 'win' in sys.platform:
  os.system('cls')
else:
  os.system('clear')
passHstDct = {}
passlen = 8
#print string.ascii_letters   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#print string.digits          0123456789
#print string.punctuation     !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~       !#$%&()*?@^_|
flag = 1
passlen = int(raw_input("Enter password length: "))

while flag == 1:
  cnt = 6
  print
  while cnt > 0:
    pass_gen = lambda length, ascii =  string.ascii_letters + string.digits + """!!!#*--___||""": "".join([list(set(ascii))[random.randint(0,len(list(set(ascii)))-1)] for i in range(length)])
    passwd = pass_gen(passlen)
    print passwd
    print
    cnt = cnt - 1
  print
  flag = P("Do you want to generate more passwords?", validResponses=[121, 110, 89, 78], echo=0)

#! Set these to record the date a password was set.
today = datetime.datetime.now()
DD = datetime.timedelta(days=90)
earlier = (today - DD).strftime("%Y%m%d")
earlier2 = (today - DD).strftime("%d%b%Y")

9

