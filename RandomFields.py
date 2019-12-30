import os
import string
import random
import secrets


ascii = string.ascii_letters + string.digits + '!@#$%&^*()_+='

roadtypes = [
    'Alley',
    'Arcade',
    'Avenue',
    'Boulevard',
    'Bypass',
    'Circuit',
    'Close',
    'Corner',
    'Court',
    'Crescent',
    'Drive',
    'Esplanade',
    'Green',
    'Grove',
    'Highway',
    'Junction',
    'Lane',
    'Link',
    'Mews',
    'Parade', 
    'Place',
    'Ridge',
    'Road',
    'Square',
    'Street',
    'Terrace'
]

#https://www.randomlists.com/random-names
with open('firstnames.txt') as f:
    firstnames = [x.strip() for x in f.readlines()]

with open('lastnames.txt') as f:
    lastnames = [x.strip() for x in f.readlines()]

with open('emaildomains.txt') as f:
    domains = [x.strip() for x in f.readlines()]

with open('towns.txt') as f:
    towns = [x.strip() for x in f.readlines()]

with open('nouns.txt') as f:
    streets = [x.strip() for x in f.readlines()]
    streets = streets + firstnames + lastnames

useragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0']

if os.path.isfile('useragents.txt'):
    with open('useragents.txt') as f:
        for line in f:
            if not line.startswith("#"):
                useragents.append(line.strip())

def randUserAgent():
    return random.choice(useragents)

def randPassword(length=12):
    return ''.join(random.choice(ascii) for i in range(length))
    
def randRoadType():
    return random.choice(roadtypes)

#todo: correlate town name to post code
def randTown():
    return random.choice(towns)

def randBiasedRoadType():
    roll = random.randint(0, 100)
    if roll < 40:
        return 'Street'
    elif roll < 60:
        return 'Road'
    elif roll < 70:
        return 'Avenue'
    elif roll < 80:
        return 'Boulevard'
    elif roll < 85:
        return 'Lane'
    elif roll < 90:
        return 'Way'
    elif roll < 95:
        return 'Drive'
    else:
        return 'Court'

def randStreetName():
    return random.choice(streets) + ' ' + randBiasedRoadType()

def randPhoneNumber(areacode='04'):
    return areacode + str(random.randint(0, 99999999)).zfill(8)

def randPerson():
    domain = random.choice(domains)
    firstname = random.choice(firstnames)
    lastname = random.choice(lastnames)
    return {
        'first': firstname,
        'last' : lastname,
        'domain': domain,
        'email': firstname + '.' + lastname + str(random.randint(0, 99)) + '@' + domain,
    }