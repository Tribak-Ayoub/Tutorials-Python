# Organizing Code with Modules
from utils.formatter import forma_user

forma_user('ayoub', 24)

########

#  File Handling

# Overwrites the file if it does exist
with open('log.txt', 'w') as f:
    f.write('This is a backend log.\n')

# This keeps adding new lines to the same file.
with open('log.txt', 'a') as f:
    f.write('Another log entry.\n')

# Reading a file
with open('log.txt', 'r') as f:
    content = f.read()
    print(content)

########

# Json Handling

# convert python to json
import json

user = {'name': 'ayoub', 'age': 24}
json_str = json.dumps(user)
print(json_str)

# save json to a file
with open('user.json', 'w') as f:
    json.dump(user, f)

# read json from file 
with open('user.json', 'r') as f:
    data = json.load(f)
    print(data['name'])

########

# Using Environment Variables

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print(api_key)

