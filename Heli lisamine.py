import pygame
import random

# Initsialiseeri pygame
pygame.init()

# Lae taustaheli
pygame.mixer.music.load('Jump.wav')

# Esita taustaheli lõpmatuseni (-1 tähistab lõpmatu mängimist)
pygame.mixer.music.play(-1)

# Muuda taustaheli helitugevust
pygame.mixer.music.set_volume(0.5)

# Esitlusloend
def play_random_sound():
    sounds = ['snd1.mp3', 'snd2.mp3', 'snd3.mp3', 'snd4.mp3', 'snd5.mp3']
    random_sound = pygame.mixer.Sound('music/' + random.choice(sounds))
    random_sound.play()

# Mängitses suvalist heli esitlusloendist
play_random_sound()

# Heli objektiga kokkupuutel (näiteks siis, kui objekt saab pihta)
def play_hit_sound():
    hit_sound = pygame.mixer.Sound('music/Hit.wav')
    hit_sound.play()

# Simuleeri heliobjektiga kokkupuudet
play_hit_sound()

# Pealiskihi uuendamine
pygame.display.update()

# Pealiskihi sulgemine
pygame.quit()
