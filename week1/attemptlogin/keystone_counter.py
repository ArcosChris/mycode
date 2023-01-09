#!/usr/bin/env python3
"""
Carcos | Parse keystone logs
"""

login_fail = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as keystone_file:
    for line in keystone_file:
        if "- - - - -] Authorization failed" in line:
            login_fail += 1
    print(f"The number of failed log in attempts is {login_fail}")

