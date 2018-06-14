import os
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    resp.message("The robots are coming!! But they are cute.")
    return str(resp)

if __name__ == '__main__':
    app.run(port=5002, debug=True)