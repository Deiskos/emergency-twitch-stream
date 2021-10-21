import sys
from multiprocessing import Process
import subprocess
import signal
import time

import settings
import secrets

def main():
    ffmpeg_cmd = (
        'ffmpeg',
        # image input
        '-re -framerate 30 -loop 1 -i test_pattern.png',
        # sound generation
        '-re -f lavfi -i sine=frequency=1000:sample_rate=48000 -af volume=-18dB',
        # video processing and codecs
        '-vcodec libx264 -b:v 512k -preset ultrafast -tune stillimage',
        # audio codecs
        '-acodec aac -b:a 128k',
        # output format
        '-f flv -strict -2',
        '{}{}'.format(settings.ingest, secrets.stream_key),
    )

    process = subprocess.Popen(' '.join(ffmpeg_cmd).split(' '))

    def sigint_handler(sig, frame):
        if process is not None:
            process.kill()
        sys.exit(0)
    signal.signal(signal.SIGINT, sigint_handler)

    while not process.poll():
        time.sleep(0.5)

if __name__ == '__main__':
    main()
