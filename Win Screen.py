import pygame
from pygame.locals import *
import sys
pygame.init()
screen = pygame.display.set_mode((800,500))

#background image
scaryBackground = pygame.image.load("scaryBackground.jpeg")
scaryBackground = pygame.transform.scale(scaryBackground, (800,500))

#"You Win!" title
winTitle = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 120)
winTitleSurf = winTitle.render("You Win!", True, (255,255,255))

winTitleRect = winTitleSurf.get_rect()
winTitleRect.center = (400,140)

#"Back to Menu" option
menu = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 30)
menuSurf = menu.render("Back to menu", True, (255,255,255))

menuRect = menuSurf.get_rect()
menuRect.center = (400,250)

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            if menuRect.collidepoint(event.pos):
                MenuScreen()


    mouse_pos = pygame.mouse.get_pos()

    if menuRect.collidepoint(mouse_pos):
        menuSurf = menu.render("Back to menu", True, (255, 0, 0))
    else:
        menuSurf = menu.render("Back to menu", True, (255, 255, 255))

    screen.blit(scaryBackground, (0, 0))

    screen.blit(winTitleSurf, winTitleRect)
    screen.blit(menuSurf, menuRect)

    pygame.display.flip()