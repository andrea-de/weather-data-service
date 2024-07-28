from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WeatherResponse(BaseModel):
    city: str
    temperature: str
    description: str

@app.get("/weather", response_model=WeatherResponse)
def get_weather():
    # Simulate weather data
    weather_data = {
        'city': 'San Francisco',
        'temperature': '20°C',
        'description': 'Sunny'
    }
    return weather_data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
