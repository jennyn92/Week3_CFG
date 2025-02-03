#external database, ask for data
#middleman, job is to receive, bundle and send back.

#address (url) name with api is "endpoint"
#
# import requests
#
# # this endpoint tells the current location for international space station
# endpoint = 'http://api.open-notify.org/iss-now.json'
#
# response = requests.get(endpoint)
#
# data = response.json() #convert to json(dictonary) to make it readable
# print(data)
#
# #printing latitude and longitude
#
# print("latitude is:", data['iss_position']['latitude'])
# print("longitude is:", data['iss_position']['longitude'])
#
#----------------------------------
import requests

endpoint = 'http://api.open-notify.org/astros.json'  # this endpoint returns data about astronauts currently in space

response = requests.get(endpoint) # making a call to the API

print(response.status_code)  # make sure that your connection status code is 200, which means success!

data = response.json()  # lets see what data about people in space we get back from the API response
print(data)


# Note from Hamed - We will teach File Writing and Handling Tmrw

# let's extract data from the response and write it to a file
# we need section 'people' from json, which is a list of dict, so...
# we also need to extract name from each dict item in that list

# with open('astranouts.txt', 'w') as text_file:
#     for item in data['people']:
#         text_file.write(item['name'] + '\n') # added new line character, so each name appears on a new line.