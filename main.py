from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True 

#My questions: 
# How to better structure the pathing
# How to get an error code under each field and 
# how to handle multiple errors at once

# Two helper functions outside of the routes
# Two routes, one welcome and one '/'
# In user signup have all the variables imported (user, pass ect)
#empty strings for all 
#This is the home screen
def valid_username(username):
	if len(username) > 2 and len(username) < 21 and " " not in username:
		return True
	else:
		return False
def valid_email(user_data):
	if user_data:
		if '@' in user_data and '.' in user_data:
			return  True
		else:
			return False
def valid_passmatch(password, verify):
	if password == verify:
		return True
	else: 
		return False
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')
	
@app.route('/welcome', methods=['POST'])
def main():
	username = request.form["username"]
	password = request.form["password"]
	verify = request.form["verify"]
	email = request.form["email"]
	#Request all variables

	username_error= ""
	password_error= ""
	password_missmatch= ""
	email_error= ""
	#Empty error strings

	username_e= "You must enter a Username more than 3 characters in length and less than 21 characters in length"
	password_e= "You must have a Password more than 3 characters in length and less than 21 characters in length"
	password_m= "Your Passwords must match"
	email_m= "Your email must be valid (Contain an @ symbol as well as a .) "
	#Actual error strings to be added

	if valid_username(username) == False:
		username_error = username_e
	if valid_username(password) == False:
		password_error = password_e
	if valid_passmatch(password, verify) == False:
		password_missmatch = password_m
	if email != None:
		if valid_email(email) == False:
			email_error = email_m
	
	
	#logic for tests (If thing doesnt equal true do this)
		if valid_username(username) == False or valid_username(password) == False or valid_passmatch(password, verify) == False or valid_email(email) == False:
			return render_template('index.html', username = username, username_error = username_error, password= password, password_error= password_error, password_missmatch= password_missmatch, verify= verify, email = email, email_error= email_error)
		else:
			return render_template('welcome.html', username = username)
	#render welcome template (If = welcome else = index)
app.run()