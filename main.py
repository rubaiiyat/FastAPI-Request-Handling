from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def home():
    return 'is running'

@app.get('/user/user_id')
async def get_user(user_id:int):
    return {'user_id':user_id}