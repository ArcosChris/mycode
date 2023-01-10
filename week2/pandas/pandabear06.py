#!/usr/bin/python3
"""CARCOS
In pandas, a single point in time is represented as a Timestamp. We can use the to_datetime() function to create Timestamps from strings in a wide variety of date/time formats. Let’s import pandas and convert a few dates and times to Timestamps.
"""

import pandas as pd

def main():
    """run-time code"""
    # to_datetime() automatically infers a date/time format based on the input
    # the ambiguous date '7/8/1952' is assumed to be month/day/year and is interpreted as July 8, 1952
    print(pd.to_datetime('2018-01-15 3:45pm'))
    # 2018-01-15 15:45:00

    # Alternatively, we can use the dayfirst parameter to tell pandas to interpret the date as August 7, 1952.
    print(pd.to_datetime('7/8/1952'))
    # 1952-07-08 00:00:00

    print(pd.to_datetime('7/8/1952', dayfirst=True))
    # 1952-08-07 00:00:00

    # Supply a list or array of strings as input to to_datetime() and it
    # returns a sequence of date/time values in a DatetimeIndex object, which is the core data structure that powers much of pandas time series functionality
    print(pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995']))
    # DatetimeIndex(['2018-01-05', '1952-07-08', '1995-10-10'], dtype='datetime64[ns]', freq=None)
    # In the DatetimeIndex above, the data type datetime64[ns] indicates that the underlying data is stored as 64-bit integers, in units of nanoseconds (ns)
    # This data structure allows pandas to compactly store large sequences of date/time values and efficiently perform vectorized operations using NumPy datetime64 arrays.

    # Dealing with a sequence of strings all in the same date/time format, we can explicitly specify it with the format parameter
    # For very large data sets, this can greatly speed up the performance of to_datetime() compared to the default behavior
    # Any of the format codes from the strftime() and strptime() functions in Python’s built-in datetime module can be used.
    print(pd.to_datetime(['2/25/10', '8/6/17', '12/15/12'], format='%m/%d/%y'))
    # DatetimeIndex(['2010-02-25', '2017-08-06', '2012-12-15'], dtype='datetime64[ns]', freq=None)


if __name__ == "__main__":
    main()

