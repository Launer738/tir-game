import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tir Game")
icon = pygame.Surface((32, 32), pygame.SRCALPHA)
icon.fill((20, 24, 36))
pygame.draw.circle(icon, (0, 200, 255), (16, 16), 12, 3)
pygame.draw.line(icon, (0, 200, 255), (16, 5), (16, 27), 2)
pygame.draw.line(icon, (0, 200, 255), (5, 16), (27, 16), 2)
pygame.display.set_icon(icon)

target_wigth = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_wigth)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)


def draw_target(surface, x, y, width, height):
    center_x = x + width // 2
    center_y = y + height // 2
    radius = min(width, height) // 2

    pygame.draw.circle(surface, (240, 240, 240), (center_x, center_y), radius)
    pygame.draw.circle(surface, (220, 0, 0), (center_x, center_y), int(radius * 0.7))
    pygame.draw.circle(surface, (240, 240, 240), (center_x, center_y), int(radius * 0.4))
    pygame.draw.circle(surface, (220, 0, 0), (center_x, center_y), int(radius * 0.15))

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_wigth and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_wigth)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    draw_target(screen, target_x, target_y, target_wigth, target_height)
    pygame.display.update()

pygame.quit()