#!/usr/bin/env python
# coding: utf-8
# genPasswd.py
# Author: Richard Polk

import baseTools
from baseTools import *
print 
if 'win' in sys.platform:
  os.system('cls')
else:
  os.system('clear')
flag = 1
# print uuid.uuid1()
  
while flag == 1:
  os.system('clear')
  cnt1 = 6  
  print "Machine specific UUID"
  while cnt1 > 0:
	# returns a machine specific uuid
    print uuid.uuid1()   
    cnt1 = cnt1 - 1
  cnt2 = 6
  print "\nCompletely random UUID"   
  while cnt2 > 0:
    # returns a random uuid
    print uuid.uuid4()    
    cnt2 -= 1 # = cnt - 1 
    P() 
  print
  flag = P()
  print 'flag', flag
#import random
#def uniqueid():
#    seed = random.getrandbits(32)
#    while True:
#       yield seed
#       seed += 1  

