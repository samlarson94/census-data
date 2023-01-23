import os
from dotenv import load_dotenv, find_dotenv
import requests


host = "https://api.census.gov/data"

year = '/2022'

dataset_acronym = '/acs/acs1'

g = '?get='

variables = 'NAME,B01001_001E'

location = '&for=us:*'

#API KEY
load_dotenv()
API_KEY = os.getenv("API_KEY")
usr_key = f"&key={API_KEY}"

#Query URL
query_url = f"{host}{year}{dataset_acronym}{g}{variables}{location}{usr_key}"
print(query_url)

#Use Request Package to call out the API
response = requests.get(query_url)

#Print response in plain text
print(response.text)
