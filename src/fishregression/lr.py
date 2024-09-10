from typing import Union
from fastapi import FastAPI
from fishregression.model.manager import get_Reg_path
import pickle
import os

app = FastAPI()

with open(get_Reg_path(), "rb") as f:
    linear_model = pickle.load(f)

@app.get("/")
def read_root():
    return {"Hello": "fishpredict"}

def run_prediction(length: float):
    model_path = get_linearReg_path()
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    r = model.predict([[length**2, length]])
    return float(r[0])

@app.get("/fish")
def lr_api(length: float):
    """
        물고기의 무게 예측

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        dict:
          weight (float): 물고기 무게(g)
          length (float): 물고기 길이(cm)
    """
    weight = run_prediction(length)

    return {
                "입력한 길이": length,
                "예측된 무게": weight
            }

