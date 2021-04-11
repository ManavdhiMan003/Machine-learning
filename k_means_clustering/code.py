# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:25:11 2021

@author: Nitro 7
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random
import math

# iris data set
iris = pd.read_csv('Iris.csv')
iris = iris.drop(['Id','Species'],axis=1)
iris = iris.sample(frac=1).reset_index(drop=True)


# mall dataset
mall = pd.read_csv('Mall_Customers.csv')
mall = mall.drop(['CustomerID','Gender','Spending Score (1-100)'],axis=1)


def max_min(data):
    mx = []
    mn = []
    # print(data)
    lc = len(data.columns)
    lr = len(data)
    # print(data[1][25],"jajajajajajajj")
    # print(lc,lr)
    mx = data.max()
    mn = data.min()
    # print(mx['SepalLengthCm'])
    mx2 = []
    mn2 = []
    mx2.append(mx['SepalLengthCm'])
    mx2.append(mx['SepalWidthCm'])
    mx2.append(mx['PetalLengthCm'])
    mx2.append(mx['PetalWidthCm'])
    mn2.append(mn['SepalLengthCm'])
    mn2.append(mn['SepalWidthCm'])
    mn2.append(mn['PetalLengthCm'])
    mn2.append(mn['PetalWidthCm'])
    # for i in range(0,lc):
    #     tmn = 10000000000
    #     tmx = -1000000000
    #     for j in range(0,lr):
    #         # print(i,j)
    #         # print(data[i][j])
    #         try:
    #             tmn = min(data[i][j],tmn)
    #             tmx = max(data[i][j],tmx)
    #         except IndexError as e: 
    #             # print(i,j,"panga hai kuch ",e)
                
    #     mx.append(tmx) 
    #     mn.append(tmn) 
    # print(mx2,"\n",mn2)
    return mx2,mn2

# mx,mn = max_min(data)    

# def get_random2(data):
#     mn = []
#     mn.append(data['SepalLengthCm'].mean())
#     mn.append(data['SepalWidthCm'].mean())
#     mn.append(data['PetalLengthCm'].mean())
#     mn.append(data['PetalWidthCm'].mean())
#     return mn
# get_random2(data)

def get_first(mx,mn,k):
    t = []
    ans = 0
    b = True
    for j in range(k):
        for i in range(len(mx)):
            t.append(random.uniform(mn[i],mx[i]))
        if b:
            ans = np.array([t])
            b=False
        else:
            ans = np.append(ans,[t],axis=0)
        t.clear()    

    return ans

# d= get_first(mx,mn,3)
def get_dist(d1,d2):
    # euclidean distance
    ans = 0
    for i in range(len(d1)):
        ans += math.pow(d1[i]-d2[i],2)
    return math.sqrt(ans)
# get_dist(d[0],d[1])
def convert(mx):
    mx2 = []
    mx2.append(mx['SepalLengthCm'])
    mx2.append(mx['SepalWidthCm'])
    mx2.append(mx['PetalLengthCm'])
    mx2.append(mx['PetalWidthCm'])
    return mx2

def iteration(point,data,k):
    k_cluster = {}
    for i in range(k):
        k_cluster[i]=[]
    it = 0
    # it2 = 0
    for i in range(len(data)):
        mn = 1000
        temp = data.iloc[i]
        temp = convert(temp)
        for j in range(len(point)):
            # print(temp,"hhha\n",point[j])
            t = get_dist(temp,point[j])
            if t < mn:
                mn = t
                it = j
        # print(it," hhh ",i)
        k_cluster[it].append(i)        
    return (k_cluster)
def get_points(cluster,k,data):
    t = []
    ans = 0
    b=True
    for i in range(k):
        t = cluster[i]
        temp = []
        t1=0
        t2=0
        t3=0
        t4=0
        for j in t:
            t1+=data['SepalLengthCm'][j]
            t2+=data['SepalWidthCm'][j]
            t3+=data['PetalLengthCm'][j]
            t4+=data['PetalWidthCm'][j]
        if(len(t)!=0):
            t1/=len(t)
            t4/=len(t)
            t3/=len(t)
            t2/=len(t)                  
            temp.append(t1)
            temp.append(t2)
            temp.append(t3)
            temp.append(t4)
        if b:
            if len(temp)==0:
                ans = np.array([[]])
            else:
                ans = np.array([temp])
            b=False
        else:
            if len(temp)==0:
                ans = np.append(ans,[[]],axis=0)
            else:
                ans = np.append(ans,[temp],axis=0)
    # print(ans)
    return ans

def algo(data):
    k = int(input("Enter value of k for means algo : "))
    mx,mn = max_min(data)
    rk_points = get_first(mx,mn,k)    
    # print(rk_points)
    cluster = iteration(rk_points,data,k)
    l_points = 0
    b = True
    z = 0
    # e =0
    while b:
        if z==0:
            l_points = rk_points
        if z!=0:
            compare = l_points==rk_points
            isequal = compare.all()
            if isequal:
                break
            else:
                l_points = rk_points
        rk_points = get_points(cluster,k,data)
        cluster = iteration(rk_points,data,k)    
        z+=1
        # if e == 10: break    
    # for i in range(k):
    #     temp = cluster[i]
    #     ans = []
    #     for it in temp:
    #         v = data.iloc[i]
    #         v = convert(v)
    #         ans.append(v)
    #     plt.plot(ans)
    #     plt.show()
    print(cluster)
    print(rk_points)
    print(z)
    # plt.scatter(data['SepalLengthCm'],data['SepalWidthCm'],color="red")
    # plt.scatter(data['PetalLengthCm'],data['PetalWidthCm'],color="red")
    # plt.plot(cluster[0],cluster[1])
    # plt.show()
# algo(iris) 
    
    
    
    
    
    
    
    

