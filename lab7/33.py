import pygame
import sys


pygame.init()


WIDTH = 400
HEIGHT = 400

WHITE = (255, 255, 255)
RED = (255, 0, 0)


radius = 25
diameter = 50


x = (WIDTH - diameter) // 2
y = (HEIGHT - diameter) // 2


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3-task")
clock = pygame.time.Clock()


while True:
    screen.fill(WHITE)  

    
    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if y - 20  > 0:
                    y -= 20
            elif event.key == pygame.K_DOWN:
                if y + radius + 20 <= HEIGHT:
                    y += 20
            elif event.key == pygame.K_LEFT:
                if x - 20 >= 0:
                    x -= 20
            elif event.key == pygame.K_RIGHT:
                if x + radius + 20 <= WIDTH:
                    x += 20

    
    clock.tick(30)
