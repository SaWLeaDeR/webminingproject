# coding=utf-8
import os
import sys
import json
from datetime import datetime
from subprocess 

import requests
from flask import Flask, request

import pandas as pd

subprocess.Popen(['Rscript', '/app/webmining.R'],shell=True)


data = pd.read_csv("/app/data.headlines.csv",encoding = "utf-8")
titles = data.iloc[:,0]
links = data.iloc[:,1].values
images = data.iloc[:,2].values



app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event:  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text
                    jsonData = {"elements":[]}
                    for i in range(3,10):

                        temp = {
                            "title": titles[i],
                            "subtitle": "Element #1 of an hscroll",
                            "image_url":images[i],
                            "buttons": [{
                            "type": "web_url",
                            "url": links[i],
                            "title": "web url"}]
                        }
                        jsonData["elements"].append(temp)
                    
                    send_message(sender_id,jsonData["elements"])

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):

    #log("sending message to "+ str(recipient_id) + message_text)

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            #"text": message_text.encode("utf-8")
"attachment": {
		    "type": "template",
		    "payload": {
				"template_type": "generic",
			    "elements": message_text
		    }
  }
                    }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)



def log(msg, *args, **kwargs):  # simple wrapper for logging to stdout on heroku
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            msg = msg.format(*args, **kwargs)
        print (msg)
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)