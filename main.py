import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {'root':'root'}

@app.get("/{x}d{y}")
def rolarDados(x:int, y:int):

    resultados = []
    for i in range(x):
        resultados.append(random.randrange(0,y)+1)

    return {
        "Quantidade":x,
        "Lados":y,
        "Resultados":resultados
    }