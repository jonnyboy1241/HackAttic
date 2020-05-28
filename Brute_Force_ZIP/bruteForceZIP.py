#   Challenge info is located at https://hackattic.com/challenges/brute_force_zip

import requests
import config
from subprocess import run
from zipfile import ZipFile

# Send request to get the JSON
r = requests.get('https://hackattic.com/challenges/brute_force_zip/problem?access_token=' + config.access_token)
get_json = r.json()

# Get the .zip file
result = run(['wget', '-q', '-O', 'encrypted.zip', get_json['zip_url']])

# Crack the password
password = run(['/home/jonathan/pkcrack/bin/pkcrack', '-a', '-C', 'encrypted.zip', '-c', 'dunwich_horror.txt', '-P', 'unprotected.zip', '-p', 'dunwich_horror.txt', '-d', 'decrypted.zip'])

with ZipFile('decrypted.zip', 'r') as zp:
    zp.extract('secret.txt')

with open('secret.txt', 'r') as file:
    secret_info = file.readline()

r = requests.post('https://hackattic.com/challenges/brute_force_zip/solve?access_token=' + config.access_token,
    json = {
        'secret':secret_info
    })

print(r.json())

run(['rm', 'encrypted.zip', 'decrypted.zip', 'secret.txt'])
