# Security system with Telegram Bot

## What is it?
With this code you can create a home security system to detect strangers. The program reads a video stream from your USB camera and in the "Security" mode, when a person is detected, a message is sent with a photo and the name of this person, if it is recorded in your database.

## Components:
Raspberry Pi 4, Intel Neuro Stick, USB camera, SD card + micro sd, HDMI.

### First steps:
Firstly you should install _Raspberry Pi OS_ with desktop and recommended software by using SD card and _balenaEther_ - application for burning ISO, ZIP and other images to removable media, including SD cards. Then install _Open CV, face-recognition and imutils_. Links:
1. _RPi OS_: https://www.raspberrypi.org/software/operating-systems/
2. _Open CV_: https://software.intel.com/content/www/us/en/develop/..
3. _face-recognition_: https://pypi.org/project/face-recognition/
4. _imutils_: https://pypi.org/project/imutils/

### Adding new people
1. Create a new folder in the dataset, call it your name.
2. Run the file _headshots.py_, press the spacebar to take a photo (it is better to take at least 10 photos).
3. Run the file _train_model.py_. This file trains the neural network.
4. Create a mapping between names and faces in the _encodings.pickle_ file.
5. Everything is ready for testing.

In the process, the program saves the last face that it recognized in the file _image.jpg_. It saves the last recognized name to the file _name.txt_.

### Working with a bot
_**You should create a new TG-bot with @BotFather.**_
The _config.py_ file contains the basic settings: token and user id. Add your id and bot token there.
The bot will write to you when it starts.
There are two modes of operation: _**"Update", "Security"**_
1. "Update" mode sends you the last recognized face after pressing.
2. The "Security" mode works without your participation until it is disabled. When a person is detected, a message is sent to you.

## To get started, run:
_**facial_req.py (for face recognition)**_ and _**a.out (for TG bot)**_
