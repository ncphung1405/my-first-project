# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:06:52 2020

@author: Administrator
"""

import os
list1=[]
list2=[]
for (a,b,c) in os.walk('C:\\'):
	if b!=[]:
		list2.append(b)
	if c!=[]:
		list1.append(c)
print(list1)	
print(list2)
