from fastapi import FastAPI
from pydantic import BaseModel
import pickle 


filename = 'myModel.pkl'
loaded_model = pickle.load(open(filename, 'rb'))




app = FastAPI()

@app.get("/home")
async def root():
    return {"message": "Hello FastApi!"}


class Item(BaseModel):
    input: list =[]

@app.post("/loadAndServeModel")
async def loadAndServeModel(item: Item):
    anomalyScore = loaded_model.score_samples(item.input).tolist()
    return anomalyScore