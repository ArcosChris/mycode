#!/usr/bin/env python3
"""Carcos | Reading csv file with standard lib
"""

import csv

def main ():
    with open('superbirthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count =0

        for row in csv_reader:
            if line_count == 0:
                print('Column name are {}'.format(", ".join(row)))
                line_count += 1

            print('\t{} aka {} was born in {}.'.format(row["name"],row["heroname"],row["birthday month"]))
            line_count += 1
    # print(f'Processed {line_count} lines.') # python3.6 way to do things
    print('Processed {} lines.'.format(line_count))

if __name__ == "__main__":
    main()
