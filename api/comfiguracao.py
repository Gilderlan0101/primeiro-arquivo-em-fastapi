from fastapi import FastAPI
from src.api.routes import users

def configure_rutes(app: FastAPI):
    '''def onde sera criada as rotas'''
    app.include_router(users.router)

    return app

