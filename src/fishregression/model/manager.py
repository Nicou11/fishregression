import os

def get_reg_path():
    f = os.path.abspath(__file__)
    dir_name = os.path.dirname(f)
    #model_path = dir_name + "/" + "model.pkl"
    reg_path = os.path.join(dir_name, f"reg.pkl")
    return reg_path
