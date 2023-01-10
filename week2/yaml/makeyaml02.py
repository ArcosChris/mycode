#!/usr/bin/env python3 
"""Carcos
"""

import yaml

def main():
    """runtime code"""
    
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Create the YAML string
    yamlstring = yaml.dump(hitchhikers)

    ## Display a single string of YAML
    print(yamlstring)

if __name__ == "__main__":
    main()

