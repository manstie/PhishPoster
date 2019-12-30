import requests
import os
import random
import secrets
import time
import RandomFields

"""
https://nab-authsec-reffrence6834576523.statrments.com/12acc/nabib/frauds
userid
password
login: Login

https://nab-authsec-reffrence6834576523.statrments.com/12acc/nabib/confirm_card
nabid
osid
continue: Continue

https://nab-authsec-reffrence6834576523.statrments.com/12acc/nabib/confirm_details
cardn4me 
ceceh (card number) #### #### #### ####
exMonth ##
exYear ##
cvv ###
DOBDays ##
DOBMonths ## 
DOBYears ####
limit ####?
continue: Continue

https://nab-authsec-reffrence6834576523.statrments.com/12acc/nabib/finish
FirstName
LastName
SubUnit
StreetName
Town
Postcode
Phone
3mail
passwordem
continue: Continue
"""

#post urls
urls = [
'https://nab-authsec-reffrence6834576523.statrments.com/12acc/nabib/frauds',
'https://nab-authsec-reffrence6834576523.statrments.com/12acc/nabib/confirm_card',
'https://nab-authsec-reffrence6834576523.statrments.com/12acc/nabib/confirm_details',
'https://nab-authsec-reffrence6834576523.statrments.com/12acc/nabib/finish'
]
#valid starting numbers for nab cards
nabnums = ['4017', '4902', '4557', '4336', '4530', '4377']

#generate random post values and send
isgood = True
while(isgood):
    person = RandomFields.randPerson()

    #change these per-site
    headers = {
        'user-agent': RandomFields.randUserAgent(),
        'referrer': 'https://www.' + person['domain'],
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    #random session cookie that the site uses
    cookies = {'PHPSESSID': secrets.token_hex(nbytes=16)}

    #set variables used in post data
    userid = str(random.randint(10000000, 9999999999))
    password = RandomFields.randPassword(random.randint(6, 12))
    osid = '' if bool(random.getrandbits(1)) else str(random.randint(0,99999999))
    firstname = person['first']
    lastname = person['last']
    cardname = firstname + ' ' + lastname
    cardnum = nabnums[random.randint(0,5)] + str(random.randint(1000, 9999)) + str(random.randint(1000, 9999)) + str(random.randint(1000, 9999))
    email = person['email']
    phoneno = RandomFields.randPhoneNumber()
    town = RandomFields.randTown()

    #start posting
    url = urls[0] + '?index_jsp=' + secrets.token_hex(nbytes=32)
    r1 = requests.post(url, headers=headers, allow_redirects=False, cookies=cookies, data={
        'userid' : userid,
        'password' : password,
        'login' : 'Login'
    })
    sleepfor = random.randint(2, 15)
    print(f"Request 1: {r1.ok}, sleeping {sleepfor}")
    time.sleep(sleepfor)

    url = urls[1] + '?index_jsp=' + secrets.token_hex(nbytes=32)
    r1 = requests.post(url, headers=headers, allow_redirects=False, cookies=cookies, data={
        'nabid' : userid,
        'osid' : osid,
        'continue': 'Continue'
    })
    sleepfor = random.randint(2, 15)
    print(f"Request 2: {r1.ok}, sleeping {sleepfor}")
    time.sleep(sleepfor)

    url = urls[2] + '?index_jsp=' + secrets.token_hex(nbytes=32)
    r1 = requests.post(url, headers=headers, allow_redirects=False, cookies=cookies, data={
        'cardn4me' : cardname,
        'ceceh' : cardnum,
        'exMonth': str(random.randint(1, 12)),
        'exYear' : str(random.randint(2020, 2024)),
        'cvv' : str(random.randint(0, 999)).zfill(3),
        'DOBDays' : str(random.randint(1, 31)),
        'DOBMonths' : str(random.randint(1, 12)), 
        'DOBYears' : str(random.randint(1901, 2003)),
        'limit' : str(random.randint(1000, 20000)),
        'continue': 'Continue'
    })
    sleepfor = random.randint(2, 15)
    print(f"Request 3: {r1.ok}, sleeping {sleepfor}")
    time.sleep(sleepfor)

    url = urls[3] + '?index_jsp=' + secrets.token_hex(nbytes=32)
    r1 = requests.post(url, headers=headers, allow_redirects=False, cookies=cookies, data={
        'FirstName' : firstname,
        'LastName' : lastname,
        'SubUnit' : str(random.randint(1, 999)),
        'StreetName' : RandomFields.randStreetName(),
        'Town' : town,
        'Postcode' : str(random.randint(1000, 9999)),
        'Phone' : phoneno,
        '3mail' : email,
        'passwordem' : password,
        'continue': 'Continue'
    })
    sleepfor = random.randint(2, 15)
    print(f"Request 4: {r1.ok}, sleeping {sleepfor}")
    print(f"uid: {userid}\npw: {password}\nname: {cardname}\ncard: {cardnum}\nemail: {email}\nph: {phoneno}\n")
    isgood = r1.ok
    if isgood:
        time.sleep(sleepfor)
    else:
        break

print('blocked :(')