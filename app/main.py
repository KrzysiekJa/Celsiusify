"""
Main module for the Celsiusify application.
"""
import random
import string
from typing import Dict
from fastapi import FastAPI


app = FastAPI(title='Celsiusify')

@app.on_event("startup")
async def startup_event() -> None:
    """
    Generate and set an application identifier on startup.
    """
    string_len, constants_str = 8, string.ascii_letters + string.digits
    list_of_ids = [''.join(random.choices(constants_str, k=string_len)) for _ in range(stop=4)]
    app.app_identifier = '-'.join(list_of_ids)

@app.get("/convert/")
async def convert_temperature(fahrenheit: float) -> Dict[str, str]:
    """
    Convert temperature from Fahrenheit to Celsius, following the equation:
    
    temperature in degrees Celsius (°C) = (temperature in degrees Fahrenheit (°F) - 32) * 5/9
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        Dict[str, str]: Dictionary containing converted temperature in Celsius and app identifier.
    """
    celsius = (fahrenheit - 32) * 5.0/9.0
    return {"celsius": f'{celsius:.6f}', "app_identifier": app.app_identifier}
