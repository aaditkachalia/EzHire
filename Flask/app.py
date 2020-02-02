from flask import Flask, render_template,request,jsonify,session
import os
import requests
import pyrebase
from flask_cors import CORS,cross_origin
import json
import time

app = Flask(__name__)
cors = CORS(app)

config = {
    'apiKey': "AIzaSyCxI5iyU4O-9HLNI6zL6TwLhJVD1XxV9SQ",
    'authDomain': "ezhire-4d3b2.firebaseapp.com",
    'databaseURL': "https://ezhire-4d3b2.firebaseio.com",
    'projectId': "ezhire-4d3b2",
    'storageBucket': "ezhire-4d3b2.appspot.com",
    'messagingSenderId': "994011825630",
    'appId': "1:994011825630:web:f892a3aecf3b23f37c094f",
    'measurementId': "G-SSBXV8PB9Z"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
app.secret_key = "abc"  
db=firebase.database()


@app.route('/', methods = ['GET', 'POST'])
def login():
	print("Hello")
	if request.method == 'POST':
		print("Hey baby")
		response={'mess':"Login Successful"}
		#response.header.add('Access-Control-Allow-Origin','*')
		byte_data = request.get_data()
		my_string=byte_data.decode("utf-8")
		json_data=json.loads(my_string)
		print("This is the react message bitch!!",json_data)
		email= json_data['email']
		password= json_data['password']
		#print("This is the react message bitch!!",json_data['message'])
		print("Email is ",email)
		print("Password is ",password)
		#print("Trying verification.....")
		#user = auth.sign_in_with_email_and_password(email,password)
		#time.sleep(20)
		#print("Sign in successful",user)
		#x=30+50
		#time.sleep(20)
		#print("Trying to return the message...")
		#response={'mess':"Login Successful Bitches!"}
		try:
			print("Trying verification.....")
			user = auth.sign_in_with_email_and_password(email,password)
			print("Sign in successful ",user)
			print("The user_id is ",user['localId'])
			session['user_id']=user['localId']
			mock_session=session.pop('user_id',None)
			print("The session is..",mock_session)
			response={'mess':"Login Successful Bitch"}
			#return json.dumps(response)
		except Exception as e:
			print(e)
			response={'mess':"Login Unsuccessful"}
			#return json.dumps(response)
		return json.dumps(response) 
		#return 'Hello World!!!'
	#return json.dumps(response)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	data={"Name":"Aadit Kachalia","Age":"21","email":"aaditkachalia@gmail.com"}
	user_id = session.pop('user_id',None)
	print("User id is ",user_id)
	return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
