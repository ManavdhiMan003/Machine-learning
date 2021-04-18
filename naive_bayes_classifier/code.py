# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:00:22 2021

@author: Nitro 7
"""


import pandas as pd
import math
data = pd.read_csv('Titanic_train.csv')

data  = data.drop(['Name','PassengerId','Cabin','Ticket','Sex'],axis=1)

data['Age'].fillna(data['Age'].mean(), inplace=True)

def seprate(data):
    cond = data['Survived']==1
    ys_data = data[cond]
    ns_data = data[~cond]
    return ys_data,ns_data      
# seprate(data)            
def get_intial_prob(data):
    ns=0
    ys=0
    # ln = len(data)
    for i in range(len(data)):
        if data['Survived'][i]==0:
            ns += 1
        else:
            ys+=1
    return (ys)/(ys+ns),ns/(ys+ns)        


# ys,ns = get_intial_prob(data)
def mean(data,feat):
    # ans = 0
    return sum(data[feat])/len(data)

def std_dev(data,feat):
    mn = mean(data,feat)
    var = 0
    for i in data[feat]:
        # print(data[feat][1])
        # print(i)
        var += pow((i-mn),2)
    # print(var)
    var/=len(data)
    return math.sqrt(var)


def calc_gaussian(x,std,mn):
    # std = std_dev(data,feat)
    # mn = mean(data,feat)
    # 1/(2*pi*std)*e^(-(x-mn)^2/2std)
    return (1/(math.sqrt(2*math.pi*std)))*(math.exp((-1)*pow((x-mn),2)/(2*std)))
    

def get_all_mean(data):
    mn = []
    mn.append(mean(data,'Pclass'))
    mn.append(mean(data,'Age'))
    mn.append(mean(data,'SibSp'))
    mn.append(mean(data,'Parch'))
    mn.append(mean(data,'Fare'))    
    return mn

def get_all_std(data):
    std = []
    std.append(std_dev(data,'Pclass'))
    std.append(std_dev(data,'Age'))
    std.append(std_dev(data,'SibSp'))
    std.append(std_dev(data,'Parch'))
    std.append(std_dev(data,'Fare'))    
    return std

# def is_same()
def get_prob(data,it,ip,mn,std):
    prb = math.log(ip)
    # prb+=math.log((calc_gaussian((data['Pclass'][it]),(mn[0]),(std[0]))))
    # prb+=math.log((calc_gaussian(float(data['Age'][it]),float(mn[1]),float(std[1]))))
    # prb+=math.log((calc_gaussian(float(data['SibSp'][it]),float(mn[2]),float(std[2]))))
    # prb+=math.log((calc_gaussian(float(data['Parch'][it]),float(mn[3]),float(std[3]))))
    # # print((calc_gaussian(float(data['Fare'][it]),float(mn[4]),float(std[4]))))
    # prb+=math.log((calc_gaussian(float(data['Fare'][it]),float(mn[4]),float(std[4]))))
    
    prb+=((calc_gaussian((data['Pclass'][it]),(mn[0]),(std[0]))))
    prb+=((calc_gaussian(float(data['Age'][it]),float(mn[1]),float(std[1]))))
    prb+=((calc_gaussian(float(data['SibSp'][it]),float(mn[2]),float(std[2]))))
    prb+=((calc_gaussian(float(data['Parch'][it]),float(mn[3]),float(std[3]))))
    # print((calc_gaussian(float(data['Fare'][it]),float(mn[4]),float(std[4]))))
    prb+=((calc_gaussian(float(data['Fare'][it]),float(mn[4]),float(std[4]))))
    return prb
        
test = pd.read_csv('Titanic_test.csv')
test = test.drop(['Name','Sex','Ticket','Cabin','PassengerId'],axis=1)

test['Age'].fillna(test['Age'].mean(), inplace=True)
test['Fare'].fillna(test['Fare'].mean(), inplace=True)

# print(get_all_std(test))
check = pd.read_csv('Titanic_gender_submission.csv')

def algo(data,check,test):
    ys,ns = get_intial_prob(data)
    ys_data,ns_data = seprate(data)
    # print(ys_data,ns_data)
    y_mn = []
    y_mn = get_all_mean(ys_data)
    # print(y_mn)
    y_std = []
    y_std = get_all_std(ys_data)
    # print(y_std)
    n_mn = []
    n_mn = get_all_mean(ns_data)
    n_std = []
    n_std = get_all_std(ns_data)
    ok=0
    # print(y_std,n_std,y_mn,n_mn)
    for i in range(len(test)):
        pred_ys = get_prob(test,i,ys,y_mn,y_std)
        pred_ns = get_prob(test,i,ns,n_mn,n_std)
        if pred_ys>pred_ns:
            if(check['Survived'][i]==1):
                # print("pridict 1: ",i)
                ok+=1
        else:
            if(check['Survived'][i]==0):
                # print("pridict 0: ",i)
                ok+=1
                
    print("Accuracy : ",(ok/len(test))*100)
    
    
algo(data,check,test)   
    
    
    
    
    