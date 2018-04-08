# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import datetime as dt

app = Flask(mood)

@app.route("/sms", methods=['GET', 'POST'])
def end_of_conversation():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message to response
    if dt.datetime.now().hour < 12:
        resp.message("Have a good morning!")
    elif dt.datetime.now().hour > 12 && dt.datetime.now().hour < 5:
        resp.message("Have a good afternoon!")
    else:
        resp.message("Have a good night!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

def 
