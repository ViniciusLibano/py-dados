import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Use":"/XdY para rolar dados."}

@app.get("/{x}d{y}")
def rolar_dados(x:int, y:int):
    resultados = []
    for i in range(x):
        resultados.append(random.randrange(0,y)+1)

    return {
        "Quantidade":x,
        "Lados":y,
        "Resultados":resultados
    }

@app.get("/gerarAtributos")
def gerar_atributos():
    atributos = []
    removidos = []
    for i in range(6):
        tempList = []
        for j in range(4):
            tempList.append(random.randrange(0,6)+1)
        
        tempList.sort()
        tempList.pop(0)
        
        tempVar = 0
        for dado in tempList:
            tempVar+=dado

        atributos.append(tempVar)

    return {"Atributos":atributos}