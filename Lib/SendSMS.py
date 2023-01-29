# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import json

try:
    f = open('../ResourcesLib/TwilioCreds.JSON')
    data = json.load(f)
except:
    raise Exception("Must include your Twilio Credentials in a TwilioCreds.JSON file within your Resource Library")

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = data["TWILIO_ACCOUNT_SID"]
auth_token = data['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

class SendSMS:
  def SendTractorBegin(self, process, loc):
   client.messages.create(
      body="Your Tractor is beginning to {} at {}".format(process, loc),
      from_="+18335664407",
      to="+15868546361"
    )

sendSMS = SendSMS()
sendSMS.SendTractorBegin("Harvesting", "1,1")