from typing import Union
from fastapi import FastAPI
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

app = FastAPI()

def get_linearReg_path():
    f = os.path.abspath(__file__)
    dir_name = os.path.dirname(f)
    #model_path = dir_name + "/" + "model.pkl"
    linearReg_path = os.path.join(dir_name, f"linearReg.pkl")
    return linearReg_path

with open(get_linearReg_path(), "rb") as f:
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
def fish(length: float):
    """
        물고기의 무게 예측

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        dict:
          weight (float): 물고기 무게(g)
          length (float): 물고기 길이(cm)
    """
    fish_weight = run_prediction(length)

    return {
                "입력한 길이": length,
                "예측된 무게": fish_weight
            }
