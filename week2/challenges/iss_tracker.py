#!/usr/bin/env python3
"""Carcos | Challenge for the ISS Tracker api
"""

import requests
import reverse_geocoder as revg
from datetime import datetime

def main():
    API = "http://api.open-notify.org/iss-now.json"
    resp = requests.get(API).json()
    info = resp.get("iss_position")

    location = revg.search((info["latitude"], info["longitude"]))

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {datetime.fromtimestamp(resp.get('timestamp'))} ")
    print(f"Lon: {info.get('longitude')}")
    print(f"Lat: {info.get('latitude')}")
    print(f"City/Country: {location[0]['name']}, {location[0]['cc']}")
    

if __name__ == "__main__":
    main()



