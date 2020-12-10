# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:22:07 2020

@author: Administrator
"""

import string,random,os
name = input('nhập tên thư mực :')
data_size = input('nhập gới hạn dữ liệu (1Mb-1024Mb) :')
check = 1

#while check != 0 :

 #   if (type(data_size) != float) :
  #      data_size = input('Dữ liệu phải là kiểu số')
        #data_size = int(data_size)
   # else :
    #    check = 1
data_size = int(data_size )
while ( data_size < 1 or data_size > 1024 ) :
    data_size = input('Nhập lại size dữ liệu(1Mb-1024Mb):')
    data_size = int(data_size)
# Có vấn đề xảy ra là sau khi qua vòng while thứ nhất, nếu biến nhập lại là chữ thì chương trình vẫn lỗi
# có cách nào để đưa 2 điều kiện vòng while lại hay biến phải thỏa cả 2 vòng while nếu không thì chạy lại không ?.
a = link=os.getcwd()
os.mkdir(name)
os.chdir(name)
name_file = input('name file: ')
print(a)
dl_toi_da = 1000*1024
sl_file = data_size*(2**20)%dl_toi_da
dl_last_file = data_size*(2**20)//dl_toi_da
x = sl_file/1024
n = random.randrange(1000)
def random_char(n):
    return ''.join(random.choice(string.ascii_letters) for x in range(n))
print('Số file có kích thước 1Kb là :',dl_last_file )
print('file lớn nhất có kích thước',x)
for i in range(dl_last_file) :
    f = open(name_file +'.doc','w')
    f.write(random_char(n))
    f.close()


