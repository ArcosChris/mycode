#!/usr/bin/env python3
"""
Carcos | Read file practice
"""
from os import path


def main():

    while True: 
        prompt = input("\nPlease let me know which file you would like me to read:\n")
        dir_path = path.dirname(path.abspath(__file__))
        file = path.join(dir_path, prompt)

        try:
            with open(file, 'r') as user_file: #with open will close the file once ops are complete
                for line in user_file:
                    print(line)
        except FileNotFoundError as e:
            print(f"There seems to be an issue: {e}")
        else:
            break

if __name__ == "__main__":
    main()