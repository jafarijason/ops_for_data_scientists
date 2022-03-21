from fastapi import FastAPI, Request
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression


url = "pima-indians-diabetes.data.csv"
names = [
    'preg',
    'plas',
    'pres',
    'skin',
    'test',
    'mass',
    'pedi',
    'age',
    'class'
]
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X,
    Y,
    test_size=test_size,
    random_state=seed
)


import pickle


filename = 'finalized_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/loadAndServe")
async def loadAndServe(request: Request):
    body = await request.json()
    # result = loaded_model.score(X_test, Y_test)
    # result = loaded_model.predict([[ 13.   , 153.   ,  88.   ,  37.   , 140.   ,  40.6  ,   1.174,
    # #     39.   ]])
    # print(loaded_model)
    return body
