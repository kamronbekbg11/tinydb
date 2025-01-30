from tinydb import TinyDB 


db = TinyDB("students.json")


database = [
    {
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
},
{
    "id": 2,
    "name": "Sultan Abdullayev",
    "age": 22,
    "gender": "Male",
    "contact": "987-654-3210",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 92,
        "science": 85,
        "english": 95
    },
    "attendance": 88,
    "activities": ["Reading", "Writing"],
    "address": {
        "street": "Balkan 123",
        "city": "Tashkent",
        "state": "Uzbekistan",
        "zip_code": "123456"
    }
},
{
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
},
{
    "id": 2,
    "name": "Suxayl Bobomirzayev",
    "age": 22,
    "gender": "male",
    "contact": "987-654-3210",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 92,
        "science": 87,
        "english": 95
    },
    "attendance": 95,
    "activities": ["Read Club", "Drama Club"],
    "address": {
        "street": "city 43",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "60616"
    }
},
{
    "id": 3,
    "name": "Dilmurod Mamarajabov",
    "age": 18,
    "gender": "Male",
    "contact": "555-555-5555",
    "grade_level": "Grade 12",
    "subjects": {
        "english language": 45,
        "russian language": 31,
        "turkish language": 65
    },
    "attendance": 87,
    "activities": ["Dyzudo", "Football"],
    "address": {
        "street": "Samarkand University",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "141500"
    }
},
{
    "id": 4,
    "name": "Moxina Mansurova",
    "age": 15,
    "gender": "Female",
    "contact": "91-777-7777",
    "grade_level": "Grade 8",
    "subjects": {
        "math": 82,
        "science": 93,
        "english": 90
    },
    "attendance": 90,
    "activities": ["Basketball", "Drama Club"],
    "address": {
        "street": "Gagaren",
        "city": "Tashkent",
        "state": "Uzbekistan",
        "zip_code": "10010"
    }
},
{
    "id": 5,
    "name": "Abbos Ravshanov",
    "age": 16,
    "gender": "Male",
    "contact": "888-888-8888",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 95,
        "science": 89,
        "english": 92
    },
    "attendance": 93,
    "activities": ["Gardening", "Drama Club"],
    "address": {
        "street": "Amir Temur 21",
}
},
{
    "id": 6,
    "name": "Nodir Ravshanov",
    "age": 17,
    "gender": "Male",
    "contact": "33-999-9999",
    "grade_level": "Grade 12",
    "subjects": {
        "english language": 67,
        "russian language": 58,
        "turkish language": 75
    },
    "attendance": 88,
    "activities": ["Dyzudo", "Football"],
    "address": {
        "street": "Dinamo 231",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "110000"
    }
},
{
    "id": 7,
    "name": "Aziza Bo'riyeva",
    "age": 15,
    "gender": "Female",
    "contact": "444-444-4444",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 88,
        "science": 91,
        "english": 92
    },
    "attendance": 91,
    "activities": ["Draw Club", "Music Club"],
    "address": {
        "street": "Spitametr",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "90007"
    }
},
{
    "id": 8,
    "name": "Toir Ravshanov",
    "age": 16,
    "gender": "Male",
    "contact": "90-555-5555",
    "grade_level": "Grade 3",
    "subjects": {
        "math": 93,
        "science": 88,
        "english": 91
    },
    "attendance": 92,
    "activities": ["Football", "Drama Club"],
    "address": {
        "street": "Gagaren Avenue 32",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "123456"
    }
},
{
    "id": 9,
    "name": "Alexander Omonov",
    "age": 17,
    "gender": "Male",
    "contact": "50-666-6666",
    "grade_level": "Grade 12",
    "subjects": {
        "english language": 72,
        "russian language": 65,
        "turkish language": 80
    },
    "attendance": 89,
    "activities": ["Dyzudo", "Football"],
    "address": {
        "street": "Tashkent State 134",
        "city": "Tashkent",
        "state": "Uzbekistan",
        "zip_code": "100000"
    }
},
{
    "id": 10,
    "name": "Komil Ulashov",
    "age": 15,
    "gender": "Male",
    "contact": "33-333-3333",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 85,
        "science": 90,
    "english": 90
    },
    "attendance": 90,
    "activities": ["Basketball", "Drama Club"],
    "address": {
        "street": "Mirzarahim 32",
        "city": "Andijan",
        "state": "Uzbekistan",
        "zip_code": "01000"
    }
},
{
    "id": 11,
    "name": "Bobir Suvonov",
    "age": 16,
    "gender": "Male",
    "contact": "22-222-2222",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 92,
        "science": 87,
        "english": 95
    },
    "attendance": 95,
    "activities": ["Gardening", "Drama Club"],
    "address": {
        "street": "Vokzal 32",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "220000"
    }
},
{
    "id": 12,
    "name": "Toshpulatova Iroda",
    "age": 17,
    "gender": "Female",
    "contact": "88-111-3232",
    "grade_level": "Grade 12",
    "subjects": {
        "english language": 45,
        "russian language": 31,
        "turkish language": 65
        },
    "attendance": 87,
    "activities": ["Dyzudo", "Football"],
    "address": {
        "street": " city 222",
        "city": "Navoiy",
        "state": "Uzekistan",
        "zip_code": "690000"
        }
},
{
    "id": 13,
    "name": "Ibrohim Anvarov",
    "age": 15,
    "gender": "Male",
    "contact": "33-444-4444",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 82,
        "science": 93,
        "english": 90
    },
    "attendance": 90,
    "activities": ["Basketball", "Drama Club"],
    "address": {
        "street": "Beruniy 32",
        "city": "Samarkand",
        "state": "Uzbekistan",
        "zip_code": "440000"
    }
},
{
    "id": 14,
    "name": "Natalia Sharapova",
    "age": 16,
    "gender": "Female",
    "contact": "555-555-5555",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 95,
        "science": 89,
        "english": 92
    },
    "attendance": 93,
    "activities": ["Gardening", "Drama Club"],
    "address": {
        "street": "444 Fourth St",
        "city": "Kazan",
        "state": "Russia",
        "zip_code": "320000"
    }
},
{
    "id": 15,
    "name": "Andrei Gavrilov",
    "age": 17,
    "gender": "Male",
    "contact": "666-666-6666",
    "grade_level": "Grade 12",
    "subjects": {
        "english language": 72,
        "russian language": 65,
        "turkish language": 80
    },
    "attendance": 89,
    "activities": ["Dyzudo", "Football"],
    "address": {
        "street": "555 Fifth Ave",
        "city": "New York",
        "state": "NY",
        "zip_code": "10010"
    }
},
{
    "id": 16,
    "name": "Sergey Zaytsev",
    "age": 15,
    "gender": "Male",
    "contact": "333-333-3333",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 85,
        "science": 90,
        "english": 90
    },
    "attendance": 90,
    "activities": ["Basketball", "Drama Club"],
    "address": {
        "street": "666 Sixth St",
        "city": "Los Angeles",
        "state": "CA",
        "zip_code": "90007"
    }
},
{
    "id": 17,
    "name": "Anton Petrov",
    "age": 16,
    "gender": "Male",
    "contact": "222-222-2222",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 92,
        "science": 87,
        "english": 95
    },
    "attendance": 95,
    "activities": ["Gardening", "Drama Club"],
    "address": {
        "street": "777 Seventh St",
        "city": "Moscow",
        "state": "Russia",
        "zip_code": "123456"
    }
},
{
    "id": 18,
    "name": "Valentina Ivanova",
    "age": 17,
    "gender": "Female",
    "contact": "111-111-1111",
    "grade_level": "Grade 12",
    "subjects": {
        "english language": 45,
        "russian language": 31,
        "turkish language": 65
    },
    "attendance": 87,
    "activities": ["Dyzudo", "Football"],
    "address": {
        "street": "888 Eighth St",
        "city": "Vladivostok",
        "state": "Russia",
        "zip_code": "690000"
        }
},
{
    "id": 19,
    "name": "Oleg Kozlov",
    "age": 15,
    "gender": "Male",
    "contact": "444-444-4444",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 82,
        "science": 93,
        "english": 90
    },
    "attendance": 90,
    "activities": ["Basketball", "Drama Club"],
    "address": {
        "street": "999 Ninth St",
        "city": "Samara",
        "state": "Russia",
        "zip_code": "440000"
    }
},
{
    "id": 20,
    "name": "Natalia Sharapova",
    "age": 16,
    "gender": "Female",
    "contact": "555-555-5555",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 95,
        "science": 89,
        "english": 92
    },
    "attendance": 93,
    "activities": ["Gardening", "Drama Club"],
    "address": {
        "street": "101 Tenth St",
        "city": "Kazan",
        "state": "Russia",
        "zip_code": "320000"
    }
},
{
    "id": 21,
    "name": "Andrei Gavrilov",
    "age": 17,
    "gender": "Male",
    "contact": "666-666-6666",
    "grade_level": "Grade 12",
    "subjects": {
        "english language": 72,
        "russian language": 65,
        "turkish language": 80
    },
    "attendance": 89,
    "activities": ["Dyzudo", "Football"],
    "address": {
        "street": "111 Eleventh St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10010"
    }},
{
    "id": 22,
    "name": "Nurzod Quchqorov",
    "age": 20,
    "gender": "male",
    "contact": "98-213-22-12",
    "grade-level": "Grade 3",
    "subjects":{
        "history": 23,
        "economy": 32,
        "politics": 25
    },
    "attendance": 32,
    "activities": ["Art club", "Drama club"],
    "address": {
        "street": "123 4th Ave",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001"
        }},
{
    "id": 23,
    "name": "Muhammad Olimov",
    "age": 21,
    "gender": "male",
    "contact": "98-213-22-12",
    "grade_level": "Grade 4",
    "subjects":{
        "history": 35,
        "economy": 38,
        "politics": 30
    },
    "attendance": 28,
    "activities": ["Art club", "Drama club"],
    "address": {
        "street": "456 5th Ave",
        "city": "New York",
        "state": "NY",
        "zip_code": "10002"
    }},
{
    "id": 24,
    "name": "Vladimir Dorofeev",
    "age": 19,
    "gender": "male",
    "contact": "98-213-22-12",
    "grade_level": "Grade 5",
    "subjects":{
        "history": 30,
        "economy": 28,
        "politics": 35
    },
    "attendance": 35,
    "activities": ["Art club", "Drama club"],
    "address": {
        "street": "789 6th Ave",
        "city": "New York",
        "state": "NY",
        "zip_code": "10003"
    }},
{
    "id": 25,
    "name": "Suresh Nagar",
    "age": 22,
    "gender": "male",
    "contact": "98-213-22-12",
    "grade_level": "Grade 6",
    "subjects":{
        "history": 28,
        "economy": 32,
        "politics": 30
    },
    "attendance": 30,
    "activities": ["Art club", "Drama club"],
    "address": {
        "street": "1010 7th Ave",
        "city": "New York",
        "state": "NY",
        "zip_code": "10004"
    }}

]
db.insert_multiple(database)


