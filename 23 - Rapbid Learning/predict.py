# https://www.dataquest.io/blog/machine-learning-python/

import pandas as pd
import os
import requests
import json
import ast

r = requests.get('http://whale.hacking-lab.com:2222/gate')
session = r.cookies['session_id']

list=r.text.replace('{"attributes": ["bjRtMw==", "ZzNuZDNy", "NGcz", "YzBsMHI=", "dzMxZ2h0", "bDNuZ3Ro", "c3AwMG4=", "dDQxbA=="], "data": ','')[:-1]
x = ast.literal_eval(list)

with open('data.txt', 'a') as f:
	f.write("w31ght,l3ngth,g3nd3r,c0l0r,n4m3,t41l,sp00n,ag3,g00d\n")
	for i in x:
		f.write(str(i[4])+','+str(i[5])+','+str(i[1])+','+str(i[3])+','+str(i[0])+','+str(i[7])+','+str(i[6])+','+str(i[2])+','+'True'+'\n')

print 'session_id: '+session

train = pd.read_csv('train.txt')
test = pd.read_csv('data.txt')
print "train.shape:"
print(train.shape)
print "test.shape:"
print(test.shape)

print 'head(20): '
print test.head(20)

# Get all the columns from the dataframe.
columns = train.columns.tolist()
# Filter the columns to remove ones we don't want.
columns = [c for c in columns if c not in ["n4m3", "c0l0r", "g3nd3r"]]

# Store the variable we'll be predicting on.
target = "g00d"

# Import the linearregression model.
from sklearn.linear_model import LinearRegression

# Initialize the model class.
model = LinearRegression()
# Fit the model to the training data.
model.fit(train[columns], train[target])

# Import the scikit-learn function to compute error.
from sklearn.metrics import mean_squared_error

# Import the random forest model.
from sklearn.ensemble import RandomForestRegressor

# Initialize the model with some parameters.
model = RandomForestRegressor(n_estimators=100, min_samples_leaf=10, random_state=1)
# Fit the model to the data.
model.fit(train[columns], train[target])
# Make predictions.
predictions = model.predict(test[columns])
# Compute the error.
print 'mean_squared_error:'
print mean_squared_error(predictions, test[target])

solution=""
for item in predictions:
	if item == 1.0:
		solution+='1,'
	else:
		solution+='0,'
post='['+solution[:-1]+']'

headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
cookie = {'session_id': session}
r = requests.post('http://whale.hacking-lab.com:2222/predict', data=post, cookies=cookie, headers=headers)
print r.status_code, r.reason
print r.text
r = requests.get('http://whale.hacking-lab.com:2222/reward', cookies=cookie)
print r.status_code, r.reason

with open('solution.html', 'a') as f:
	f.write(r.text)