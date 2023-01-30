import os
from dotenv import load_dotenv, find_dotenv
import requests


url = "https://api.census.gov/data/2022/pep/population"

load_dotenv()
API_KEY = os.getenv("API_KEY")
usr_key = f"&key={API_KEY}"

params = {
    "get": "NAME,POP_2022,PC1Y_2022,PC5Y_2022",
    "for": "place:*",
    "in": "state:*",
    "key": usr_key,
}

response = requests.get(url, params=params)

data = response.json()

for record in data[1:]:
    name, pop_2022, pc1y_2022, pc5y_2022 = record
    if " capital" in name.lower():
        print(f"{name}:")
        print(f"\t2022 total population count: {pop_2022}")
        print(f"\t1-year percent population change: {pc1y_2022}")
        print(f"\t5-year percent population change: {pc5y_2022}\n")

