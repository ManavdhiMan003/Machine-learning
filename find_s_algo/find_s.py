# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:09:12 2021

@author: Nitro 7
"""


import pandas as pd
import numpy as np

data = pd.read_csv('dataset2.csv')
print('Dataset used :\n',data)
att = np.array(data.drop(['enjoy sport'],axis=1))

target = np.array(data['enjoy sport'])

print('Attributes : ',att)
print("Target data : ",target)

def get_specific_hypo(att,target): 
    for i, val in enumerate(target):
        if val == "yes":
            specific_hypothesis = att[i].copy()
            break
             
    for i, val in enumerate(att):
        if target[i] == "yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
                     
    return specific_hypothesis
    

print('Final hypothesis : ',get_specific_hypo(att,target))    