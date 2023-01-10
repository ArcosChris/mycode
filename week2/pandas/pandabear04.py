#!/usr/bin/env python3
"""Carcos | Working with Pandas to concat diff files
"""

import pandas as pd


def main():

    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    print(ciscodf)

    print()

    ciscodf.to_json("combined_ciscodata.json")
    ciscodf.to_csv("combined_ciscodata.csv")
    ciscodf.to_excel("combined_ciscodata.xls")


    x = ciscodf.to_dict()
    print(x)

if __name__ == "__main__":
    main()
