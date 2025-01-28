from tinydb import TinyDB 
import requests

db = TinyDB("shop.json")

shop = {
    "iphone": [
        {"name": "iphone 11", 
        "model": "ios",
        "memory": "64"
        },
        {"name": "iphone 12", 
        "model": "ios",
        "memory": "128"
        },
        {"name": "iphone 13", 
        "model": "ios",
        "memory": "256"
        }
    ],

    "samsung": [
        {"name": "samsung Galaxy S21", 
        "model": "android",
        "memory": "128"
        },
        {"name": "samsung Galaxy S21 Ultra", 
        "model": "android",
        "memory": "256"
        },
        {"name": "samsung Galaxy S22",
        "model": "android",
        "memory": "512"
        }
    ],

    "vivo": [
        {"name": "vivo Y93", 
        "model": "android",
        "memory": "64"
        },
        {"name": "vivo Y95", 
        "model": "android",
        "memory": "128"
        },
        {"name": "vivo Y96", 
        "model": "android",
        "memory": "256"
        }
    ]
}


















# db = TinyDB("random.json")

# url = "https://randommer.io/api/Name?nameType=firstname&quantity=10"

# headers = {
#      "X-Api-Key": "29f760dcebe74d798990f7d51cd5e2b4"
# }
# response  = requests.get(url,headers=headers)
# r = response.json()
# for user in r:
#     db.insert({
#         "name": f"{user}"
#     })
