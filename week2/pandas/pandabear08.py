#!/usr/bin/python3
"""CARCOS | Learning to work with Time-based indexing in pandas
"""

import pandas as pd

def main():
    """run-time code"""
    # consolidate the above steps into a single line using the index_col and parse_dates parameters of the read_csv() function
    opsd_daily = pd.read_csv('netTraffic.csv', index_col=0, parse_dates=True)

    # add some additional columns to our data
    # Add columns with year, month, and weekday name
    opsd_daily['Year'] = opsd_daily.index.year
    opsd_daily['Month'] = opsd_daily.index.month
    # required to 'pull' the day name (ex. Monday, Tuesday, happy days...)
    opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

    # select data for a single day using a string such as '2017-08-10'
    input("\nPress ENTER to see the data for 2017-08-10")
    print(opsd_daily.loc['2017-08-10'])

    # select a slice of days, '2014-01-20':'2014-01-22'
    # Note that the slice is inclusive of both endpoints
    input("\nPress ENTER to see the data slice from 2014-01-20 to 2014-01-22")
    print(opsd_daily.loc['2014-01-20':'2014-01-22'])

    # partial-string indexing select all date/times which partially match a given string
    # select the entire year 2006 with opsd_daily.loc['2006']
    # select the entire month of February 2012 with opsd_daily.loc['2012-02']
    input("\nPress ENTER to see the data slice for 2012-02")
    print(opsd_daily.loc['2012-02'])

if __name__ == "__main__":
    main()

