import os
from twilio.rest import Client

account_sid     = os.environ["TWILIO_ACCOUNT_SID"]
auth_token      = os.environ["TWILIO_AUTH_TOKEN"]
my_number       = os.environ["MY_NUMBER"]
twilio_number   = os.environ["TWILIO_NUMBER"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to= my_number, 
    from_= twilio_number,
    body="Twilio is good, but its atleast 7X expensive in Australia as compared to USA!")

print("MESSAGE SENT!")
