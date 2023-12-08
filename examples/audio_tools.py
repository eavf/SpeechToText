import ffmpeg

FROM = "00:46:28"
TO = "01:23:08"
TARGET = "demo.mp4"
url_to_download = 'https://www.youtube.com/watch?v=mU-x2Kv2haA'


# ffmpeg.input(url_to_download, ss=FROM, t=TO).output("demo.mp3", vcodec="copy", acodec="copy").overwrite_output().run()
ffmpeg.input(url_to_download, ss=FROM, t=TO).output("demo.mp3", vcodec="copy", acodec="copy").overwrite_output().run()

