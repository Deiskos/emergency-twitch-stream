A script that uses ffmpeg to stream TV test pattern and 1 kHz tone to Twitch.

## Setup Guide
### Requirements
* ffmpeg
* python3.7+

### Setup
0. `sudo add-apt-repository ppa:deadsnakes/ppa`
0. `sudo apt update`
0. `sudo apt install ffmpeg libx264 python3.8`
1. Edit `settings.py`: go to [https://stream.twitch.tv/ingests/](Recommended Ingest Endpoints For You), copy #1 and replace `INGEST_HERE` with it.
2. Edit `secrets.py` to include your stream key.

## Usage
0. Ensure the stream from your PC is down one way or another, Twitch has to show NotLikeThis screen.
1. `python3.8 ffmpeg_stream.py`
2. When ready to resume - Ctrl-C to terminate
3. Wait until NotLikeThis on Twitch
4. Start streaming in XSplit

