# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:53:22 2020

@author: Administrator
"""
import os
list1=[]
list2=[]
for (x,y,z) in os.walk('C:\\'):
	print(x) # a= dirpath chỉ ra những thư mục con tại ổ C
	print(y) # b= dirnames xem tên tất cả các thư mục con
	print(z) # c= name file xem têt tất cả các file con