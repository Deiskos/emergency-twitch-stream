import subprocess
import itertools
from secrets import *


ffmpeg_cmd = [
    'ffmpeg',

    '-framerate', '15',
    '-re', # Read input at native frame rate.
    '-loop', '1',
    '-i', 'test_pattern.png', # TV test pattern

    '-re',
    '-f', 'lavfi', # filter input
    '-i', 'sine=frequency=1000', # 1kHz sound

    # codecs and bitrate
    '-vf', 'scale=1920:1080:flags=lanczos,setsar=1:1',
    '-vcodec', 'libx264', '-preset', 'ultrafast', '-x264opts', 'keyint=30:scenecut=0', '-tune', 'stillimage', '-b:v', '128k',
    '-g', '60',

    '-acodec', 'aac', '-b:a', '64k',

    '-f', 'flv', # output in flv format
    '-threads', '0',
    '-strict', '-2', # for some reason aac codec wasn't working for me without this
    '-rtmp_buffer', '0',
    'INGEST'
]
print(' '.join(ffmpeg_cmd))
# subprocess.run(ffmpeg_cmd)
