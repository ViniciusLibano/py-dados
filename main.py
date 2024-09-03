from random import randrange
from fastapi import FastAPI
import t20_assets
import sqlite3

app = FastAPI()

def consultar_classes() -> list[t20_assets.ClassesT20]:
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM classes;')
    resultado: list[t20_assets.ClassesT20] = []
    
    for linha in cursor.fetchall():
        resultado.append(t20_assets.ClassesT20(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6]));

    conn.close()
    
    return resultado

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
    classeFicha = t20_assets.classes[randrange(0,len(t20_assets.classes))]
    racaFicha = t20_assets.racas[randrange(0,len(t20_assets.racas))]
    origemFicha = t20_assets.origens[randrange(0,len(t20_assets.origens))]

    if (classe != None):
        classeFicha = classe;
    
    if (raca != None):
        racaFicha = raca

    return {
        "Atributos":atributosFicha,
        "Origem": origemFicha,
        "Classe":classeFicha,
        "Raca":racaFicha
    }

@app.get("/teste")
def teste():
    classes_t20 = []

    for classe in consultar_classes():
        temp = {
            "id_classe": classe.id,
            "ds_classe": classe.desc,
            "pv_classe": classe.pv,
            "pm_classe": classe.pm,
            "pericias": classe.per,
            "proficiencias": classe.pro,
            "habilidades": classe.hab
        }

        classes_t20.append(temp)


    return {"Classes":classes_t20}

# TODO
# Gerar fichas para players
# Atributos
# Origem
# Classe
# Raça


# Gerar fichas para NPCs