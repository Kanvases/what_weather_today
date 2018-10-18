import pygame 
import os
import time
def AudioPlay(path):
    pygame.mixer.init()
    track = pygame.mixer.music.load(path)
    pygame.mixer.music.play()
def main():
    AudioPlay(os.getcwd()+'/res.mp3')
    time.sleep(5)
    pygame.mixer.music.stop()

if __name__ == '__main__':
    main()