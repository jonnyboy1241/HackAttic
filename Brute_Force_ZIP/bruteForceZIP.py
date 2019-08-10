#   Challenge info is located at https://hackattic.com/challenges/brute_force_zip

import requests

# Send request to get the JSON
r = requests.get('https://hackattic.com/challenges/brute_force_zip/problem?access_token=')
get_json = r.json()

print(get_json)

# Get the .zip file
r = requests.get(get_json['zip_url'])
filename = "./package.zip"

# Write to the .zip file
file = open(filename, 'wb')
for chunk in r.iter_content(100000):
    file.write(chunk)
file.close()

# Now theres a file named package.zip in the current directory
