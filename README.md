<h1 align="center">Boetheia</h1>
<h3 align="center">Calling system running on a Raspberry Pi for disabled people unable to speak and only able to move their head.</h3>

---------

<p align="center">Want to see pictures of my installation of boetheia? Click <a href="https://gist.githubusercontent.com/raspberryenvoie/a26dac779fb531d5d1778ba412e44f94/raw/f56f65f10849b30debbe52746e3644caeb7d4073/boetheia%2520outside.jpg">here</a> and <a href="https://gist.githubusercontent.com/raspberryenvoie/a26dac779fb531d5d1778ba412e44f94/raw/f56f65f10849b30debbe52746e3644caeb7d4073/boetheia%2520inside.jpg">here</a>.
</p>

# How does it work?
1. A laser is fixed to the disabled person's head.
2. When the Raspberry Pi boots, boetheia launches automatically.
3. Optional: If boetheia is running succesfully, an LED gets turned on.
4. If the disabled person points the laser to the LRD module, a sound is played, else nothing happens.

# Parts list
- a Raspberry Pi (any model) with an SD or MicroSD card depending on the model
- Speakers
- a Light Dependent Resistor (LDR) sensor module
- At least 3 female to female jumper wires
- a laser fixed to the person's head. It can be attached using wiring ties to glasses or a hair clip.
- Optional: an LED

## How to build the laser
1. Get a USB cable and a laser diode such as [these](https://www.amazon.com/HiLetgo-10pcs-650nm-Diode-Laser/dp/B071FT9HSV).
2. Cut the the tip that is supposed to be connected to a phone.
3. Strip the red and black or blue wires.
4. Weld the laser module to the bare wires.
5. Protect the wires you have just welded using a heat-shrink tubing.
6. The laser you built can now be connected to a power bank or a USB wall charger.

# Build instructions

## Connecting everything
1. Make sure you have every item written in the [parts list](https://github.com/raspberryenvoie/boetheia#parts-list) section.
2. Connect the speakers to the Raspberry Pi.
3. Connect the LDR module to the Raspberry Pi: \
See [pinout.xyz](https://pinout.xyz/). \
The VCC pin is to be connected to any 5v power pin of the Raspberry Pi. \
The GND pin is to be connected to any Ground pin. \
The DO pin is to be connected to GPIO 4. \
If you've got an AO pin don't connect it to the Raspberry Pi.
4. Ajust the sensitivity of the LDR module by turning the onboard potentiometer with a screwdriver. The DO-LED on the module should only turn on when the laser is pointed to the LDR sensor module.
5. Optional: you can decide to use an LED. It shows whether boetheia is running. Moreoever, if you put the LED next to the LDR sensor module, it can help the disabled person point the LDR sensor module in the dark. \
Connect the negative end to any ground pin of the Raspberry Pi.\
Connect the positive end to GPIO 17.
6. Now head to the [installation section](https://github.com/raspberryenvoie/boetheia#installation) !

<img width=400 alt="Diagram" src="https://gist.github.com/raspberryenvoie/a26dac779fb531d5d1778ba412e44f94/raw/5ce822a2f9c212888e9aa846394f64fcc4a713fc/boetheia%2520diagram.jpg"> \
Connection Diagram

## Installation
1. Set up Raspberry Pi OS : follow the instructions in the [install and set up Raspberry Pi OS section](https://github.com/raspberryenvoie/piRa1n/wiki/Install-piRa1n-on-a-Raspberry-Pi-4#1-install-and-set-up-raspberry-pi-os)
2. Copy and paste the following command and press the enter key.
```
curl -s https://raw.githubusercontent.com/raspberryenvoie/boetheia/main/install.sh | sudo sh
```
4. If you don't want to use an LED refer to the [settings section](https://github.com/raspberryenvoie/boetheia#parts-list)
3. Type ` sudo reboot now` followed by the enter key to reboot the Raspberry Pi.
4. If you've set up the LED it should turn on. \
Boetheia is ready to be used! If the programme doesn't work, type `sudo systemctl status boetheia` to see the logs.

# Settings
Refer to this section if you need to change some parameters of the programme. \
Type `nano /home/pi/boetheia/boetheia.py` to edit the file. \
The following settings are in the settings part of the code which begins with `# Settings`.

| Options               | Description                                               | Values
|-----------------------|-----------------------------------------------------------|------------------------------------------------
| `self.isLed`          | Whether to use an LED                                     | `True` or `False`
| `self.ledPin`         | GPIO pin of the LED                                       | Integer (see [pinout.xyz](https://pinout.xyz/))
| `self.ldrPin`         | GPIO pin of the LDR sensor module                         | Integer (see [pinout.xyz](https://pinout.xyz/))
| `self.delay`          | Waiting time (in seconds) between each sensor status check| Integer or float

## Changing the default sound
To change the default sound, replace the `sound.mp3` file in `/home/pi/boetheia` with a mp3 file of the same name.
