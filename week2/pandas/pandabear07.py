#!/usr/bin/emv python3
"""Carcos | Creating a DataFrame from a timeseries dataset and working with methods to display data
"""
import pandas as pd

#read csv file
def main():

    opsd_daily = pd.read_csv('netTraffic.csv')
    
    print(opsd_daily.shape)

    print("First 3 rows")
    print(opsd_daily.head(3))

    print("Last 3 rows")
    print(opsd_daily.tail(3))

    print(opsd_daily.dtypes)

    opsd_daily = opsd_daily.set_index('Date')

    print("\nLook at the first three rows after date has been set as the primary index")
    print(opsd_daily.head(3))

    print("\nLook at the last three rows after date has been set as the primary index")
    print(opsd_daily.tail(3))

    # display all of the index values (this is a lot of data)
    input("\nPress ENTER to look at all of the index values associated with the dataset (dates)")
    print(opsd_daily.index)

    # consolidate the above steps into a single line using the index_col and parse_dates parameters of the read_csv() function
    opsd_daily = pd.read_csv('netTraffic.csv', index_col=0, parse_dates=True)

    # add some additional columns to our data
    # Add columns with year, month, and weekday name
    opsd_daily['Year'] = opsd_daily.index.year
    opsd_daily['Month'] = opsd_daily.index.month
    # required to 'pull' the day name (ex. Monday, Tuesday, happy days...)
    opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

    # display a random sampling of 5 rows
    input("\nPress ENTER to look at a random sampling from 5 rows after adding the Year, Month and Weekday Name columns")
    print(opsd_daily.sample(5, random_state=0))


if __name__ == "__main__":
    main()

