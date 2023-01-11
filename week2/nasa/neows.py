#!/usr/bin/python3

import requests
import os
from dotenv import load_dotenv

load_dotenv()

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds(): 
   nasacreds = os.getenv("NASA_KEY").strip("\n")
   return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate =""
    while startdate == "":
        startdate = input("Please enter a start date YYYY-MM-DD\n")

    enddate = input("Please enter an end date YYYY-MM-DD (Optional)\n")
    
    if enddate == "":
        enddate = startdate

    neowrequest = requests.get(f"{NEOURL}start_date={startdate}&end_date={enddate}&api_key={nasacreds}")

    neodata = neowrequest.json()
    
if __name__ == "__main__":
    main()

