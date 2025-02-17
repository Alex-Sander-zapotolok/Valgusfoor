import pygame
pygame.init()

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Foor - Alex-Sander Zapotõlok")

screen.fill([0, 0, 0])  #taustavärvi

pygame.draw.circle(screen, [0,255,1,255], [150,230], 38, 500) #Roheline
pygame.draw.circle(screen, [255, 255, 0], [150,150], 38, 500) #Kollane
pygame.draw.circle(screen, [255, 0, 0], [150,70], 38, 500) #Punane
pygame.draw.rect(screen, [140, 140, 140], [100, 20, 100, 265], 2) #Loome ristküliku


pygame.display.flip()

while True:
    print("")