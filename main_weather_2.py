import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()


appid = os.environ.get("APPID")

city = "Utrecht"

endpoint = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={appid}&units=metric"

response = requests.get(endpoint)

weather_data = response.json()

#
list_dates = []
list_temperature = []
list_description = []

for idx, data in enumerate(weather_data['list']):
    list_dates.append(data['dt_txt'])
    list_temperature.append(data['main']['temp'])
    list_description.append(data['weather'][0]['description'])


# dict comprehension
new_weather_dict = {
                    dt: {
                       'temperature': tmp,
                       'description': descr
                       }
                    for dt, tmp, descr
                    in zip(list_dates, list_temperature, list_description)
                   }

#
weather_df = (pd.DataFrame.from_dict(new_weather_dict, orient="index") 
                .reset_index() 
                .rename(columns={"index": "date"})
                )
                

pass