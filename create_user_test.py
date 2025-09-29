import sender_stand_request
import re
from Data_test import user as user_data

# Create a user with n letters
def positive_assert_username(data):
    user_response = sender_stand_request.create_new_user(data)
    # Ok response
    assert user_response.status_code == 201
    #Generate authToken
    assert user_response.json()["authToken"] != ""

def negative_assert_username(data):
    user_response = sender_stand_request.create_new_user(data)
    # Ok response
    assert user_response.status_code == 400
    #Generate authToken
    special_characters = r'[^a-zA-Z0-9]'
    if re.search(special_characters, data.body["firstName"]):
        assert user_response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras latinas, la longitud debe ser de 2 a 15 caracteres."
    elif len(data.body["firstName"]) > 15 or len(data.body["firstName"]) < 2:
        assert user_response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras latinas, la longitud debe ser de 2 a 15 caracteres."


def positive_assert_get_users_database_success_response(data):
    database_response = sender_stand_request.get_database_user(data)
    #Token generated is saved in the database
    assert database_response[1]["authToken"] == database_response[0]
    #The userName saved in the database is equal to send.
    assert database_response[1]["firstName"]== data.body["firstName"]
    #The phone number saved in the database is equal to send.
    assert database_response[1]["phone"] == data.body["phone"]

def negative_assert_get_users_database_error_response(data):
    database_response = sender_stand_request.get_database_user(data)
    #Token generated is saved in the database
    assert database_response == "Not new elements in the database."


#Tests username creation
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert_username(user_data.user_2_characters)

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert_username(user_data.user_15_characters)

def test_create_user_16_letter_in_first_name_get_success_response():
    negative_assert_username(user_data.user_16_characters)

def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_username(user_data.user_1_characters)

def test_create_user_space_in_last_name_get_error_response():
    negative_assert_username(user_data.user_space_characters)

def test_create_user_special_letter_in_last_name_get_error_response():
    negative_assert_username(user_data.user_special_characters)

#Test username saved in database
def test_create_user_2_letter_database_get_success_response():
    positive_assert_get_users_database_success_response(user_data.user_2_characters)

def test_create_user_15_letter_database_get_success_response():
    positive_assert_get_users_database_success_response(user_data.user_15_characters)

def test_create_user_1_letter_database_get_error_response():
    negative_assert_get_users_database_error_response(user_data.user_1_characters)
