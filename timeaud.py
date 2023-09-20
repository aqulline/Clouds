from pygame import mixer
import os

mixer.init()

time = 0


c = mixer.Sound
x = c.get_length(c("/home/alpha/Music/b/bazzi_beautiful_feat._camila_official_audio_mp3_81491.mp3"))
print(x)

def times(musc):
    if musc:
        for i in musc:
            u = i[0]
            c = mixer.Sound
            x = c.get_length(c(f"/home/alpha/Music/{u}/{i}"))
            print(x)

time += ((1 * x)/60)
x = os.listdir("/home/alpha/Music/")
for i in x:
    try:
        z = os.listdir(f"/home/alpha/Music/{i}")
        print(z)
        times(z)
    except NotADirectoryError:
        print("Not")



