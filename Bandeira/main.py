import pygame
import sys
import math

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bandeira do Brasil")

GREEN = (0, 156, 59)
YELLOW = (255, 223, 0)
BLUE = (0, 39, 118)
WHITE = (255, 255, 255)

screen.fill(WHITE)

pygame.draw.rect(screen, GREEN, pygame.Rect(0, 0, width, height))

pygame.draw.polygon(screen, YELLOW, [(width // 2, 0), (width, height // 2), (width // 2, height), (0, height // 2)])

circle_center = (width // 2, height // 2)
circle_radius = height // 5
pygame.draw.circle(screen, BLUE, circle_center, circle_radius)

star_points = []
for i in range(5):
    angle = math.radians(90 + i * 72)
    x = circle_center[0] + int(circle_radius * math.cos(angle))
    y = circle_center[1] - int(circle_radius * math.sin(angle))  
    star_points.append((x, y))
pygame.draw.polygon(screen, YELLOW, star_points)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
pygame.quit()
sys.exit()
