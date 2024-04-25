import random
import string
from typing import Dict
from fastapi import FastAPI


app = FastAPI(title='Celsiusify')

@app.on_event("startup")
async def startup_event() -> None:
    string_len, num_of_strs = 8, 4
    list_of_ids = [''.join(random.choices(string.ascii_letters + string.digits, k=string_len)) for _ in range(num_of_strs)]
    app.app_identifier = '-'.join(list_of_ids)

@app.get("/convert/")
async def convert_temperature(fahrenheit: float) -> Dict[str, str]:
    # temperature in degrees Celsius (°C) = (temperature in degrees Fahrenheit (°F) - 32) * 5/9
    celsius = (fahrenheit - 32) * 5.0/9.0
    return {"celsius": f'{celsius:.6f}', "app_identifier": app.app_identifier}
