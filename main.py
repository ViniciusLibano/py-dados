from random import randrange
from fastapi import FastAPI
import t20_lists

app = FastAPI()

def gerar_atributos() -> list:
    atributos = []
    for i in range(6):
        tempList = []
        for j in range(4):
            tempList.append(randrange(0,6)+1)
        
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
        resultados.append(randrange(0,y)+1)

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

@app.get("/t20/ficha_player")
def t20_ficha_player(classe=None, raca=None):
    atributosFicha = gerar_atributos();
    classeFicha = t20_lists.classes[randrange(0,len(t20_lists.classes))]
    racaFicha = t20_lists.racas[randrange(0,len(t20_lists.racas))]
    origemFicha = t20_lists.origens[randrange(0,len(t20_lists.origens))]

    if (classe != None):
        classeFicha = classe;
    
    if (classe != None):
        racaFicha = raca

    return {
        "Atributos":atributosFicha,
        "Origem": origemFicha,
        "Classe":classeFicha,
        "Raca":racaFicha
    }


# TODO
# Gerar fichas para players
# Atributos
# Origem
# Classe
# Raça


# Gerar fichas para NPCs