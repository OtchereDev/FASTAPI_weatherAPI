
import fastapi
from typing import Optional
from fastapi import Depends
from models.location import Location
from services.openweather import get_report

router=fastapi.APIRouter()

@router.get('/api/weather/{city}')
async def weather(loc:Location=Depends(),
                units:Optional[str]='metric'):
    report =await get_report(city=loc.city,state=loc.state,country=loc.country,units=units)
    return report