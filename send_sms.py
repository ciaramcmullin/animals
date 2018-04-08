Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
		
SDK Version: 5.x 6.x
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "IS4ad0f38e7faf70f699fcb659426e9287"
auth_token = "e16aecb44eeac999c936ce435515eed2"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+16314870778",
    from_="+13476320375",
    body="Hello there!")
