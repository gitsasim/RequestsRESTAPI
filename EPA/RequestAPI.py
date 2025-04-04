import requests
import random
import json
import string

#base_url:
base_url = "https://gorest.co.in"
base_url_sit = "https://api-preprod.enphaseenergy.com"

#Auth token:
auth_token = "Bearer f1dd925c20306f41cea59d42ac025353408ed3c5e8ac050a4e6785e1c4f70f3d"
auth_token_sit = "Bearer eyJhbGciOiJSUzI1NiJ9.eyJhcHBfdHlwZSI6InBhcnRuZXIiLCJ1c2VyX25hbWUiOiJzYXNzaW5naEBlbnBoYXNlZW5lcmd5LmNvbSIsImVubF9jaWQiOiI1IiwiZW5sX3Bhc3N3b3JkX2xhc3RfY2hhbmdlZCI6IjE3MjM0NDY2NjkiLCJhdXRob3JpdGllcyI6WyJST0xFX1VTRVIiXSwiY2xpZW50X2lkIjoiNzcxNzk1NGYyMmIwOGQ2YzAwNDUwMGE2NzcwMDYyOTIiLCJhdWQiOlsib2F1dGgyLXJlc291cmNlIl0sImlzX2ludGVybmFsX2FwcCI6ZmFsc2UsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJleHAiOjE3MjY2NTk4NDgsImVubF91aWQiOiIyMDY3NDk3IiwiYXBwX0lkIjoiMTQwOTYyMzMyMTg1MiIsImp0aSI6IjNkZmE5YTVjLTJkYjQtNGU5NS1iNjgxLWExMjVkYmNkMzExMyJ9.ziK6bh81KgXoNuz6ViR7JTzBKyl9nk4QUeGlCf2CvhLhkfM3SPzYbUbj6vsvNy_ZHuN7k7Gc7uNKyB9zGQFoR1koJceaRoyd4ifhKuIXgv5HIxPkcQoqON2NXjy1Rf5lEOrbi2sqiYGsf4Ocsnu06le9jdrGHp01qx2Uc4SfbzI"
key = "0d5b89f18b6fcd3ca26c493c830d1816"
request_header = {"key": key, "Authorization": auth_token_sit}
#get random email id:
def generate_random_email():
    domain = "sasim.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#GET Request
def get_request():
    url = base_url + "/public/v2/users"
#    print("get url: " +url)
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)
#    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: " ,json_str)
    print("....GET user is done....")
    status_code = response.status_code
    print("Stats code is: ", + status_code)


def get_request_sit():
    # global auth_token_sit
    url = base_url_sit + "/api/v4/systems/1952518/devices"
    headers = request_header
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    # print(json_data)
    json_str = json.dumps(json_data, indent=4)
    print("json response body: " ,json_str)
    print("....GET user is done....")
    status_code = response.status_code
    print("Stats code is: ", + status_code)

#POST Request
def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Sasim1 Kumar1",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
#    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body :", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Sasim1 Kumar1"
    return user_id
    print("....POST user is done....")

#PUT Request

def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Sasim Kumar Singh",
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Sasim Kumar Singh"
    print("....PUT user is done....")


#DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("....DELETE user is done....")

#call
#get_request()
#user_id = post_request()
#put_request(user_id)
#delete_request(user_id)
get_request_sit()