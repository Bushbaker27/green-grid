from twilio.rest import Client
import json
import os

try:
    f = open(os.path.dirname(__file__)+"/../ResourcesLib/TwilioCreds.JSON")
    data = json.load(f)
except:
    raise Exception("Must include your Twilio Credentials in a TwilioCreds.JSON file within your Resource Library")


class SendSMS:
    account_sid = data["TWILIO_ACCOUNT_SID"]
    auth_token = data["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    twilio_phone_number = data["TWILIO_PHONE_NUMBER"]
    recipient_phone_number = data["RECIPIENT_PHONE_NUMBER"]

    def SendTractorBegin(self, process, loc):
        self.client.messages.create(
            body="Your Tractor had begun {} at {}".format(process, loc),
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )

    def SendTractorPause(self, process, loc):
        self.client.messages.create(
            body="Your Tractor has paused {} at {}".format(process, loc),
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )

    def SendTractorError(self, loc):
        self.client.messages.create(
            body="Your Tractor is an error state at {}".format(loc),
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )

    def SendInvalidResponse(self):
        self.client.messages.create(
            body="You have responded with an invalid command. Please either say BEGIN or PAUSE",
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )
