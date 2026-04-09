import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
data = response.json()

lat = data["iss_position"]["latitude"]
lon = data["iss_position"]["longitude"]
print(f"ISS is at {lat}, {lon}")