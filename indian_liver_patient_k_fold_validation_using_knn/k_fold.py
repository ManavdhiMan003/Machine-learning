# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:46:43 2021

@author: Nitro 7
"""

import pandas as pd
from matplotlib import pyplot as plt
import math
def graph(x,y,lx,ly,t):
   plt.plot(x,y)
   plt.xlabel(lx)
   plt.ylabel(ly)
   plt.title(t)
   plt.show()   

def split(leng,idx,div):
    trn=[]
    tst=[]
    for i in range((idx-1)*div,idx*div):
        if i==0:
            continue
        tst.append(i)
    for i in range((idx-1)*div):
        if i==0:
            continue
        trn.append(i)
    for i in range((idx*div),leng):
        if i==0:
            continue
        trn.append(i)
    return tst,trn    

def predict(data,tst,trn,k):
    result={}
    correct=0
    for i in range(len(tst)):
        x1=data['Total_Bilirubin'][tst[i]]
        x2=data['Direct_Bilirubin'][tst[i]]
        x3=data['Alkaline_Phosphotase'][tst[i]]
        x4=data['Alamine_Aminotransferase'][tst[i]]
        x5=data['Aspartate_Aminotransferase'][tst[i]]
        x6=data['Total_Protiens'][tst[i]]
        x7=data['Albumin'][tst[i]]
        x8=data['Albumin_and_Globulin_Ratio'][tst[i]]
        for j in range(len(trn)):
            x1=data['Total_Bilirubin'][trn[j]]-x1
            x2=data['Direct_Bilirubin'][trn[j]]-x2
            x3=data['Alkaline_Phosphotase'][trn[j]]-x3
            x4=data['Alamine_Aminotransferase'][trn[j]]-x4
            x5=data['Aspartate_Aminotransferase'][trn[j]]-x5
            x6=data['Total_Protiens'][trn[j]]-x6
            x7=data['Albumin'][trn[j]]-x7
            x8=data['Albumin_and_Globulin_Ratio'][trn[j]]-x8
            ans = x1*x1+x2*x2+x3*x3+x4*x4+x5*x5+x6*x6+x7*x7+x8*x8
            ans = math.sqrt(ans)
            result[ans]=data['Dataset'][trn[j]]
    
        c1 = 0
        c2 = 0
        count = 0
        
        for z in sorted(result):
            if(count == k): break
            if(result[z]==1): c1=c1+1
            elif(result[z]==2): c2=c2+1
            count = count + 1
        mx=max(c1,c2)
        if(mx==c1):
            if data['Dataset'][tst[i]] == 1 :
                # print("Yes ",data['Dataset'][tst[i]]," = ","1")
                correct =  correct+1
            # else: print("NO")    
        else:
            if(data['Dataset'][tst[i]]==2):
                # print("Yes ",data['Dataset'][tst[i]]," = ","1")
                correct =  correct+1
            # else:
                # print("NO")
        result.clear()
    return correct        
data = pd.read_csv('indian_liver_patient.csv')
k=int(input("Enter the value in how many parts you want to split the data  "))
# print(k)
t=[]
leng=data['Total_Bilirubin'].count()
div=int(leng/k)
i=1
result=[]
avg=0
grp = {}
K=int(input("Enter value of K use in KNN algo "))
while i<=k:
    tst,trn = split(leng,i,div)
    # print(tst)
    temp = predict(data,tst,trn,K)    
    temp = temp/(len(tst))*100                    
    avg=max(avg,temp)
    grp[i]=temp
    if(temp==avg):
        result.clear()
        result=tst
    i=i+1

ks=list(grp.keys())
val = list(grp.values())

plt.bar(ks,val)
plt.xlabel("Different set of K used")
plt.ylabel("Accuracy")
plt.title("Graph between Accuracy and K-fold")
plt.show()

print("Maximum accuracy : ",avg)
print("Training data to be used : ",result)