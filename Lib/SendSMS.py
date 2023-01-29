from twilio.rest import Client
import json
import os

try:
    twilioCredsFile = open(os.path.dirname(__file__)+"/../ResourcesLib/TwilioCreds.JSON")
    twilioCreds = json.load(twilioCredsFile)
except:
    raise Exception("Must include your Twilio Credentials in a TwilioCreds.JSON file within your Resource Library")


class SendSMS:
    # Gather Twilio credentials from TwilioCreds.JSON
    account_sid = twilioCreds["TWILIO_ACCOUNT_SID"]
    auth_token = twilioCreds["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    twilio_phone_number = twilioCreds["TWILIO_PHONE_NUMBER"]
    recipient_phone_number = twilioCreds["RECIPIENT_PHONE_NUMBER"]

    def send_tractor_begin(self, process, loc):
        self.client.messages.create(
            body="Your Tractor had begun {} at {}".format(process, loc),
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )

    def send_tractor_pause(self, process, loc):
        self.client.messages.create(
            body="Your Tractor has paused {} at {}".format(process, loc),
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )

    def send_tractor_error(self, loc):
        self.client.messages.create(
            body="Your Tractor is an error state at {}".format(loc),
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )

    def send_invalid_response(self):
        self.client.messages.create(
            body="You have responded with an invalid command. Please either say BEGIN or PAUSE",
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )
