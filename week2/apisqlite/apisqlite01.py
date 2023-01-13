#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"

# search for all movies containing string
def movielookup(mykey, searchstring, year = None, vtype = None):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for
       year = optional search year
       vtype = optional video type. Valid options [episode, series, movie]"""
    try:
        # begin constructing API
        api = f"{OMDBURL}s={searchstring}&apikey={mykey}"
        # user is also searching by year
        if year:
            api = api + f"&y={year}"
        # user is also searching by video type
        if vtype == "movie" or vtype == "series" or vtype == "episode":
            api = api + f"&type={vtype}"

        ## open URL to return 200 response
        resp = requests.get(api)
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            # in the line below, the ? are examples of "bind vars"
            # this is best practice, and prevents sql injection attacks
            # never ever use f-strings or concatenate (+) to build your executions
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

def printlocaldb():
    pass
    #cursor = conn.execute("SELECT * from MOVIES")
    #for row in cursor:
    #    print("MOVIE = ", row[0])
    #    print("YEAR = ", row[1])


def main():

    print("Particulating Splines...")

    # read the API key out of a file in the home directory
    mykey = harvestkey()

    # enter a loop condition with menu prompting
    while True:
        # initialize answer
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            1) Search for All Movies Containing String
            2) Search for Movies Containing String, and by Type
            3) Search for Movies Containing String, and by Year
            4) Search for Movies Containing String, and by Type, and by Year 
            99) Exit""")

            answer = input("> ")

        if answer in ["1", "2", "3", "4"]:
            # All searches require a string to include in the search
            searchstring = input("Search all movies in the OMDB. Enter search string: ")

            if answer == "1":
                resp = movielookup(mykey, searchstring)
            elif answer == "2":
                vtype = input("Search by episode, series, or movie? (enter one): ")
                vtype = vtype.lower()
                resp = movielookup(mykey, searchstring, vtype=vtype)
            elif answer == "3":
                year = input("What is the year of release? ")
                resp = movielookup(mykey, searchstring, year=year)
            elif answer == "4":
                vtype = input("Search by episode, series, or movie? (enter one): ")
                vtype = vtype.lower()
                year = input("What is the year of release? ")
                resp = movielookup(mykey, searchstring, year=year, vtype=vtype)

            if resp:
                # display the results
                resp = resp.get("Search")
                print(resp)
                # write the results into the database
                trackmeplease(resp)
            else:
                print("That search did not return any results.")

        # user wants to exit
        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()
