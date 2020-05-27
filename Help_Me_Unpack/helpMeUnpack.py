#   Challenge info is located at https://hackattic.com/challenges/help_me_unpack

import requests
from base64 import b64decode
import struct
import config

# get the encoded data
r = requests.get('https://hackattic.com/challenges/help_me_unpack/problem?access_token=' + config.access_token)
get_json = r.json()

# decode the data
decode = b64decode(get_json['bytes'])

# Unpack the data.
unpacked_data = struct.unpack('iIhfdd', decode)

# post the answer
r = requests.post('https://hackattic.com/challenges/help_me_unpack/solve?access_token=' + config.access_token,
    json = {
        'int':unpacked_data[0],
        'uint':unpacked_data[1],
        'short':unpacked_data[2],
        'float':unpacked_data[3],
        'double':unpacked_data[4],
        'big_endian_double':unpacked_data[4]
        })

print(r.json())
