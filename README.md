<p align="center"><img src="https://raw.githubusercontent.com/HostiFi/cash-register-pi/master/cash-register-pi.png"></p>
From the team that brought you <a href="https://hostifi.net" target="_blank">HostiFi</a>, introducing...

# Cash Register Pi

Raspberry Pi audio alerts for Stripe events

Demo: [![](http://img.youtube.com/vi/GcjIZyMuT_w/0.jpg)](http://www.youtube.com/watch?v=GcjIZyMuT_w "")

I noticed a trend on a Twitter - people like to post screenshots of their Stripe notifications blowing up with payments on launch day. It's a great feeling when months of hard work pays off and the internet rains money upon you. Now you can get that same dopamine rush but with customizable sound effects like "ka-ching" or Drake lyrics.

# Installation Instructions
This was tested on a Raspberry Pi 2 B, but should work on others.

## Install Raspberry Pi OS
1. Install "Raspberry Pi OS (32-bit) with desktop and recommended software" from https://www.raspberrypi.org/downloads/raspberry-pi-os/

2. Log in to the desktop, complete setup, run updates

3. Under Settings > Preferences > Raspberry Pi configuration > Interfaces I enabled SSH and VNC

## Connect Audio Device
4. I'm using an Etekcity Roverbeats T3 Bluetooth speaker, so I paired that under Bluetooth > Add device and right clicked on the volume control to change the audio output to that device.

## Install Cash Register Pi

5. Open a terminal and run the following commands, make sure to set your Stripe API key in config.ini:

cd /home/pi

git clone https://github.com/HostiFi/cash-register-pi.git

pip3 install stripe

mv config.ini.example config.ini

nano config.ini

## Configure logging and cron

6. Set up a cronjob to check for new Stripe events every minute and log errors:

sudo touch /var/log/cash-register-pi.log

sudo chown pi:pi /var/log/cash-register-pi.log

crontab -e

\* \* \* \* \* /usr/bin/python3 /home/pi/cash-register-pi/main.py > /var/log/cash-register-pi.log 2>&1

CTRL+X then y to save

# Troubleshooting
Check /var/log/cash-register-pi.log for any errors

# Feature Wishlist
- OLED display with total $ counts for today, this month, and this year https://www.amazon.com/dp/B078YQDZ17/
- Set sounds/jackpot.mp3 to trigger based on a configurable daily threshold like $1,000
