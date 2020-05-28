#   Challenge info is located at https://hackattic.com/challenges/backup_restore

import requests
from base64 import b64decode
import config

# Get the data
r = requests.get('https://hackattic.com/challenges/backup_restore/problem?access_token=' + config.access_token)
get_json = r.json()

# Decode the database dump
decode = b64decode(get_json['dump'])
print(decode)
