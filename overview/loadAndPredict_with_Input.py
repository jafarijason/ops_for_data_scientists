from sklearn.ensemble import IsolationForest
import pickle
import sys

num1 = int(input('first input?'))
num2 = int(input('second input?'))
num3 = int(input('third input?'))

myInput=[[num1], [num2], [num3]]

filename = 'myModel.pkl'
loaded_model = pickle.load(open(filename, 'rb'))


anomalyScore = loaded_model.score_samples(myInput)

print(anomalyScore)

