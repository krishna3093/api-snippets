# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

number = client.incoming_phone_numbers("PN2a0747eba6abf96b7e3c3ff0b4530f6e") \
               .update(voice_url="http://demo.twilio.com/docs/voice.xml",
                       sms_url="http://demo.twilio.com/docs/sms.xml")

print(number.voice_url)
