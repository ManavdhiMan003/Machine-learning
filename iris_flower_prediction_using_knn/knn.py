# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:53:13 2021

@author: Nitro 7
"""

import pandas as pd
from matplotlib import pyplot as plt
import math
def seprate(t1,t2,t3,data):
    for i in range (0,data['species'].count()):
        if data['species'].values[i]=='Iris-setosa':
            t1.append(i)
        elif data['species'].values[i]=='Iris-versicolor':
            t2.append(i)
        elif data['species'].values[i]=='Iris-virginica':
            t3.append(i)
    return t1,t2,t3    
def ready(train,t1,t2,t3):
    id=int(len(t1)*0.7)
    for i in range (0,id):
        train.append(t1[i])
    id=int(len(t2)*0.7)
# print(id,"cccccccccccccccccccc")
    for i in range (0,id):
        train.append(t2[i])
    id=int(len(t3)*0.7)
    for i in range (0,id):
        train.append(t3[i])
    return train    

def testing(test,t1,t2,t3):
    for i in range (int(len(t1)*0.7),len(t1)):
        test.append(t1[i])
    for i in range (int(len(t2)*0.7),len(t2)):
        test.append(t2[i])
    for i in range (int(len(t3)*0.7),len(t3)):
        test.append(t3[i])  
    return test  
def predict(data,test,train,k):
    result={}
    correct=0
    
    for i in range (0,tr):
        sl=data['sepal_length'][test[i]]
        sw=data['sepal_width'][test[i]]
        pl=data['petal_length'][test[i]]
        pw=data['petal_width'][test[i]]
        for j in range(0,len(train)):
            sl2=data['sepal_length'][train[j]]-sl
            sw2=data['sepal_width'][train[j]]-sw
            pl2=data['petal_length'][train[j]]-pl
            pw2=data['petal_width'][train[j]]-pw
            ans=sl2*sl2+sw2*sw2+pl2*pl2+pw2*pw2
            ans=math.sqrt(ans)
            result[ans]=data['species'][train[j]]
        # result=sorted(result.keys())
        # print(result)
        # break
        c1=0
        c2=0
        c3=0
        # key=list(result.items())
        count=0
    
        for z in sorted(result):
            if(count==k): break
            if(result[z]=='Iris-setosa'): c1=c1+1
            if(result[z]=='Iris-versicolor'): c2=c2+1
            if(result[z]=='Iris-virginica'): c3=c3+1
            count=count+1
        mx=max(c1,max(c2,c3))
        if(mx==c1):
            if(data['species'][test[i]]=="Iris-setosa"):
                print(test[i]," yes ",data['species'][test[i]])
                correct=correct+1
            else:
                print(test[i]," no ",data['species'][test[i]])
        elif(mx==c2):
            if(data['species'][test[i]]=="Iris-versicolor"):
                print(test[i]," yes ",data['species'][test[i]])
                correct=correct+1
            else:
                print(test[i]," no ",data['species'][test[i]])
        elif(mx==c3):
            if(data['species'][test[i]]=="Iris-virginica"):
                print(test[i]," yes ",data['species'][test[i]])
                correct=correct+1
            else:
                print(test[i]," no ",data['species'][test[i]])
        result.clear()  
    return correct    
data = pd.read_csv('IRIS.csv')
t1=[]
t2=[]
t3=[]           
# print("hahah ",data['species'].values[3])
t1,t2,t3=seprate(t1,t2,t3,data)
test=[]
train=[]
train=ready(train,t1,t2,t3)
test=testing(test,t1,t2,t3)
tr=len(test)
# print(tr,len(train))
nn=[]
acc=[]
for k in range(1,106,2):
    correct=0
    correct=predict(data,test,train,k)
    per=correct/len(test)*100
    print("Accuracy of k = ",k," is ",per)
    nn.append(k)
    acc.append(per)
    
plt.plot(nn,acc)
plt.xlabel("value of k")
plt.ylabel("accuracy")
plt.title("GRAPH BETWEEN ACCURACY AND K")
plt.show()