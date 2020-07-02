# Cash Register Pi
Raspberry Pi audio alerts for Stripe events

For those of us who have online businesses, money is just a number moving over the internet into our bank accounts. It happens quietly and automatically each day. Maybe it would be fun to have some sounds to remind us about it.

Cash Register Pi will play sounds/ka-ching.mp3 for each new charge.succeeded event, and sounds/squad-goin-up.mp3 for each new customer.subscription.created event.

# Installation instructions
This was tested on a Raspberry Pi 2 B, but should work on others.

1. Install "Raspberry Pi OS (32-bit) with desktop and recommended software" from https://www.raspberrypi.org/downloads/raspberry-pi-os/

2. Log in to the desktop, complete setup, run updates

3. Under Settings > Preferences > Raspberry Pi configuration > Interfaces I enabled SSH and VNC

4. I'm using an Etekcity Roverbeats T3 Bluetooth speaker, so I paired that under Bluetooth > Add device and right clicked on the volume control to change the audio output to that device.

5. Open a terminal and run the following commands, make sure to set your Stripe API key in config.ini:

cd /home/pi

git clone https://github.com/reillychase/cash-register-pi.git

pip3 install stripe

mv config.ini.example config.ini

nano config.ini

6. Set up a cronjob to check for new Stripe events every minute:

sudo touch /var/log/cash-register-pi.log

sudo chown pi:pi /var/log/cash-register-pi.log

crontab -e

\* \* \* \* \* /usr/bin/python3 /home/pi/cash-register-pi/main.py > /var/log/cash-register-pi.log 2>&1

CTRL+X then y to save

# Troubleshooting
Check /var/log/cash-register-pi.log for any errors
