import requests
import json

def create_facc():
    response = requests.get('https://randomuser.me/api/')
    #Returns a JSON object of the result
    json_val = response.json()
    # INFO: Name, Date of Birth, Gender, Country, Postal Code, Username, Password, Phone

    DOB = j_print(json_val['results'][0]['dob']['date'])
    GENDER = j_print(json_val['results'][0]['gender'])
    COUNTRY = j_print(json_val['results'][0]['location']['country'])
    POSTAL = j_print(json_val['results'][0]['location']['postcode'])
    USERNAME = j_print(json_val['results'][0]['login']['username'])
    PASSWORD = j_print(json_val['results'][0]['login']['password'] + '!s9W')
    PHONE = j_print(json_val['results'][0]['phone'])
    F_NAME = j_print(json_val['results'][0]['name']['first'])
    L_NAME = j_print(json_val['results'][0]['name']['last'])

    return [str(F_NAME),str(L_NAME),str(USERNAME),str(PASSWORD),str(DOB),str(GENDER), str(COUNTRY),str(POSTAL),str(PHONE)]

# Takes python object and dumps it to a string
def j_print(py_obj):
    return json.dumps(py_obj, sort_keys=True, indent = 4)




