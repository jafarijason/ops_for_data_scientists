import pickle
from fastapi import FastAPI, Request
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import json
import socket



filename = 'finalized_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello World!",
        "hostName": socket.gethostname()
    }


@app.post("/loadAndServe")
async def loadAndServe(request: Request):
    body = await request.json()
    predict = loaded_model.predict(body).tolist()
    return predict
