from fastapi import FastAPI,Request
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
