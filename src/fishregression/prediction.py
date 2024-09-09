from typing import Union
from fastapi import FastAPI
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

app = FastAPI()

def get_linearReg_path(k=5):
    # from fishmlserv.model.manager import get_model_path
    #f = __file__
    f = os.path.abspath(__file__)
    dir_name = os.path.dirname(f)
    #model_path = dir_name + "/" + "model.pkl"
    linearReg_path = os.path.join(dir_name, f"linearReg{k}.pkl")
    return linearReg_path

with open(get_linearReg_path(), "rb") as f:
    linear_model = pickle.load(f)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fish")
def fish(length: float, weight: float):
    """
    물고기 종류 판별기
    ```
    Args:
        length (float): 물고기 길이(cm)
        weight (float): 물고기 무게(g)
    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    From fish model
    ```
    """
    prediction = linear_model.predict([[length, weight]])

    if prediction[0] == 1:
        fish_class = "도미"
    else:
        fish_class = "빙어"

    return fish_class
