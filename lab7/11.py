import pygame
import sys
import math
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 800, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1-task")

background = pygame.image.load("C:/Users/turs/Desktop/dzz/pp/lab7/main-clock.png - Copy.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
clock_rect = background.get_rect()
right_hand = pygame.image.load("rightarm.png")
left_hand = pygame.image.load("leftarm.png")


def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    return rotated_image

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    current_time = datetime.now()
    minutes = current_time.minute
    seconds = current_time.second

    
    screen.fill((255, 255, 255))

    
    screen.blit(background, clock_rect)

    
    minutes_angle = -6 * minutes
    seconds_angle = -6 * seconds

    rotate_right = rotate_image(left_hand, minutes_angle)
    rotate_left = rotate_image(left_hand, seconds_angle)

    screen.blit(rotate_right, (WIDTH // 2 - rotate_right.get_width() // 2, HEIGHT // 2 - rotate_right.get_height() // 2))
    screen.blit(rotate_left, (WIDTH // 2 - rotate_left.get_width() // 2, HEIGHT // 2 - rotate_left.get_height() // 2))

    
    pygame.display.flip()

    
    clock.tick(60)

