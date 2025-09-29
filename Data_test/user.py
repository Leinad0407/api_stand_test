headers = {
    "Content-Type": "application/json"
}

user_body = {
    "user_2_characters": {
        "firstName": "Aa",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_15_characters": {
        "firstName": "Aaaaaaaaaaaaaaa",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_1_characters": {
        "firstName": "A",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_16_characters": {
        "firstName": "Аааааааааааааааа",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_space_characters": {
        "firstName": "A Aaa",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_special_characters": {
        "firstName": "№%@",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_numbers_characters": {
        "firstName": "123",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_without_firstName": {
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_empty_firstName":{
        "firstName": "",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    },
    "user_number_firstName":{
        "firstName": 12,
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    }
}

class User:
    def __init__(self, header, body):
        self.header = header
        self.body = body

user_2_characters = User(headers, user_body["user_2_characters"])
user_15_characters = User(headers, user_body["user_15_characters"])
user_1_characters = User(headers, user_body["user_1_characters"])
user_16_characters = User(headers, user_body["user_16_characters"])
user_space_characters = User(headers, user_body["user_space_characters"])
user_special_characters = User(headers, user_body["user_special_characters"])
user_numbers_characters = User(headers, user_body["user_numbers_characters"])
user_without_firstName = User(headers, user_body["user_without_firstName"])
user_empty_firstName = User(headers, user_body["user_empty_firstName"])
user_number_firstName = User(headers, user_body["user_number_firstName"])
