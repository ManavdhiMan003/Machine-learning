# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:46:43 2021

@author: Nitro 7
"""

import pandas as pd
from matplotlib import pyplot as plt
def graph(x,y,lx,ly,t):
   plt.plot(x,y)
   plt.xlabel(lx)
   plt.ylabel(ly)
   plt.title(t)
   # plt.show()
data = pd.read_csv('indian_liver_patient.csv')
graph(data[0],data[2],"haha","yaya","hoho")