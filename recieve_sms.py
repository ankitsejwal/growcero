import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    from_number = request.values.get('From')
    # from_number = request.form['From']
    text_message = request.form["Body"]
    resp.message("-> \nYou texted: " + text_message + ".\nYou texted from: " + str(from_number))
    return str(resp)

if __name__ == '__main__':
    app.run(port=5002, debug=True)