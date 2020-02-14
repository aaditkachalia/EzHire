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
			
			response={'mess':"Login Successful Bitch",'user_id':user['localId']}
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
	#data={"Name":"Aadit Kachalia","Age":"21","email":"aaditkachalia@gmail.com"}
	if request.method == 'POST':
		user_key=request.get_data()
		user_id=user_key.decode("utf-8")
		print("The user key is ",user_id)
		db=firebase.database()
		success={'success':"Successfull response"}
		user_id=user_id.replace('"','')   
		user_profile=db.child("users").child(user_id).get().val()
		print("The details are....",user_profile)
		hey=json.dumps(user_profile)
		print("YOYOYOYOYO",hey)
		#return json.dumps(user_profile)
	return json.dumps(hey)

@app.route('/register', methods = ['GET', 'POST'])
def register():
	#data={"Name":"Aadit Kachalia","Age":"21","email":"aaditkachalia@gmail.com"}
	if request.method == 'POST':
		user_key=request.get_data()
		user_detail=user_key.decode("utf-8")
		json_data=json.loads(user_detail)
		print("The json_data is ",json_data)
		db=firebase.database()
		email=json_data['email']
		password=json_data['password']
		x=auth.create_user_with_email_and_password(email, password)
		#user_id=x['localId']
		print("Account successfully created bitchhhhhh")
		user_id = auth.sign_in_with_email_and_password(email,password)
		success={'success':"Successfull response"}
		# for element in json_data:
		# 	element.pop('password',True)
		print(db.child("users").child(user_id['localId']).set(json_data))
		print("Successfully created")
		#user_id=user_id.replace('"','')   
		#user_profile=db.child("users").child(user_id).get().val()
		#print("The details are....",user_profile)
		#hey=json.dumps(user_profile)
		#print("YOYOYOYOYO",hey)
		#return json.dumps(user_profile)
	return json.dumps(success)

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
	if request.method == 'POST':
		user_key=request.get_data()
		user_key=request.get_data()
		user_id=user_key.decode("utf-8")
		print("The user key is ",user_id)
		db=firebase.database()
		final_interview={}
		success={'success':"Successfull Interview"}
		user_id=user_id.replace('"','') 
		print("The user id is ",user_id)
		interview_detail = db.child("interview").get().val()
		interview_detail = json.dumps(interview_detail)
		interview_detail=json.loads(interview_detail)
		for i in interview_detail.items():
			if i[1]["user_id"] == user_id:
				final_interview[i[0]] = i[1] 
		print("The interview details ",interview_detail)
		print("The final interview is ",final_interview)
		final_interview=json.dumps(final_interview)
	return json.dumps(final_interview)   

if __name__ == '__main__':
    app.run(debug=True)
