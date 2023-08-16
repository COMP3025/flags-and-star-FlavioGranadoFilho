import pygame
import sys
import math

# Inicialização do Pygame
pygame.init()

# Dimensões da janela
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bandeira do Brasil")

# Cores
GREEN = (0, 156, 59)
YELLOW = (255, 223, 0)
BLUE = (0, 39, 118)
WHITE = (255, 255, 255)

# Limpa a tela com a cor branca
screen.fill(WHITE)

# Desenha o fundo verde da bandeira
pygame.draw.rect(screen, GREEN, pygame.Rect(0, 0, width, height))

# Desenha o losango amarelo
pygame.draw.polygon(screen, YELLOW, [(width // 2, 0), (width, height // 2), (width // 2, height), (0, height // 2)])

# Desenha o círculo azul
circle_center = (width // 2, height // 2)
circle_radius = height // 5
pygame.draw.circle(screen, BLUE, circle_center, circle_radius)

# Desenha a estrela no centro do círculo azul
star_points = []
for i in range(5):
    angle = math.radians(90 + i * 72)
    x = circle_center[0] + int(circle_radius * math.cos(angle))
    y = circle_center[1] - int(circle_radius * math.sin(angle))  # Negativo devido à inversão do eixo y
    star_points.append((x, y))
pygame.draw.polygon(screen, YELLOW, star_points)

# Atualiza a tela
pygame.display.flip()

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Encerramento do Pygame
pygame.quit()
sys.exit()
