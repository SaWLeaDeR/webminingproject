#encoding=utf-8
import os
import sys
import json
from datetime import datetime

import requests
from flask import Flask, request

import pandas as pd
reload(sys)     
sys.setdefaultencoding("utf-8")


data_sites = ["https://raw.githubusercontent.com/omerfdemir/webmining-chatbot/master/data.headlines.csv",
         "https://raw.githubusercontent.com/omerfdemir/webmining-chatbot/master/data.economy.csv",
         "https://raw.githubusercontent.com/omerfdemir/webmining-chatbot/master/data.health.csv",
         "https://raw.githubusercontent.com/omerfdemir/webmining-chatbot/master/data.mag.csv",
         "https://raw.githubusercontent.com/omerfdemir/webmining-chatbot/master/data.scienceandtech.csv",
         "https://raw.githubusercontent.com/omerfdemir/webmining-chatbot/master/data.sport.csv",
         "https://raw.githubusercontent.com/omerfdemir/webmining-chatbot/master/data.turkey.csv",
         "https://raw.githubusercontent.com/omerfdemir/webmining-chatbot/master/data.world.csv"]
data_names = ["headlines","economy","health","mag","scienceandtech","sport","turkey","world"]
j = 0
for i in data_sites:
        
        temp = "data_"+data_names[j]
        vars()[temp] = pd.read_csv(i)
        j += 1
        
        
for j in data_names:
    temp = "data_"+str(j)
    temp2 = "titles_"+str(j)
    temp3 = "links_"+str(j)
    temp4 = "images_"+str(j)
    vars()[temp2] = vars()[temp].iloc[:,0]
    vars()[temp3] = vars()[temp].iloc[:,1].values
    vars()[temp4] = vars()[temp].iloc[:,2].values
    



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

                    
                   # if i in message_text:
                    if "sport" in message_text or "spor" in message_text or "sports" in message_text or "sporu" in message_text or "spordaki" in message_text or "spordakiler" in message_text:
                        titles = titles_sport
                        links = links_sport
                        images = images_sport
                        jsonData = {"elements": []}

                        for i in range(0,10):

                            temp = {
                                "title": titles[i],
                                "subtitle": "",
                                "image_url":images[i],
                                "buttons": [{
                                "type": "web_url",
                                "url": links[i],
                                "title": "See More"}]
                            }
                            jsonData["elements"].append(temp)
                        send_card(sender_id,jsonData["elements"])
                            

                    elif "ekonomi" in message_text or "economy" in message_text or "economies" in message_text or "ekonomidekiler" in message_text or "ekonomidekileri" in message_text:
                        titles = titles_economy
                        links = links_economy
                        images = images_economy
                        jsonData = {"elements": []}
                    

                        for i in range(0,10):

                            temp = {
                                "title": titles[i],
                                "subtitle": "",
                                "image_url":images[i],
                                "buttons": [{
                                "type": "web_url",
                                "url": links[i],
                                "title": "See More"}]
                            }
                            jsonData["elements"].append(temp)
                        send_card(sender_id,jsonData["elements"])

                    elif "gündem" in message_text or "headlines" in message_text or "son dakika" in message_text or "popular" in message_text or "gündemi" in message_text or "gündemdekileri" in message_text:
                        titles = titles_headlines
                        links = links_headlines
                        images = images_headlines
                        jsonData = {"elements": []}

                        for i in range(0,10):

                            temp = {
                                "title": titles[i],
                                "subtitle": "",
                                "image_url":images[i],
                                "buttons": [{
                                "type": "web_url",
                                "url": links[i],
                                "title": "See More"}]
                            }
                            jsonData["elements"].append(temp)
                        send_card(sender_id,jsonData["elements"])

                    elif "health" in message_text or "sağlık" in message_text or "sağlıktakiler" in message_text or "sağlıktakileri" in message_text:
                        titles = titles_health
                        links = links_health
                        images = images_health
                        jsonData = {"elements": []}

                        for i in range(0,10):

                            temp = {
                                "title": titles[i],
                                "subtitle": "",
                                "image_url":images[i],
                                "buttons": [{
                                "type": "web_url",
                                "url": links[i],
                                "title": "See More"}]
                            }
                            jsonData["elements"].append(temp)
                        send_card(sender_id,jsonData["elements"])

                    elif "magazin" in message_text or "mag" in message_text or "magazindekiler" in message_text or "magazindekileri" in message_text or "magazini" in message_text:
                        titles = titles_mag
                        links = links_mag
                        images = images_mag
                        jsonData = {"elements": []}

                        for i in range(0,10):

                            temp = {
                                "title": titles[i],
                                "subtitle": "",
                                "image_url":images[i],
                                "buttons": [{
                                "type": "web_url",
                                "url": links[i],
                                "title": "See More"}]
                            }
                            jsonData["elements"].append(temp)
                        send_card(sender_id,jsonData["elements"])

                    elif "bilim" in message_text or "teknoloji" in message_text or "teknolojidekiler" in message_text or "bilimi" in message_text or "technology" in message_text or "science" in message_text or "teknolojidekileri" in message_text or "bilimdekiler" in message_text or "bilimdekileri" in message_text or "bilimdekileri" in message_text:
                        titles = titles_scienceandtech
                        links = links_scienceandtech
                        images = images_scienceandtech
                        jsonData = {"elements": []}

                        for i in range(0,10):

                            temp = {
                                "title": titles[i],
                                "subtitle": "",
                                "image_url":images[i],
                                "buttons": [{
                                "type": "web_url",
                                "url": links[i],
                                "title": "See More"}]
                            }
                            jsonData["elements"].append(temp)
                        send_card(sender_id,jsonData["elements"])

                    elif "turkey" in message_text or "turk" in message_text or "turkiye" in message_text or "turkiyedeki" in message_text or "turkiyedekiler" in message_text:
                        titles = titles_turkey
                        links = links_turkey
                        images = images_turkey
                        jsonData = {"elements": []}

                        for i in range(0,10):

                            temp = {
                                "title": titles[i],
                                "subtitle": "",
                                "image_url":images[i],
                                "buttons": [{
                                "type": "web_url",
                                "url": links[i],
                                "title": "See More"}]
                            }
                            jsonData["elements"].append(temp)
                        send_card(sender_id,jsonData["elements"])

                    elif "dunya" in message_text or "world" in message_text or "dunyadaki" in message_text or "dunyadakiler" in message_text or "dunyadakileri" in message_text:
                        titles = titles_world
                        links = links_world
                        images = images_world
                        jsonData = {"elements":[]}

                        
                        for i in range(0,10):

                            temp = {
                                "title": titles[i],
                                "subtitle": "",
                                "image_url":images[i],
                                "buttons": [{
                                "type": "web_url",
                                "url": links[i],
                                "title": "See More"}]
                            }
                            jsonData["elements"].append(temp)
                                
                        send_card(sender_id,jsonData["elements"])
                    else:
                        send_message(sender_id,"Hello")
                            

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_card(recipient_id, message_text):

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

def send_message(recipient_id, message_text):

    #log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

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
            "text": message_text
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
            msg = str(msg)
        print (msg)
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
