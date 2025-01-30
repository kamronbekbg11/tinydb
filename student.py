from tinydb import TinyDB 


db = TinyDB("students.json")


st_1 = {
    "id": 1,
    "name": "Ziyodullo Elmurodov",
    "age": 23,
    "gender": "Male",
    "contact": "123-456-7890",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 85,
        "science": 90,
        "english": 88
    },
    "attendance": 92,
    "activities": ["Basketball", "Football"],
    "address": {
        "street": "Beruniy 87",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "141500"
    }
}

db.insert(st_1)
