import random
from fastapi import FastAPI

app = FastAPI()

def gerar_atributos() -> list:
    atributos = []
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
    
    return atributos

@app.get("/")
def root():
    return {"Use":"/XdY para rolar dados."}

# Rola dados Simples
@app.get("/{x}d{y}")
def rolar_dados(x:int, y:int):
    resultados = []
    for i in range(x):
        resultados.append(random.randrange(0,y)+1)

    resultados.sort()

    return {
        "Quantidade":x,
        "Lados":y,
        "Resultados":resultados
    }

# Rola atributos de Tormenta20/DnD
@app.get("/t20/atributos")
def t20_atributos():
    return {"Atributos": gerar_atributos()}

# TODO
# Gerar fichas para players
# Gerar fichas para NPCs