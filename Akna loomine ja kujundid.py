import pygame
pygame.init()

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("My Screen")

roheline = (0, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.arc(screen,[255,0,0], [100,100,250,200], 0, 3.14*1.5, 1)
    pygame.display.flip()

    screen.fill(roheline)
    pygame.display.flip()

pygame.quit()