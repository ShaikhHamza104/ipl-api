import pandas as pd
import numpy as np
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {
        "Massage":"Success",
        "Mode":"Online",
        "Created By":"Hamza",
    }
