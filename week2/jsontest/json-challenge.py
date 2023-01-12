#!/usr/bin/env python3 


import requests

TIME = "http://date.jsontest.com" 
IP = "http://ip.jsontest.com/"
VALID = "http://validate.jsontest.com/"

def main():
    time = requests.get(TIME).json().get('time').replace(" ", "").replace(":", "-")
    ip = requests.get(IP).json().get('ip')

    with open("myservers.txt", "r") as servers:
        myservers = servers.readlines()

    jtest = {}
    jtest['time'] = time
    jtest['ip'] = ip
    jtest['mysvrs'] = myservers

    data = {}
    data['json'] = str(jtest)

    validate = requests.post(VALID, data = data).json()
    
    print(f"Created : {data}")
    print(f"Validate : {validate}")
    print(f"JSON is Valid ? : {validate['validate']}")


if __name__ == "__main__":
    main()
