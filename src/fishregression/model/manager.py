import os

def get_Reg_path():
    f = os.path.abspath(__file__)
    dir_name = os.path.dirname(f)
    #model_path = dir_name + "/" + "model.pkl"
    Reg_path = os.path.join(dir_name, f"Reg.pkl")
    return Reg_path
