#!/usr/bin/env python3 
"""
CARCOS | using range in loop
"""

import uuid

amount = int(input("How many UUIDs should we generate? "))

print("Generating UUIDs...")

for i in range(amount):
    print(uuid.uuid4()) #creating new each iteration



