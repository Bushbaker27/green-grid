import ssl
from pyngrok import ngrok, conf, installer
import os
from flask import Flask, request
import json
from SendSMS import SendSMS

pyngrok_config = conf.get_default()

if not os.path.exists(pyngrok_config.ngrok_path):
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    installer.install_ngrok(pyngrok_config.ngrok_path, context=myssl)

public_url = ngrok.connect(5000).public_url
print(public_url)

app = Flask(__name__)


@app.route("/sms", methods=['POST'])
def sms_reply():
    from_number = request.form['From']
    body = request.form['Body'].lower()
    print(body)
    sendSMS = SendSMS()

    textRequest = {
        "entry": body
    }

    textRequestFile = json.dumps(textRequest, indent=4)

    with open(os.path.dirname(__file__)+"/../ResourcesLib/TextRequest.JSON", "w") as outfile:
        outfile.write(textRequestFile)

    if body == "pause" or body == "begin":
        return body
    else:
        sendSMS.SendInvalidResponse()
        return "invalid"


app.run()
