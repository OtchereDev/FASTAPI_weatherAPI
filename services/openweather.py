from typing import Optional
import httpx

api_key:Optional[str]=None

async def get_report(city:str,state:Optional[str],country:str,units:str):
    if state:
        q=f'{city},{state},{country}'
    else:
        q=f'{city},{country}'
             
    url=f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}?units={units }'


    async with httpx.AsyncClient() as client: 
        response= await client.get(url)
        response.raise_for_status()

    data=response.json()
    forecast=data['main']
  

    return forecast