# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:22:51 2020

@author: Administrator
"""
import os
name_folder=input('name folder: ')
link=os.getcwd()
os.mkdir(name_folder)
os.chdir(name_folder)
name_file= input('name file: ')
abc= open(name_file,'w')
abc.close()