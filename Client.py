
#Client sevrer Network
"""Creating a client for a simple client server network which will serialise and ncrypt a string 
before sending it to the server"""

import json

# Create an empty dictionary
my_dict = {}

# Create a dictionary with key-value pairs
dictionary = {"name": "Pawan", "age": 40, "city": "Preston"}

#serialse my_dict to json format

json_data = json.dumps(dictionary)
print(json_data)

