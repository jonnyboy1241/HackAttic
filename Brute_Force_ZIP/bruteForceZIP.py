#   Challenge info is located at https://hackattic.com/challenges/brute_force_zip

import requests

r = requests.get('https://hackattic.com/challenges/brute_force_zip/problem?access_token=')

get_json = r.json()
print(get_json)
