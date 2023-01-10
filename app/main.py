from fastapi import FastAPI
from function import *

app=FastAPI()

@app.get('/list')
def generate():
    submit()
    return ""