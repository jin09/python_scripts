from twilio.rest import TwilioRestClient

account_sid = "AC472774823c214ac92d8c774d465af68c" # Your Account SID from www.twilio.com/console
auth_token  = "4c58411772fc6ad3ff31b2c50e219cf0"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="romanoFF??",
    to="+919818002587",    # Replace with your phone number
    from_="+14849334430") # Replace with your Twilio number

print(message.sid)
