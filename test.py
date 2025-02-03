import requests

# from art

# object_id_input = input("Put in your object ID: ")

endpoint = 'https://collectionapi.metmuseum.org/public/collection/v1/departments'

response = requests.get(endpoint)

print(response)

art = response.json()

# print(art['departments'])

for department in art['departments']:
    print(department['displayName'])



