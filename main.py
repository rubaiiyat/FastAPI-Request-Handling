from fastapi import FastAPI
from enum import Enum
app=FastAPI()

@app.get('/')
async def home():
    return 'is running'

class Category(str, Enum):
    electronics='electronics',
    clothes='clothes',
    instruments='instruments'



@app.get('/user/user_id')
async def get_user(user_id:int):
    return {'user_id':user_id}



@app.get('/products/category')
async def products(category:Category):
    return {
        'Category':category
    }