A script that uses ffmpeg to stream to Twitch.

## Setup Guide
### Requirements
* ffmpeg
* python2.7

### Setup
3. Edit `settings.py`
4. Edit `secrets.py`
5. Provide your own prerecorded file or run `pipenv run python ffmpeg_stream.py --generate`

## Usage
0. Ensure the stream from your PC is down one way or another, Twitch has to show NotLikeThis screen.
1. `python ffmpeg_stream.py`
2. When ready to resume - Ctrl-C to terminate
3. Wait until NotLikeThis on Twitch
4. Start streaming in XSplit

