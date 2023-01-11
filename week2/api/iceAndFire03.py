#!/usr/bin/env python3 
"""Carcos | Working with OpenAPIs with requests
"""

import requests

API = "https://www.anapioficeandfire.com/api/books"

def main():
    resp = requests.get(API).json()

    for book in resp:
        print(f"{book['name']}, pages - {book['numberOfPages']}")
        print(f"\tAPI URL -> {book['url']}\n")
        print(f"\tISBN -> {book['isbn']}\n")
        print(f"\tPUBLISHER -> {book['publisher']}\n")
        print(f"\tNo. of Characters -> {len(book['characters'])}\n")


if __name__ == "__main__":
    main()



