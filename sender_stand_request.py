from Enpoints import user as user_path
from Enpoints import database as database_path
import configuration
import requests

#Creates a new user, generates a authToken and add in database
def create_new_user(data):
    return requests.post(configuration.URL_SERVICE+user_path.CREATE_USER_PATH, headers=data.header, json=data.body)

#Generates new user and get database user information
def get_database_user(data):
    create_user = create_new_user(data)
    user_result = create_user.json()

    if create_user.ok:
        get_database_response = requests.get(configuration.URL_SERVICE+database_path.GET_USER_DATABASE_PATH+database_path.DATABASES[2]).text
        get_database_list = []
        for l in get_database_response.split("\n"):
            get_database_list.append(l.split(','))

        del get_database_list[0]
        del get_database_list[-1]

        element_required = get_database_list[-1]
        get_database_dictionary = {
            "firstName": element_required[1],
            "phone": element_required[2],
            "authToken": element_required[7],
        }

        result = [user_result["authToken"], get_database_dictionary]

        print(result)
        return result
    else:
        return "Not new elements in the database."