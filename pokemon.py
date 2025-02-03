"""
This API is called 'Pokéapi' pokeapi.co/
It gives access to data about Pokémons
This API is free and does not require any authentication!

Each Pokemon has a number that identifies it

You can retrieve information about different Pokemon from urls

https://pokeapi.co/api/v2/pokemon/6/
"""

import requests

pokemon_number = input("What is the Pokemon's ID? ")

endpoint = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)  # note how we manipulate the url to request data!
#{}.format is using formatting, read document to find which section.
#see above .../pokemon/6/ -user input is getting the number to put into the url and get the data.

response = requests.get(endpoint)
print(response)
#200 = success

pokemon = response.json()
print(pokemon["name"])  #passing the key with print will get the value from that key from the data from api

