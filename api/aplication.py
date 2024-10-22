from fastapi import FastAPI
from src.api.comfiguracao import configure_rutes


def creat_app():
    app = FastAPI()

    
    configure_rutes(app)



    return app

'''Executando fução para ligar'''
app = creat_app()