#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Exploring redirection with a simple Flask server. This server has
   the following endpoints:
   
   /admin            - returns 200 + 'Hello Admin'
   /guest/<guesty>   - returns 200 + 'Hello {guesty} Guest'
   /user/<name>      - returns 302 to one of the other 2 endpoints depending on the
                       <name> provided."""

# python3 -m pip install flask
from flask import Flask
from flask import redirect
from flask import url_for

# create flask app instance    
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty} Guest"
    #V2 FORMATTER - return "Hello {} Guest".format(guesty)
    #OLD FORMATTER - return "Hello %s as Guest" % guesty

@app.route("/user/<name>")
def hello_user(name):
    ## if you go to hello_user with a value of admin
    if name =="admin":
        # return a 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("hello_guest",guesty = name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

