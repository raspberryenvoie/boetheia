#!/bin/sh
# Exit if user isn't root
[ "$(id -u)" -ne 0 ] && {
    echo 'Please run as root'
    exit 1
}
# Install mpg123 and git
apt-get install mpg123 git -y

# Clone boetheia
cd /home/pi/
git clone https://github.com/raspberryenvoie/boetheia
cd boetheia/

# Install python requirements
pip install -r requirements.txt
chmod +x boetheia.py

# Enable boetheia at startup
mv boetheia.service /etc/systemd/system/
chmod 644 /etc/systemd/system/boetheia.service
systemctl daemon-reload
systemctl enable boetheia.service
echo 'Done. Please reboot the device!'
