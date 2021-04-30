import pygame

w,h = 800,600

window = pygame.display.set_mode((w,h))

bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (w,h))


game = True
while game:
    window.blit(bg, (0,0))
    pygame.display.update()