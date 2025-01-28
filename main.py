from tinydb import TinyDB 

db = TinyDB("user.json")

user1 = {
    "Name": "Zoyodullo",
    "Age": 20,
    "job": "Student"
}
user2 = {
    "Name": "Dilmurod",
    "Age": 25,
    "job": "Student"
}

db.insert_multiple([user1,user2])