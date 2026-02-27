# WF5WRMail
WF5W Remote Email system, using Pat Winlink under the hood

After installation, just just put the SD Card into your Raspberry Pi, and turn it on.

The Rmail system will come up with its own hotspot. The SSID is initially named "Rmail". You just connect your wifi to "Rmail" and connect your web browser to http://10.42.0.1

You will after 5 seconds be connected to the RMail server.

# Introduction

The RMail system uses pat winlink under the hood, and facilitates, the rapid, and easy way to collect email from anyone, on their own cellphone, tablet, or computer. The procedure for doing so, will be outlined below.

When the user connects to the hotspot and uses a web browser to bring up the RMail server, to enter an email, it is important to note that the email is not sent, it is merely posted. As a ham, you will take it home, where your radio resides, and using pat winlink, send those messages that are in the outbox.

A good ham,  will look at the emails that were posted, to see if there is any illegal messages, before doing the connection to the winlink gateway (by however means).

There are 4 servers:

- **Rmail Landing Page** - 10.42.0.1
- **RMail server**  - 10.42.0.1:4000 
- **Pat Winlink** - 10.42.0.1:5000 
- **Webadmin server** - 10.42.0.1:10000 

# Installation

1. Get the starter Raspberry Pi image

https://drive.google.com/file/d/1lT99nzWAs0ks1fVIlR1-JqmDtLkMpktZ/view?usp=sharing

currently Rmail is at Version 2.5.3P1

2. unzip the file, and note the name of the image
3. burn the image to a micro-SD card or a USB Disk, or a USB Stick

4. ### Burning
#### linux: for example:

if your SD-Card (or USB stick) is /dev/xxx1 and /dev/xxx2

```$ umount /dev/xxx1
$ umount /dev/xxx2
$ sudo dd bs=16M status=progress if=WF5WRmail-x.x.x.img of=/dev/xxx

eject /dev/xxx
```

#### Windows:

Download Etcher, or some other SD Card image burning tool
and use it to burn the image to the SD-Card

#### Mac:

Download Etcher, and use it to burn the SD Card

## Now complete the steps below:

5. connect the new disk to the raspberry pi
6. the pi will bootup, and run the extend file system routine, then reboot
7. when the pi is up for good, connect to it by using the Rmail wifi SSID (this will change after the Setup script runs)
8. now you are connected to the RMail SSID, you can get to the pi at 10.42.0.1
9. bring up the webadmin ( http://10.42.0.1:10000 ), and do the Set Date and Time
10. then do the Setup first time
11. After the setup, your wifi SSID will be    ```RMail-<callsign>```
12. You can then use the RMail email ( http://10.42.0.1:4000 )

See the details below:

# First Steps

## webadmin

Before you can use the RMail system, as a Ham you need to set your parameters for pat winlink.

You can use the webadmin server to easily do it for you. 

The first time you do the setup, you need to set the Date and Time. This is because the Raspberry Pi does not have a way to keep up with time when it is not in use, and it won't be connected to the internet to get the time. Then click on the Setup first time.

You only need to click on the Setup first time, one time. Once those parameters are set, then RMail is ready to go.

# RMail

The RMail server is a web based,  mailer, that users can enter there own email, and 
click the submit button, which posts the message the the pat winlink's outbox, for processing later on.

Once the RMail server is up, it will be up for anyone to use.

All the user needs to do, is connect the RMail SSID, and use a web browser to point to the RMail server, at 10.42.0.1:4000 and they can enter an email. There is a document named WF5WRMail_Public_Instructions.odt which should help.

If you want, you can also bring an hdmi monitor and keyboard, and connect to the RMail web page that way.

# Notes

### Enable password-less ssh

On you local system:
```
$ ssh-keygen -t rsa
#    IMPORTANT: just press the enter key for all the prompts!!

$ cd ~/.ssh
$ ssh-copy-id -i id_rsa.pub pi@10.42.0.1
# (enter the raspberry pi password)
```

### Other

The Raspberry Pi comes up as a hotspot. This system is designed to collect emails from any user who connects to the hotspot.

raspberry pi auto hotspot SSID: begins with RMail

raspberry pi hotspot network adddress: 10.42.0.1

ssh is enabled, and the user and password are pre defined below: 

- raspberry pi user: pi
- pi password: rpi


**It is highly recommended, that you ssh into the pi, and then change the passwd before taking this out to the field**

**Version 2.4.1: There is now a link to set the account password on the webadmin server**

**after you have done the Webadmin Server steps ( Set Date Time, and Setup First Time ), you may want to disable the Webadmin server and pat winlink server, after a reboot, when you take this to the field.**

This is done by the prescence of a file in the home directory, named **mailonly**

if the file named mailonly is found in the home directory, then the webadmin and pat winlink servers will not be started. You do this by logging into the pi with ssh, and  create the file.
  
or conversely, if you want the servers to come up, then remove the mailonly file

```
ssh pi@10.42.0.1
pi> cd
pi> touch mailonly      # or rm mailonly
pi> sudo reboot
```


If you would like to change the header image on the RMail page:
1. Create a png image of your own.
2. in the /home/pi/bin/http/ directory, replace header.png with your own png file.

Make sure the resulting file is named header.png

If you would like to change the text that is appended to each and every message in the RMail server, you can edit the /home/pi/bin/http/postmessage.txt file to suit your needs.

Please note, that the pat winlink config file, is not the stock config file, it has been changed to best run on the RMail system. One notable change is that the ARDOP port has been changed to port 8200 instead of 8515.

When using the pat winlink server, that one way to connect is telnet. Telnet is not available, unless you have internet. I have found that the easiest way to get ethernet is to connect an ethernet cable into a router, and internet becomes available.

### Example procedure to copy your pi's posted email to your own pat winlink system
```
# how to copy all the outbox files to your local machine from the pi
# my callsign is WF5W on both your raspberry pi, and the local system, your
# callsign will be different, and your local home directory will be different.
# These commands are for example only. Please subsitute your directories accordingly. 

local> ssh pi@10.42.0.1

pi> pat env | grep -e 'MAILBOX_PATH|MYCALL'
PAT_MYCALL="WF5W"
PAT_MAILBOX_PATH="/home/pi/.local/share/pat/mailbox"

pi> cd ~/.local/share/pat/mailbox/WF5W/out

pi> zip ~/currentpatoutbox.zip *.b2f
pi> exit


# back at your system: copy the zip file you created

local> scp pi@10.42.0.1:currentpatoutbox.zip .

# now unzip the b2f files in your local machine's pat winlink outbox

local> pat env | grep -e 'MAILBOX_PATH|MYCALL'
PAT_MYCALL="WF5W"
PAT_MAILBOX_PATH="/home/wf5w/.local/share/pat/mailbox"

local> cd ~/.local/share/pat/mailbox/WF5W/out
unzip ~/currentpatoutbox.zip 

# you have now added all the files to your outbox, use pat winlink to send them
```
i

## Copy mail from the raspberry pi to your local host

Although you can use the raspberry pi to actually send the mail you collected, there is an option to copy the files over to your local system, to send them via the pat winlink system there.

Look in the github repository for the files transferOutbox and transferOutbox.py. These will facilitate that.

To use the transferOutbox programs:

$ transferOutbox.py remote-ip-address remote-user remote-callsign local-callsign 

for instance: transferOutbox.py 10.42.0.1 pi WF5W WF5W-15

(pat winlink is setup with a different mailbox on the local machine as opposed to the pi)
