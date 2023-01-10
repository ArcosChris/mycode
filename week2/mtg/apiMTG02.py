#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get(f"{API}sets")   # this "f" string reads: API + "sets"
                                        # OR, https://api.magicthegathering.io/v1/sets

    # display the methods available to our new object
    print( dir(resp) )

if __name__ == "__main__":
    main()

