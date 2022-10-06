from json import load
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


appid = os.environ.get("APPID")

city = "Utrecht"

endpoint = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={appid}&units=metric"

response = requests.get(endpoint)

weather_data = response.json()

# specify the elements we want to retreive
weather_temp        = []
weather_feels_like  = []
weather_rain_mm     = []
weather_description = []
weather_dt_txt      = []


for i in range(0, len(weather_data['list'])):
    weather_temp.append(weather_data['list'][i]['main']['temp'])  
    weather_feels_like.append(weather_data['list'][i]['main']['feels_like'])
    try:
        weather_rain_mm.append(0) 
        #weather_rain_mm.append(weather_dict['list'][i]['rain']['3h'])
    except KeyError:
        weather_rain_mm.append(0)  
    weather_description.append(weather_data['list'][i]['weather'][0]['description'])
    weather_dt_txt.append(weather_data['list'][i]['dt_txt'])

new_weather_dict = {
      # part 1: specify structre of dictionary
      date_key: {"temperature": temp, "feels_like": feels_like,  "rain_mm": rain_mm, "description": weather_description} 
      # part 2: iterators
      for date_key, temp, feels_like, rain_mm, weather_description
      # part 3: collections to iterate
      in zip(weather_dt_txt, weather_temp, weather_feels_like, weather_rain_mm, weather_description)             
      }

# convert to DataFrame
weather_df = pd.DataFrame.from_dict(new_weather_dict, orient='index', columns=['temperature', 'feels_like', 'rain_mm', 'description'])

# reset the index
weather_df = weather_df.reset_index().rename(columns={"index": "date"})

pass