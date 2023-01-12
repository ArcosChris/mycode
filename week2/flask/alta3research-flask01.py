#!/usr/bin/env python3
"""Carcos | Working with Flask 
"""
from flask import Flask, redirect,request
from flask import render_template


app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Chris', 'course': 'Python'},
    {'id': 2, 'name': 'Cindy', 'course': 'Python'},
    {'id': 3, 'name': 'Chase', 'course': 'Python'},
    {'id': 4, 'name': 'David J', 'course': 'Python'},
    {'id': 5, 'name': 'David M', 'course': 'Python'},
    {'id': 6, 'name': 'Aeron', 'course': 'Python'},
    {'id': 7, 'name': 'Joe', 'course': 'Python'},
    {'id': 8, 'name': 'Michael', 'course': 'Python'},
]


@app.route("/")
def index():
    return render_template('mainbs.html', data=students)

@app.route("/addstudent", methods=['POST', 'GET'])
def get_students():
    global students

    if request.method == 'POST':
        result = request.form
        new_user = {
            'id': int(result.get('id')),
            'name': result.get('name'),
            'course': result.get('course') 
        }
        students.append(new_user)
        return redirect('/')
    else:
        return render_template('addStudents.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

