#Python script to check a pwned password using 'Have I been pwned?' API
# https://haveibeenpwned.com/API/v2#SearchingPwnedPasswordsByRange
from hashlib import sha1
import requests

def pwn_sha1(password, enc = 'utf-8'):
    gen_hash = sha1(password.encode(enc)).hexdigest()
    first_5 = gen_hash[0:5]
    last = gen_hash[5:]
    return first_5, last

def check_password():
    password = input('What is your password? \n')
    hash_info = pwn_sha1(password)
    prefix = hash_info[0]
    suffix = hash_info[1]
    url =  'https://api.pwnedpasswords.com/range/' + prefix
    r = requests.get(url)
    results = r.text.split('\n')
    passwords = []
    for item in results:
        cleaned_hash = item.strip('\r')
        loc = cleaned_hash.find(':')
        returned_suffix = cleaned_hash[:loc].lower()
        passwords.append(returned_suffix)
    if suffix in passwords:
        print('Password pwned!')
    else:
        print('Password safe!')
    return 

check_password()
