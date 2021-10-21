from typing import Tuple, List
import settings
import secrets

def make_args(cmd):
    # type: (Tuple[str, ...]) -> List[str]
    return ' '.join(cmd).split(' ')

# since this is a fallback, everything is scaled down to shit
stream_fallback_cmd = (
    'ffmpeg',
    # image input
    '-re -framerate 15 -loop 1 -i {}'.format(settings.fallback_image),
    # sound generation
    '-re -f lavfi -i sine=frequency=1000:sample_rate=48000 -af volume=-18dB',
    # video processing and codecs
    '-vcodec libx264 -b:v 512k -preset ultrafast -tune stillimage',
    '-maxrate 1024k -bufsize 4096k',
    # audio codecs
    '-ar 48000 -acodec aac -b:a 128k',
    # output format
    '-f flv -strict -2',
    '{}{}'.format(settings.ingest, secrets.stream_key),
)
stream_fallback_args = make_args(stream_fallback_cmd)

stream_blank_cmd = (
    'ffmpeg',
    # blank image straight from /dev/zero
    '-re -s 480x270 -f rawvideo -pix_fmt rgb24 -r 60 -i /dev/zero',
    # blank audio
    '-re -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=48000',
    # video processing and codecs
    '-vcodec libx264 -b:v 512k -preset ultrafast -tune stillimage',
    '-maxrate 1024k -bufsize 4096k',
    # audio codecs
    '-ar 48000 -acodec aac -b:a 128k',
    # output format
    '-f flv',
    '{}{}'.format(settings.ingest, secrets.stream_key),
)
stream_blank_args = make_args(stream_blank_cmd)

record_cmd = (
    'ffmpeg',
    # image input
    '-framerate 60 -loop 1 -i {}'.format(settings.record_image_source),
    # sound generation
    '-i {}'.format(settings.record_audio_source),
    # video processing and codecs
    '-vf scale=1920:1080:flags=lanczos,setsar=1:1',
    '-vcodec libx264 -b:v 2048k -preset ultrafast -tune stillimage',
    # audio codecs
    '-ar 48000 -acodec aac -b:a 192k',
    # output format
    '-f flv -r 60 -strict -2',
    # stop when shortest input stream ends
    # in this configuration this will be audio track
    '-shortest',
    '{}'.format(settings.prerecorded_file),
)
record_args = make_args(record_cmd)

stream_prerecorded_cmd = (
    'ffmpeg',
    # image input
    '-re -stream_loop -1 -i {}'.format(settings.prerecorded_file),
    '-vcodec copy -maxrate 4096k -bufsize 16384k',
    '-acodec copy',
    '-r 60 -f flv',
    '{}{}'.format(settings.ingest, secrets.stream_key),
)
stream_prerecorded_args = make_args(stream_prerecorded_cmd)