import streamlit as st
import pickle
import pandas as pd
import numpy as np
import pickle
from typing import  Optional
from fastapi import FastAPI
from pydantic import BaseModel

pickle_in = open('grid_search.pkl', 'rb') 
Pipeline_lr = pickle.load(pickle_in)

app = FastAPI()
class Request_Body(BaseModel):
    NAICS: float
    Term: float	
    NoEmp: float
    CreateJob: float
    FranchiseCode: float	
    UrbanRural: float	
    GrAppv: float
    LowDoc: str
    RevLineCr: str

    
@app.post('/predict')

def predict(data: Request_Body):
    new_data=pd.DataFrame(dict(data),index=[0])
    class_idex=Pipeline_lr.predict(new_data)[0]
    if class_idex == 0:
      return  "Votre crédit n'a pas été accordé" 
    else:
             return  "Votre crédit a été accordé"  

  