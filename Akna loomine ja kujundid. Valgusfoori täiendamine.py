import pygame

pygame.init()

screen = pygame.display.set_mode((300, 450))
pygame.display.set_caption("ValgusFoor - Alex-Sander Zapotõlok")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 114, 206)
DARK = (30, 30, 30)

screen.fill(BLACK)

pygame.draw.polygon(screen, WHITE, [(105, 350), (195, 350), (150, 380)], 2)
pygame.draw.polygon(screen, BLUE, [(110, 350), (190, 350), (150, 380)])
pygame.draw.polygon(screen, BLACK, [(115, 360), (185, 360), (150, 370)])
pygame.draw.polygon(screen, WHITE, [(120, 370), (180, 370), (150, 375)])

pygame.draw.rect(screen, WHITE, (138, 150, 24, 200), 2)
pygame.draw.rect(screen, DARK, (140, 150, 20, 200))

pygame.draw.rect(screen, WHITE, (110, 50, 80, 180), 2)
pygame.draw.rect(screen, DARK, (112, 52, 76, 176))

pygame.draw.circle(screen, RED, (150, 90), 25)
pygame.draw.circle(screen, YELLOW, (150, 140), 25)
pygame.draw.circle(screen, GREEN, (150, 190), 25)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
