import sys

import pygame
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Formula 1 võidusõidu möng')
clock = pygame.time.Clock()

taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.transform.rotate(pygame.image.load("f1_blue.png"), 180)
sinine_auto2 = pygame.transform.rotate(pygame.image.load("f1_blue.png"), 180)
sinine_auto3 = pygame.transform.rotate(pygame.image.load("f1_blue.png"), 180)


speed = 3
skoor = 0

sin_auto = 32
sin_auto2 = 147
sin_auto3 = 87

player_x = 297.5
player_y = 391
player_speed = 5

road_left = 150
road_right = 490

move_left = False
move_right = False

gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    if move_left and player_x > road_left:
        player_x -= player_speed
    if move_right and player_x < road_right - punane_auto.get_width():
        player_x += player_speed

    if sin_auto > 480:
        skoor += 1
        sin_auto = 0

    if sin_auto2 > 480:
        skoor += 1
        sin_auto2 = 0

    if sin_auto3 > 480:
        skoor += 1
        sin_auto3 = 0







    sin_auto += speed
    sin_auto2 += speed
    sin_auto3 += speed

    screen.blit(taust, (0, 0))
    screen.blit(punane_auto, (player_x, player_y))
    screen.blit(sinine_auto, (175, sin_auto))
    screen.blit(sinine_auto2, (297.5, sin_auto2))
    screen.blit(sinine_auto3, (415, sin_auto3))

    font = pygame.font.Font(None, 30)
    text = font.render("Formula 1 skoori punktid: " + str(skoor), True, [0, 0, 0])
    screen.blit(text, [200, 0])



    pygame.display.flip()

pygame.quit()
sys.exit()