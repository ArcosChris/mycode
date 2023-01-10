#!/usr/bin/python3
import pandas

def main():

    ## create a python list
    mydata = [
    {'hostname': 'dumbledore', 'ip': '192.168.9.22', 'service': 'objectstorage'},
    {'hostname': 'hermione', 'ip': '10.0.2.66', 'service': 'httpd'}
    ]

    ## create a data frame from our python data
    df = pandas.DataFrame(mydata)

    ## create the csv file without the index labels
    df.to_csv("inventorypandas.csv", index=False)

if __name__ == "__main__":
    main()

