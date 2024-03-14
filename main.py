from fastapi import FastAPI

api = FastAPI()

@api.get('/')
async def index():
    return { 'message': 'Hello, World!' }

@api.get('/hello')
async def hello():
    return { 'message': 'Hello, Flask!' }