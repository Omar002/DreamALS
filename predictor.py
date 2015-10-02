from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]


import pandas as pd
import numpy as np 

train=pd.read_csv("national-top6-for-slope.csv")

train["onset_site"] = train["onset_site"].replace("Limb", 0)
train["onset_site"] = train["onset_site"].replace("Limb and Bulbar", 1)
train["onset_site"] = train["onset_site"].replace("Bulbar", 1)
train["onset_site"] = train["onset_site"].replace("Other", 1)
train["onset_site"] = train["onset_site"].fillna(0)

for t in list(train):
    train[t]=train[t].fillna(np.mean(train[t]))

GBR = GradientBoostingRegressor(n_estimators=400,learning_rate=0.006,max_features=3,min_samples_leaf=60, max_depth=5)

x=train[["onset_delta","onset_site","ALSFRS_Total_min","Q1_Speech_min","Q4_Handwriting_min","hands_min"]]

y=train["ALSFRS_slope"]

GBR.fit(x,y)



train = pd.read_csv(input_file,delimiter="|")


delta = train[train[u'Unnamed: 2'] =="onset_delta"]
site = train[train[u'Unnamed: 2'] =="onset_site"]
total = train[train[u'Unnamed: 2'] =="ALSFRS_Total"]
q1 = train[train[u'Unnamed: 2'] =="Q1_Speech"]
q4 = train[train[u'Unnamed: 2'] =="Q4_Handwriting"]
hand = train[train[u'Unnamed: 2'] =="hands"]

    
if delta[u'Unnamed: 3'].values.tolist() :
    a= min(delta[u'Unnamed: 3'].values.tolist()) 
else: a = -501
    

if site[u'Unnamed: 3'].values.tolist() :
    b= min(site[u'Unnamed: 3'].values.tolist()) 
else: b = 0
    

if total[u'Unnamed: 3'].values.tolist() :
    c= min(total[u'Unnamed: 3'].values.tolist()) 
else: c = 31.91
    
if q1[u'Unnamed: 3'].values.tolist() :
    d= min(q1[u'Unnamed: 3'].values.tolist()) 
else: d = 3
    
if q4[u'Unnamed: 3'].values.tolist() :
    e= min(q4[u'Unnamed: 3'].values.tolist()) 
else: e = 3
    
if hand[u'Unnamed: 3'].values.tolist() :
    f= min(hand[u'Unnamed: 3'].values.tolist()) 
else: f = 6

    
 
    
if b == "Limb":
    b=0

if b == "Limb and Bulbar":
    b=1
    
if b == "Bulbar":
    b=1 
if b == "Other":
    b=1





testx = [a,b,c,d,e,f]
result = GBR.predict(testx)
resultnew = "%s|1" % result[0]


f=open(output_file,"w")
f.write(resultnew)
f.close()
