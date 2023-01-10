#!/usr/bin/env python3 
"""Carcos | Working with Pandas to concat diff file types
"""

import pandas as pd

def main():

    #using pandas to read csv and json files
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")


    ciscodf = pd.concat([ciscocsv, ciscojson])



    print(ciscodf)


if __name__ == "__main__":
    main()
