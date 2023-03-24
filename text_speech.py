from pygame import mixer 
from gtts import gTTS

def main():
    tts = gTTS('Like ...')
    tts.save('output.mp3')
    mixer.init()
    mixer.music.load('music.mp3')
    mixer.music.play()


class TestMath:
    def __init__(self):
        self.x  = 10
        self.y  = 10