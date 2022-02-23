# importing vlc module
import vlc

# importing time module
import time


# creating vlc media player object
media_player = vlc.MediaPlayer("file:///home/fabriciofr/Music/claraavd/python-ex/exercicios/ex021.mp3")


# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(10)

# getting media
value = media_player.get_media()

# printing media
print("Media : ")
print(value)