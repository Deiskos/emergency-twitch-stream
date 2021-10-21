A script that uses ffmpeg to stream TV test pattern and 1 kHz tone to Twitch.

## Setup Guide
### Requirements
* ffmpeg
* python3.7+

### Setup
0. `sudo apt install python-pip`
1. `sudo -H pip install pipenv`
2. `pipenv update`
3. Edit `settings.py`
4. Edit `secrets.py`
5. `pipenv run python ffmpeg_stream.py --generate`

## Usage
0. Ensure the stream from your PC is down one way or another, Twitch has to show NotLikeThis screen.
1. `pipenv run python ffmpeg_stream.py`
2. When ready to resume - Ctrl-C to terminate
3. Wait until NotLikeThis on Twitch
4. Start streaming in XSplit

