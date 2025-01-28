from tinydb import TinyDB 
import requests

db = TinyDB("random.json")

url = "https://randommer.io/api/Name?nameType=firstname&quantity=10"

headers = {
     "X-Api-Key": "29f760dcebe74d798990f7d51cd5e2b4"
}
response  = requests.get(url,headers=headers)
r = response.json()
for user in r:
    db.insert({
        "name": f"{user}"
    })
