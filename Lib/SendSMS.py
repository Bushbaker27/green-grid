import os
from twilio.rest import Client
import json
from flask import Flask, request
import ssl
from pyngrok import ngrok, conf, installer

pyngrok_config = conf.get_default()

if not os.path.exists(pyngrok_config.ngrok_path):
    myssl = ssl.create_default_context();
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    installer.install_ngrok(pyngrok_config.ngrok_path, context=myssl)

public_url = ngrok.connect(5000).public_url
print(public_url)

app = Flask(__name__)

try:
    f = open('../ResourcesLib/TwilioCreds.JSON')
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

    def SendTractorEnd(self, process, loc):
        self.client.messages.create(
            body="Your Tractor is finished {} at {}".format(process, loc),
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
            body="You have responded with an invalid command. Please either say START or STOP",
            from_=self.twilio_phone_number,
            to=self.recipient_phone_number
        )


sendSMS = SendSMS()

@app.route("/sms", methods=['POST'])
def sms_reply():
    from_number = request.form['From']
    body = request.form['Body'].lower()

    if body == "stop" or body == "start":
        return body
    else:
        sendSMS.SendInvalidResponse()
        return "invalid"

app.run()
