from twilio.rest import Client

account_sid = 'AC251b612273644e0f348686b99acfc185' # Found on Twilio Console Dashboard
auth_token = 'c629c0ebd7b286fd862a64163c46127d' # Found on Twilio Console Dashboard

myPhone = '+254796774831' # Phone number you used to verify your Twilio account
TwilioNumber = '+1(202)902-9288' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)
client.messages.create(
  to=myPhone,
  from_=TwilioNumber,
  media_url='https://raw.githubusercontent.com/programming-liftoff/twilio-python/master/python.png')