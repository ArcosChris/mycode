#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Using the Flask-Limiter package to set limits
   on individual API requests from an IP."""

from flask import Flask
## from python3 -m pip install Flask-Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# create an app object from Flask
app = Flask(__name__)

# create a limiter object from Limiter
# limits are being performed by tracking the
# REMOTE ADDRESS of the clients
limiter = Limiter(
    app = app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# we now have TWO decorators on our function
# app.route() describes WHEN to trigger the function
# limiter.limit() describes HOW OFTEN to trigger the function
@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return "Enjoy this message. It will only display once per day."

# No limiter decorator is needed, this function STILL is limited
# by 200 lookups per day, and 50 per hour
@app.route("/fast")
def fast():
    return "I inherit the default limits of 200 per day and 50 per hour."

## limiter().exempt removes all limits on this API
@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG FOREVER!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

