from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True 

#My questions: 
# How to better structure the pathing
# How to get an error code under each field and 
# how to handle multiple errors at once

#This is the home screen
@app.route("/", methods=['GET'])

def display_home():

    return render_template('index.html')

@app.route("/error", methods=['POST'])

#username handler
def valid_username():
    username= request.form["username"]
    username= str(username)
    if username == "" :
        return "You must enter a Username"
    if len(username) < 3 or len(username) > 20:
        return "Username must be more than 3 characters long and shorter than 20 characters long."
    else:
        return render_template("welcome.html", username = username)

#password handler
@app.route("/passerror", methods=['POST'])
def valid_password():
    password= request.form["password"]
    verify= request.form["verify"]

    if password == "":
        return "Password is required"
    if verify != password:
        return "Passwords must match"

    return render_template("index.html")
#email handler
@app.route("/emailerror", methods=['POST'])
def valid_email():
    email = request.form('email')
    if '@' and '.' not in email:
        return "Needs valid email" 
#attempt at making proper calling tool for the submit form action
#Crashes flask, says invalid syntax to each one

@app.route("/main",methods=['GET'])
display_home()
valid_username()
valid_password()
valid_email()

app.run()
