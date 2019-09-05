import pygame
import time

test =[
    'hai', 'muoi2', 'lam', 'trieu', 'ba', 'tram', 'nghin'
]

base_dir = './sounds/'

pygame.init()

pygame.mixer.music.load('./sounds/test.mp3')
pygame.mixer.music.play()
time.sleep(10)

# sound = pygame.mixer.Sound('./sounds/mot1.ogg')
# sound.play()
# pygame.time.delay(500)
