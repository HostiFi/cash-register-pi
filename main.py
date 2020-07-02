import stripe
import os
import configparser

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
        os.system("/usr/bin/cvlc /home/pi/cash-register-pi/sounds/ka-ching.mp3 -q --play-and-exit")
    if event["type"] == "customer.subscription.created":
        os.system("/usr/bin/cvlc /home/pi/cash-register-pi/sounds/squad-goin-up.mp3 -q --play-and-exit")

config["Default"]["LastEvent"] = events.data[0]["id"]
with open('/home/pi/cash-register-pi/config.ini', 'w') as configfile:
    config.write(configfile)
