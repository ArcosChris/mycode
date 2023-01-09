#!/usr/bin/env python3
"""CARCOS | Dracual Exercise"""


keyword = 'vampire'
count_dracula = 0

with open("dracula.txt", "r") as dracula:
    with open('vampytimes.txt', "w") as vampy:
        for line in dracula:
            if 'vampire' in line.lower():
                count_dracula += 1
                print(line, end="\n")
                vampy.write(line)

print(f"\nThe word vampire appeared {count_dracula} times.")
