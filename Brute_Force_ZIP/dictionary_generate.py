# Run this file to generate our dictionary password attack
# Takes approximately 320 seconds

from string import ascii_lowercase
import time

t = time.time()

with open('dict.txt', 'w') as file:
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                for d in ascii_lowercase:
                    file.write(a+b+c+d+'\n')

    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                for d in ascii_lowercase:
                    for e in ascii_lowercase:
                        file.write(a+b+c+d+e+'\n')

    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                for d in ascii_lowercase:
                    for e in ascii_lowercase:
                        for f in ascii_lowercase:
                            file.write(a+b+c+d+e+f+'\n')

print('Completed in', str(time.time() - t), 'seconds')
