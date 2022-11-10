from fastapi import FastAPI
from pydantic import BaseModel

from sklearn.ensemble import IsolationForest
import pickle


filename = 'myModel.pkl'
loaded_model = pickle.load(open(filename, 'rb'))


app = FastAPI()



@app.get("/ServeAndPredict/{input1}/{input2}/{input3}")
async def read_item(input1, input2, input3):
    myInput = [
        [int(input1)],
        [int(input2)],
        [int(input3)]
    ]
    anomalyScore = loaded_model.score_samples(myInput).tolist()
    return anomalyScore
    # return myInput


class Item(BaseModel):
    input: list =[]

@app.post("/loadAndServeModel")
async def loadAndServeModel(item: Item):
    anomalyScore = loaded_model.score_samples(item.input).tolist()
    return anomalyScore
