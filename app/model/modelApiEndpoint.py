#import pandas as pd
import pickle
import logging
import json
import pandas as pd
import numpy as np
from pathlib import Path
test_path= "test.csv"

__version__ = "0.1.0" #current version of my model

#creating the logs
logging.basicConfig(level=logging.INFO, filename="log_modelApiEndPoint.log", filemode="w", format="%(asctimea)s - %(levelname)s - %(message)s")

Base_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{Base_DIR}/trained_pipeline-{__version__}.pkl","rb") as f:
    model = pickle.load(f) #load the model


def predict_pipepline_from_path(path):
    df_file=''
    try:
        apicsv = pd.read_csv("api.csv",sep=",")
        model.predict(apicsv.loc[[0]])
    except FileNotFoundError:
        logging.warning('File not found.')
    
    model.predict(df_file)

def getPredictionFromTestByIndex():
    apicsv = pd.read_csv(f"{Base_DIR}/api.csv", sep=",")
    #with open("./api.csv", "r") as csvfile:
    #    all_lines = csvfile.readlines()
    return model.predict(apicsv[apicsv.columns]).tolist()
