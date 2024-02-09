import subprocess
import ffmpeg

FROM = "00:46:28"
TO = "01:23:08"
TARGET = "demo.mp4"
url_to_download = 'https://www.youtube.com/watch?v=mU-x2Kv2haA'

# Download audio
subprocess.run([
    'yt-dlp', '-x', '--audio-format', 'mp3',
    'https://www.youtube.com/watch?v=mU-x2Kv2haA', '-o', 'demo.%(ext)s'
])

# Trim the audio
subprocess.run([
    'ffmpeg', '-ss', '00:46:28', '-to', '01:23:08', '-i', 'demo.mp3',
    '-acodec', 'copy', 'demo_trimmed.mp3'
])
