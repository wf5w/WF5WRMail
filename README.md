# WF5WRMail
Remote Email system, using Pat Winlink under the hood

# Introduction

The RMail system uses pat winlink under the hood, and facilitates, the rapid, and easy way to collect email from anyone, on their own cellphone, tablet, or computer. The procedure for doing so, will be outlined below.

When the user connects to the hotspot and uses a web browser to bring up the RMail server, to enter an email, it is important to note that the email is not sent, it is merely posted. As a ham, you will take it home, where your radio resides, and using pat winlink, send those messages that are in the outbox.

A good ham,  will look at the emails that were posted, to see if there is any illegal messages, before doing the connection to the winlink gateway (by however means).

There are 3 servers:

**RMail server**  - 10.42.0.1:4000 
**Pat Winlink** - 10.42.0.1:5000 
**Webadmin server** - 10.42.0.1:10000 

# Installation

1. Get the starter Raspberry Pi image from:
   
https://drive.google.com/file/d/1lMiqr6Bcwfou84TJyA0beRXUlve0M6bW/view?usp=sharing

2. unzip the file, and note the name of the image
3. burn the image to a micro-SD card or a USB Disk, or a USB Stick

for linux: for example:
$ umount /dev/xxx1
$ umount /dev/xxx2
$ sudo dd bs=16M status=progress if=WF5WRmail-x.x.x.img of=/dev/xxx

4. eject /dev/xxx
5. connect the new disk to the raspberry pi
6.  the pi will bootup, and run the extend file system routine, then reboot
7. when the pi is up for good, connect to it by using the Rmail wifi SSID (this will change after the Setup script runs)
8. now you are connected to the RMail SSID, you can get to the pi at 10.42.0.1
9. bring up the webadmin, and do the Set Date and Time, then the Setup first time
10. After the setup, your wifi SSID will be    ```RMail-<callsign>```
11. You can then use the RMail email (10.42.0.1:4000)

# First Steps

## webadmin

Before you can use the RMail system, as a Ham you need to set your parameters for pat winlink.

You can use the webadmin server to easily do it for you. 

The first time you do the setup, you need to set the Date and Time. This is because the Raspberry Pi does not have a way to keep up with time when it is not in use. Then click on the Setup first time.

You only need to click on the Setup first time, one time. Once those parameters are set, then RMail is ready to go.

# RMail

The RMail server is a web based,  mailer, that users can enter there own email, and 
click the submit button, which posts the message the the pat winlink's outbox, for processing later on.

Once the RMail server is up, it will be up for anyone to use.

All the user needs to do, is connect the RMail SSID, and use a web browser to point to the RMail server, at 10.42.0.1:4000 and they can enter an email.

# notes

The Raspberry Pi comes up as a hotspot. This system is designed to collect emails from any user who connects to the hotspot.

raspberry pi auto hotspot SSID: begins with RMail

raspberry pi hotspot network adddress: 10.42.0.1

ssh is enabled, and the user and password are pre defined below: 

**It is highly recommended, that you ssh into the pi, and then change the passwd before taking this out to the field**

raspberry pi user: pi

pi password: 123

when you take this to the field, you may not want to have the webadmin and pat winlink up for anyone to connect into so if the file named mailonly is found in the home directory, then the webadmin and pat winlink servers will not be started. You do this by logging into the pi with ssh, and  

***$ touch mailonly***
  
or conversely, if you want the servers to come up, then remove the mailonly file

***$ rm -f mailonly***  
***$ sudo reboot***

If you would like to change the header image on the RMail page:
1. Create a png image of your own.
2. in the /home/pi/bin/http/ directory, replace header.png with your own png file. Make sure the resulting file is named header.png

Please note, that the pat winlink config file, is not the stock config file, it has been changed to best run on the RMail system. One notable change is that the ARDOP port has been changed to port 8200 instead of 8515.

When using the pat winlink server, that one way to connect is telnet. Telnet is not available, unless you have internet. I have found that the easiest way to get ethernet is to connect an ethernet cable into a router, and internet becomes available.
