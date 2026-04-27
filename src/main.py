from random import randint
from fastapi import FastAPI
import random

app = FastAPI()

# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,50000)}

@app.get("/status")
async def status():
    return {"status": "Online"}

@app.get("/perfil")
async def perfil():
    return {
        "nick": "AlexFPS",
        "plataforma": "Steam",
        "jogo_favorito": "Counter-Strike 2",
        "horas_cs": 2850,
        "online": True
    }

@app.get("/inventario")
async def inventario():
    skins = [
        "AK-47 | Redline",
        "AWP | Asiimov",
        "M4A1-S | Hyper Beast",
        "USP-S | Cortex",
        "Desert Eagle | Blaze"
    ]
    return {
        "item_destaque": random.choice(skins),
        "quantidade_itens": len(skins)
    }

@app.get("/mapa")
async def mapa():
    mapas = ["Dust2", "Mirage", "Inferno", "Nuke", "Ancient", "Anubis"]
    return {
        "mapa_sorteado": random.choice(mapas)
    }

@app.get("/rank")
async def rank():
    ranks = ["Prata", "AK", "Xerife", "Águia", "Global"]
    return {
        "rank_atual": random.choice(ranks)
    }
