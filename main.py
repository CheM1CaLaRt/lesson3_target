import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Catch me if you can!")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

background = pygame.image.load("img/back.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

catch = pygame.image.load("img/catch.png")
running = True
show_message = False
message_display_time = 0  # Таймер для отображения сообщения

while running:
    screen.blit(background, (0, 0))
    time_now = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                show_message = True
                message_display_time = time_now + 500  # Отображать сообщение в течение 500 мс
    if show_message:
        if time_now <= message_display_time:
            screen.blit(catch, (300, 200))
            #pygame.time.delay(100)
        else:
            show_message = False
    pygame.time.wait(200)
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()