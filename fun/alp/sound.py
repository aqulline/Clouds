from pygame import mixer


mixer.init(44100, -16, 2, 512, None, 5)
mixer.music.load("/home/alpha/Music/Elton John - Sacrifice (Lyrics) &#x1F3B5;.mp3", "")
mixer.music.play()



