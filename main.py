from fastapi import FastAPI,Request
from pydantic import BaseModel
from enum import Enum
app=FastAPI()

class chooseOption(str,Enum):
    USA='USA',
    UK='UK',
    BD='BD'

@app.get('/country/{country_name}')
async def get_country(country_name:chooseOption):
    return country_name


@app.get('/user/{user_id}')
async def get_users(user_id:int):
    return user_id



#query parameter 
@app.get('/items/')
async def get_items(product:str, price:int):
    return {
        'product':product,
        'price':price,
    }

@app.get('/products')
async def get_products(request:Request):
    return dict(request.query_params)


#Pydantic Base Model
class User(BaseModel):
    name:str
    email:str

@app.post('/user')
async def create_user(user:User):
    return user


#Headers Authorization
@app.get('/headers')
async def get_headers(request:Request):
    headers=dict(request.headers)
    token=headers.get('authorization')
    user_agent=headers.get('user-agent')
    content_type=headers.get('content-type')

    return {
        'token':token,
        'user_agent':user_agent,
        'content_type':content_type
    }
