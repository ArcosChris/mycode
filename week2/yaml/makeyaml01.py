#!/usr/bin/env python3
"""Carcos | Manipulate YAML
"""

import yaml 

def main():

    """runtime code"""
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    with open("galaxyguid.yaml", "w") as zfile:
         yaml.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()
