import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    # Initialize variables
    radius = 15
    mode = 'blue'
    points = []
    erasing = False  # Flag to indicate whether erasing mode is active
    drawing_shape = None  # Variable to store the current drawing shape
    
    while True:
        pressed = pygame.key.get_pressed()
        
        # Check for key combinations
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # Check for quit event or key presses
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_e:
                    erasing = not erasing
                if event.key == pygame.K_d:
                    drawing_shape = 'rectangle'
                if event.key == pygame.K_s:
                    drawing_shape = 'square'
                if event.key == pygame.K_1:
                    drawing_shape = 'right_triangle'
                if event.key == pygame.K_2:
                    drawing_shape = 'equilateral_triangle'
                if event.key == pygame.K_3:
                    drawing_shape = 'rhombus'
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if drawing_shape == 'rectangle' and event.button == 1:
                    start = event.pos
                elif drawing_shape == 'square' and event.button == 1:
                    start = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_shape == 'rectangle' and event.button == 1:
                    end = event.pos
                    pygame.draw.rect(screen, (0, 255, 255), (start, (end[0] - start[0], end[1] - start[1])), 100)
                elif drawing_shape == 'square' and event.button == 1:
                    end = event.pos
                    width = max(abs(start[0] - end[0]), abs(start[1] - end[1]))
                    square_rect = pygame.Rect(start[0], start[1], width, width)
                    pygame.draw.rect(screen, (0, 255, 255), square_rect, 100)
                elif drawing_shape == 'right_triangle' and event.button == 1:
                    end = event.pos
                    pygame.draw.polygon(screen, (255, 255, 0), [start, (start[0], end[1]), end], 100)
                elif drawing_shape == 'equilateral_triangle' and event.button == 1:
                    end = event.pos
                    height = math.sqrt(3) / 2 * abs(start[0] - end[0])
                    pygame.draw.polygon(screen, (255, 255, 0), [start, (end[0], start[1]), ((start[0] + end[0]) // 2, int(start[1] + height))], 100)
                elif drawing_shape == 'rhombus' and event.button == 1:
                    end = event.pos
                    center_x = (start[0] + end[0]) // 2
                    center_y = (start[1] + end[1]) // 2
                    width = abs(start[0] - end[0])
                    height = abs(start[1] - end[1])
                    pygame.draw.polygon(screen, (255, 255, 0), [(center_x, start[1]), (end[0], center_y), (center_x, end[1]), (start[0], center_y)], 100)
                    
                drawing_shape = None
                
                # Toggle erasing mode when left-clicking or right-clicking
                if event.button == 1: # left click grows radius
                    if not erasing:
                        radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    if not erasing:
                        radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if erasing:
                    position = event.pos
                    points = [p for p in points if pygame.math.Vector2(p).distance_to(pygame.math.Vector2(position)) > radius]
                else:
                    # if mouse moved, add point to list
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # Draw all points
        i = 0
        while i < len(points) - 1:
            if not drawing_shape:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            else:
                drawShape(screen, points[i], points[i + 1], radius, mode, drawing_shape)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

# Function to draw a line between two points
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Function to draw a shape between two points
def drawShape(screen, start, end, width, color_mode, shape):
    c1 = 128
    c2 = 128
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    if shape == 'rectangle':
        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            pygame.draw.rect(screen, (0, 255, 0), (x - width // 2, y - width // 2, width, width), 10)
    elif shape == 'square':
        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            width = max(abs(start[0] - end[0]), abs(start[1] - end[1]))
            square_rect = pygame.Rect(x - width // 2, y - width // 2, width, width)
            pygame.draw.rect(screen, (0, 0, 255), (x - width // 2, y - width // 2, width, width), 10)
    elif shape == 'right_triangle':
        pygame.draw.polygon(screen, (255, 255, 0), [start, (start[0], end[1]), end], 10)
    elif shape == 'equilateral_triangle':
        height = math.sqrt(3) / 2 * abs(start[0] - end[0])
        pygame.draw.polygon(screen, (255, 255, 0), [start, (end[0], start[1]), ((start[0] + end[0]) // 2, int(start[1] + height))], 10)
    elif shape == 'rhombus':
        center_x = (start[0] + end[0]) // 2
        center_y = (start[1] + end[1]) // 2
        width = abs(start[0] - end[0])
        height = abs(start[1] - end[1])
        pygame.draw.polygon(screen, (255, 255, 0), [(center_x, start[1]), (end[0], center_y), (center_x, end[1]), (start[0], center_y)], 10)

main()
