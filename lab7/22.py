import pygame
import os

pygame.init()
pygame.mixer.init()

def play_current_song():
    try:
        pygame.mixer.music.load(os.path.join(songs[current]))
        pygame.mixer.music.play()
    except pygame.error as e:
        print("Error", e)

def play_next_song():
    global current
    current = (current + 1) % len(songs)
    play_current_song()


def play_previous_song():
    global current
    current = (current - 1) % len(songs)
    play_current_song()


def stop_music():
    pygame.mixer.music.stop()


width = 400
height = 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2-task")

# List of songs
songs = ['лес.mp3', 'море.mp3', 'ночьюлес.mp3']
current = 0


play_current_song()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:  
                play_next_song()
            elif event.key == pygame.K_LEFT:  
                play_previous_song()
            elif event.key == pygame.K_s: 
                stop_music()

    
    screen.fill((255, 255, 255))
    pygame.display.flip()

# Quit Pygame
pygame.quit()
