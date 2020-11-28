# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:40:48 2020

@author: Administrator
"""

import string,random
n = random.randrange(1,10)
tuoi = random.randrange(1,100)
def random_char(n):
    return ''.join(random.choice(string.ascii_letters) for x in range(n))
dict1 = {'Name':random_char(n),'Age':tuoi}
print(dict1)