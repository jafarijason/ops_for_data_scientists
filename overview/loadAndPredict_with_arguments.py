from sklearn.ensemble import IsolationForest
import pickle
import sys

myInput=[[int(sys.argv[1])], [int(sys.argv[2])], [int(sys.argv[3])]]

filename = 'myModel.pkl'
loaded_model = pickle.load(open(filename, 'rb'))


anomalyScore = loaded_model.score_samples(myInput)

print(anomalyScore)

