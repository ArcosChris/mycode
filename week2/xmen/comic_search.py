#!/usr/bin/env python3 
"""Carcos | Working with Marvel development account for api calls
"""

import argparse 
import time
import requests
import hashlib
from pprint import pprint

COMIC_API = "http://gateway.marvel.com/v1/public/comics/"
def hashbuilder(rand, privkey, pubkey):
     return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()

def get_comic_info(rand, kh, pubk, comic):
    resp = requests.get(f"{COMIC_API}{comic}?ts={rand}&apikey={pubk}&hash={kh}")
    
    if resp.status_code != 200:
        response = None
    else:
        response = resp.json()

    return response


def main():
    
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('\n')

    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    random = str(time.time()).rstrip('\n')

    keyhash = hashbuilder(random, privkey, pubkey)
    
    result = get_comic_info(random, keyhash, pubkey, args.comic)
    
    for r in result['data'].get('results'):
        print(r['title'])
        pprint(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')

    parser.add_argument('--comic', help='Comic to search for')
    args = parser.parse_args()
    main()


