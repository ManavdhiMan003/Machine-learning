# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:03:29 2021

@author: Nitro 7
"""

import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np
train_data = pd.read_csv('train.csv')

m=0
c=0
# y=mx+c

#  m=sum((x-mean(x))*(y-mean(y)))/(sum(x-mean(x)))
# c = mean(y)-m*(mean(x))
sx=0
sy=0

def mean(train_data):
    sx=0
    sy=0
    n=len(train_data)
    for i in range(n):
        sx=sx+train_data['x'][i]
        sy=sy+train_data['y'][i]
    return sx/n,sy/n    

def get_num_deno(sx,sy,data):
    num=0
    deno=0
    n=len(train_data)
    for i in range(n):
        num = (train_data['x'][i]-sx)*(train_data['y'][i]-sy)
        deno = (train_data['x'][i]-sx)*(train_data['x'][i]-sx)
    return num,deno   

def get_value(train_data):
    n = len(train_data)
    lx = []
    for i in range(n):
        lx.append(train_data['x'][i])
    return lx

sx,sy=mean(train_data)
num,deno = get_num_deno(sx,sy,train_data)
lx = get_value(train_data)

m=num/deno
c=sy-m*sx

# prediction time

test_data = pd.read_csv('test.csv')
n= len(test_data)
x = []
y = []
# print(lx)
lx = np.array(lx)
# print(lx)
for i in range(n):
    x.append(test_data['x'][i])
    y.append(test_data['y'][i])

plt.scatter(x,y,color='black')
plt.plot(lx,c+m*lx,color='red')
