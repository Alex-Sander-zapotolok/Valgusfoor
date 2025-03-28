import sys
import pygame

pygame.init()

# Mänguakna suurus
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Formula 1 võidusõidu mäng')
clock = pygame.time.Clock()

# Piltide laadimine ja pööramine
taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")

sinine_auto = pygame.transform.rotate(pygame.image.load("f1_blue.png"), 180)
sinine_auto2 = pygame.transform.rotate(pygame.image.load("f1_blue.png"), 180)
sinine_auto3 = pygame.transform.rotate(pygame.image.load("f1_blue.png"), 180)

# Kiirus ja skoor
speed = 3
skoor = 0

# Siniste autode algasendid (Y-koordinaat)
sin_auto = 32
sin_auto2 = 147
sin_auto3 = 87

# Punase auto algasukoht ja liikumiskiirus
player_x = 297.5
player_y = 391
player_speed = 5

# Kiviaia piirid (tee jääb X-koordinaadi 150 ja 490 vahele)
road_left = 150
road_right = 490 - punane_auto.get_width()  # Lahutame auto laiuse, et see ei läheks üle piiri

# Klahvivajutuste muutujad
move_left = False
move_right = False

gameover = False
while not gameover:
    # Kaadrisageduse piiramine
    clock.tick(60)

    # Sündmuste kontrollimine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        # Kui vajutatakse klahvi alla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True

        # Kui klahv lahti lastakse
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    # Mängija liigutamine koos kiviaia piiranguga
    if move_left and player_x > road_left:
        player_x -= player_speed
    if move_right and player_x < road_right:
        player_x += player_speed

    # Kui sinised autod jõuavad alla, alustavad uuesti ülevalt ja lisavad skoori
    if sin_auto > 480:
        skoor += 1
        sin_auto = 0

    if sin_auto2 > 480:
        skoor += 1
        sin_auto2 = 0

    if sin_auto3 > 480:
        skoor += 1
        sin_auto3 = 0

    # Sinised autod liiguvad alla
    sin_auto += speed
    sin_auto2 += speed
    sin_auto3 += speed

    # Graafika joonistamine
    screen.blit(taust, (0, 0))
    screen.blit(punane_auto, (player_x, player_y))  # Punane auto liigub nüüd
    screen.blit(sinine_auto, (175, sin_auto))
    screen.blit(sinine_auto2, (297.5, sin_auto2))
    screen.blit(sinine_auto3, (415, sin_auto3))

    # Skoori kuvamine
    font = pygame.font.Font(None, 30)
    text = font.render("Formula 1 skoori punktid: " + str(skoor), True, [0, 0, 0])
    screen.blit(text, [200, 0])

    # Ekraani värskendamine
    pygame.display.flip()

pygame.quit()
sys.exit()
