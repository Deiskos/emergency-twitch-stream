from __future__ import print_function

import sys
import os
import argparse
import subprocess
import signal

import settings
from ffmpeg_commands import stream_fallback_args, stream_blank_args, \
    stream_prerecorded_args, record_args

parser = argparse.ArgumentParser(description='Emergency Twitch Broadcast script')
parser.add_argument(
    '--generate', '-g',
    dest='generate',
    action='store_true',
    help='Generate video file'
)
parser.add_argument(
    '--fallback', '-f',
    dest='fallback',
    action='store_true',
    help='Use fallback streaming method'
)
args = parser.parse_args()


def run_ffmpeg(ffmpeg_args):
    # type: (List[str]) -> None
    process = subprocess.Popen(ffmpeg_args)

    def sigint_handler(sig, frame):
        if process is not None:
            process.kill()
        sys.exit(0)
    signal.signal(signal.SIGINT, sigint_handler)

    process.wait()


# fallbacks to ensure streaming
def fallback():
    if os.path.isfile(settings.fallback_image):
        print('Starting fallback with image and 1kHz tone')
        run_ffmpeg(stream_fallback_args)
    else:
        print('Starting blank fallback')
        run_ffmpeg(stream_blank_args)


def main():
    if args.fallback:
        fallback()
    elif args.generate:
        if os.path.isfile(settings.prerecorded_file):
            os.rename(settings.prerecorded_file, '{}.old'.format(settings.prerecorded_file))
        run_ffmpeg(record_args)
    elif not os.path.isfile(settings.prerecorded_file):
        print('No prerecorded file found, starting fallback', file=sys.stderr)
        fallback()
    else:
        print('Starting prerecorded stream')
        run_ffmpeg(stream_prerecorded_args)

    return 0


if __name__ == '__main__':
    main()

