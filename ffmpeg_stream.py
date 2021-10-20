import sys
from multiprocessing import Process
import subprocess
import signal
import time

import settings
import secrets

process = None
slider_position = 1

def sigint_handler(sig, frame):
    if process is not None:
        process.kill()
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def main():
    ffmpeg_cmd = (
        'ffmpeg',
        # image input
        '-framerate 15 -re -loop 1 -i test_pattern.png -re',
        # sound generation
        '-f lavfi -i sine=frequency=1000',
        # video processing and codecs
        '-vf scale=1920:1080:flags=lanczos,setsar=1:1 -vcodec libx264 -preset ultrafast -tune stillimage',
        # audio codecs
        '-b:v 128k -acodec aac -b:a 64k',
        # output format
        '-f flv -strict -2',
        f'{settings.ingest}{secrets.stream_key}',
    )

    process = Process(
        target=subprocess.run,
        args=(' '.join(ffmpeg_cmd).split(' '), ),
        # kwargs={'stdout': subprocess.DEVNULL, 'stderr': subprocess.DEVNULL}
    )
    process.start()

    while process.is_alive():
        time.sleep(0.5)

if __name__ == '__main__':
    main()
