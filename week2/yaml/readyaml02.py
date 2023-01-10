#!/usr/bin/python3
"""Manipulating data pulled from YAML files | Alta3 Research"""

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    """runtime code"""
    ## Open a blob of YAML data
    with open("myYAML.yml", "r") as myf:
        ## pull in YAML as Python lists and dictionaries
        pyyammy = yaml.load(myf, Loader=yaml.FullLoader)
    ## how does our data currently look?
    print(pyyammy)
    ## add Minecraft to the list of apps
    pyyammy[0]['apps'].append('minecraft')
    ## Did the Python data change?
    print(pyyammy)
    ## open a file to dump out to
    with open("myYAML.yml.updated", "w") as myf:
    ## use the YAML library
    ## USAGE: yaml.dump(input data, file like object)
        yaml.dump(pyyammy, myf)

if __name__ == "__main__":
    main()

