# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:41:02 2020

@author: Administrator
"""

import random
import numpy as np
import string
#chữ cái đầu tiên của tên nên viết hoa
first_string= string.ascii_uppercase
#các chữ cái sau nên viết thường
next_string= string.ascii_lowercase
#n nhận giá trị từ (50->100)
n=random.randrange(50,101)
#tạo list 000...000
list_dict=list(np.zeros(n))
def name_one(): # hàm tạo tên
    #độ dài của tên
    length_name = random.randrange(1, 15)
    #lựa chọn ngẫu nhiên ký tự đầu tiên viết hoa
    k= random.choice(first_string)
    #lựa chọn các kí tự tiếp và nối chúng lại
    for i in range(length_name):
        k+= random.choice(next_string)
    return k # trả về kết quả của hàm = k
def age(): # hàm tạo tuổi
    #tuổi ngẫu nhiên từ 0->100
    rd_age= random.randrange(0,101)
    return rd_age # trả về kết quả của hàm = rd_age
# biến các phần tử của list thành dictonary
for i in range(len(list_dict)):
    list_dict[i]= dictionary = {'name': name_one(), 'age': age()}
print(list_dict)

