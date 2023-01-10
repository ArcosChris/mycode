#!/usr/bin/env python3
"""Carcos | Practice with pandas, convert json to python 
"""

import pandas as pd 



def main():
    
    df = pd.read_json("5movies.json")
    df.to_csv("converted_from_json.csv")


if __name__ == "__main__":
    main()



