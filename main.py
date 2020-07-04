import stripe
import os
import configparser
from gtts import gTTS

config = configparser.ConfigParser()
config.read('/home/pi/cash-register-pi/config.ini')
stripe.api_key = config["Default"]["StripeAPIKey"]
events = stripe.Event.list(limit=100)
last_event = config["Default"]["LastEvent"]

for event in events:
    print(event["id"])
    if event["id"] == last_event:
        break
    if event["type"] == "charge.succeeded":
        text_to_say = str(int(event["data"]["object"]["amount"]) / 100) + " dollars"
        amount_mp3 = gTTS(text=text_to_say, lang="en", slow=False)
        amount_mp3.save("/home/pi/cash-register-pi/sounds/amount.mp3")
        os.system("/usr/bin/cvlc /home/pi/cash-register-pi/sounds/ka-ching.mp3 -q --play-and-exit")
        os.system("/usr/bin/cvlc /home/pi/cash-register-pi/sounds/amount.mp3 -q --play-and-exit")
    
    if event["type"] == "customer.subscription.created":
        os.system("/usr/bin/cvlc /home/pi/cash-register-pi/sounds/squad-goin-up.mp3 -q --play-and-exit")

config["Default"]["LastEvent"] = events.data[0]["id"]
with open('/home/pi/cash-register-pi/config.ini', 'w') as configfile:
    config.write(configfile)
