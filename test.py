import pygame
import time

test =[
    'hai', 'muoi2', 'lam', 'trieu', 'ba', 'tram', 'nghin'
]

base_dir = './sounds/'

pygame.init()

for t in test:
    sound_dir = base_dir + t + '.ogg'
    print(sound_dir)
    play_sound(sound_dir)
    time.sleep(0.8)

# sound = pygame.mixer.Sound('./sounds/mot1.ogg')
# sound.play()
# pygame.time.delay(500)
