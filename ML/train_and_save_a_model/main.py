from sklearn.ensemble import IsolationForest
import pickle


X = [[-1.1], [0.3], [0.5], [100]]

clf = IsolationForest(random_state=0).fit(X)

clf.predict([[0.1], [0], [90]])
model=clf

filename = 'myModel.pkl'
pickle.dump(model, open(filename, 'wb'))


