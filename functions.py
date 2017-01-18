from __future__ import print_function
import requests
import json


class API():
    def get_all_users(self):
        print("-----------Retrieving all users-------------")
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        data = json.loads(response.text)
        for index, user in enumerate(data):
            print(str(index + 1) + " - " + user['name'])

    def retrieve_user(self, user_id):
        print("-----------Retrieving a single user-------------")
        response = requests.get(
            'https://jsonplaceholder.typicode.com/users/' + str(user_id))
        user_data = json.loads(response.text)
        if not user_data:  # Check if any data has been retrieved
            print("No Results for user with that ID")
            return
        print("Username: " + user_data['name'])
        print("Email: " + user_data['email'])
        print("Phone: " + user_data['phone'])

    def delete_user(self, user_id):
        print("-----------Deleting a user-------------")
        response = requests.delete(
            'https://jsonplaceholder.typicode.com/users/' + str(user_id))
        if response.status_code == 200:  # Successful deletion returns 200 status code with no data
            print("User deleted successfully")
        else:
            print("User with id {0} not found".format(str(user_id)))

    def create_user(self, data):
        print("-----------Creating a  user-------------")
        response = requests.post(
            'https://jsonplaceholder.typicode.com/users', data=data)
        if response.status_code == 201:
            user_details = json.loads(response.text)
            print("User {0} created succesfully".format(user_details['name']))
        else:
            print("Error Occurred Creating new user")

    def update_user(self, user_id, data):
        print("-----------Updating a user-------------")
        response = requests.put(
            'https://jsonplaceholder.typicode.com/users/' + str(user_id), data=data)
        if response.status_code == 200:  # Status code == 200 on successful update
            user_details = json.loads(response.text)
            print("User {0} updated succesfully".format(user_details['name']))
        else:
            print("Error Occurred Updating user")


# api = API()
# api.get_all_users()
# api.retrieve_user(12)
# api.delete_user(14)
# api.create_user({'name': 'James Bond', 'email': 'james@007.com',
#                  'username': '007', 'website': 'www.james007.com'})
# api.update_user(1, {'name': 'Will Smith', 'email': 'will@smith.com',
#                     'username': 'Will', 'website': 'www.smith.com'})
