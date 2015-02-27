from twilio.rest import TwilioRestClient
import serial
import time

exampleString = ""

def notif():
# Your Account Sid and Auth Token from twilio.com/user/account
  account_sid = "AC5b5e46b16de29eed890699a1230e26a9"
  auth_token  = "70c4ad4a988de702986ad5574f3a147a"
  client = TwilioRestClient(account_sid, auth_token)
 
  message = client.messages.create(body="Test",
      to="+520445521061342",    # Replace with your phone number
      from_="+16615284910") # Replace with your Twilio number
  print message.sid

p = raw_input('Com port(Empty for default): ') or 0
ser = serial.Serial(p, 9600)

var = 1

while var == 1 :  # This constructs an infinite loop
	if ser.read()=="h":
		notif()
		print("revieved")
		
	else:
		print("Waiting...")
		print ser.readline()
		

print "Good bye!"