# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:47:19 2020

@author: Administrator
"""

#1.Numpy:
  #- Tạo ma trận:
import numpy as np 
a = np.array(([(2,3,4,5), (4,6,4,8)],
              [(2,4,6,2), (3,6,7,2)],
              [(4,6,3,2), (4,7,9,0)]),dtype=int)
print("Ma trận A= ",a)

  #- Tính tổng 2 ma trận:
import numpy as np
a = np.array(([(2,3,5,6), (2,7,8,4)]),dtype = int)
b = np.array(([(2,9,0,1), (7,4,7,8)]),dtype = int) 
print("ma trận A= ",a)
print("ma trận B= ",b)
print("ma trận A+B= ", a+b)

  #- Tính tích hai ma trận:
import numpy as np 
a = np.array(([((6,8),(3,9)), ((6,3),(8,3))]),dtype = int)
b = np.array(([(5,7,3,7), (6,2,7,2)]),dtype = int)
print("ma trận C= ",a)
print("ma trận D= ",b)
print("ma trận C*D ", a @ b)
 
  