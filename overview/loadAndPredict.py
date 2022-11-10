from sklearn.ensemble import IsolationForest
import pickle

myInput=[[0.9], [10], [95]]

filename = 'myModel.pkl'
loaded_model = pickle.load(open(filename, 'rb'))


anomalyScore = loaded_model.score_samples(myInput)

print(anomalyScore)

