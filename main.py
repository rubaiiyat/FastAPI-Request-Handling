from fastapi import FastAPI
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


