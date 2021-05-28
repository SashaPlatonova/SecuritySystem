# SecuritySystem with Telegram Bot
## Components:
Raspberry pi 4, Intel Neuro Stick, USB camera, SD card + micro sd, HDMI

Link to install and configure **Open CV:** https://software.intel.com/content/www/us/en/develop/..

## To get started, run:
_**facial_req.py (for face recognition)**_ and _**a.out (for TG bot)**_

### Adding new people
1. Create a new folder in the dataset, call it your name
2. Run the file headshots.py, press the spacebar to take a photo (it is better to take at least 10 photos)
3. Run the file train_model.py. This file trains the neural network
4. Everything is ready for testing

In the process, the program saves the last face that it recognized in the file _image.jpg_. It saves the last recognized name to the file _name.txt_.

### Working with a bot
_**You can find the bot at @pisecsys_bot**_
The config.py file contains the basic settings: token and user id. Add your id there.
The bot will write to you when it starts.
There are two modes of operation: _**"Update", "Security"**_
1. "Update" mode sends you the last recognized face after pressing
2. The "Security" mode works without your participation until it is disabled. When a person is detected, a message is sent to you