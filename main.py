import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

import json
from pathlib import Path

from views import home,weather_api
from services import openweather

api=fastapi.FastAPI()

def configure():
    configure_routing()
    configure_api_key()

def configure_api_key():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f'Warning : {file} not found, you can not continue')
        raise Exception('settings.json expected')

    with open('settings.json')as fin:
        settings=json.load(fin)
        openweather.api_key=settings.get('api_key')

def configure_routing():
    api.mount('/static',StaticFiles(directory='static'),name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(api,port=8000,host='127.0.0.1')
else:
    configure() 
