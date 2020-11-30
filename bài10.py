# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:43:27 2020

@author: Administrator
"""

In [27]:
import pandas as pd
In [33]:
df=pd.read_json("https://www.sba.gov/sites/default/files/data.json")
In [34]:
df.head(10)