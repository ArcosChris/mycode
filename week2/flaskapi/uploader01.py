#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   A simple Flask server to upload and download files"""

# python3 -m pip install flask
from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Return HTML that allows file uploads
@app.route("/upload")
def upload():
  return render_template("upload.html")

# this endpoint accepts the upload (POST) or download (GET)   
@app.route("/uploader", methods = ["GET", "POST"])
def upload_file():
  if request.method == "GET":  # if method is a get (same as "/upload")
     return render_template("upload.html")
  if request.method == "POST":
     f = request.files["file"]
     f.save(secure_filename(f.filename))
     return "file uploaded successfully"
        
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

