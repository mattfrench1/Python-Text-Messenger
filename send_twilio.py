from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("TWILIO_TOKEN")
account = os.getenv("TWILIO_ACCOUNT_SID")
twilio_number = os.getenv("TWILIO_NUMBER")
to_number = os.getenv("NUMBER")  # need country code

client = Client(account, token)

message = client.messages.create(
  from_=twilio_number,
  body='Hello from Twilio',
  to=to_number
)

print(message.sid)