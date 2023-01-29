import ssl

import requests
from pyngrok import ngrok, conf, installer
import os
from flask import Flask, request
import json
from Lib import SendSMS
from Lib import Game

pyngrok_config = conf.get_default()

# Create a local server to host endpoint from
if not os.path.exists(pyngrok_config.ngrok_path):
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    installer.install_ngrok(pyngrok_config.ngrok_path, context=myssl)

public_url = ngrok.connect(5000).public_url
print(public_url)

app = Flask(__name__)

# Twilio end points that gets pinged when there is a response to the phone number provided
@app.route("/sms", methods=['POST'])
def sms_reply():
    body = request.form['Body'].lower()
    send_sms = SendSMS.SendSMS()

    text_request = {
        "entry": body
    }

    text_request_file_update = json.dumps(text_request, indent=4)

    with open(os.path.dirname(__file__)+"/../ResourcesLib/TextRequest.JSON", "w") as outfile:
        outfile.write(text_request_file_update)

    if body == "pause" or body == "begin":
        return body
    else:
        send_sms.send_invalid_response()
        return "invalid"

def runApp():
    app.run(debug=True, use_reloader=False, port=5000, host='0.0.0.0')

def runGame():
    game = Game.Game()
    game.start_game()
