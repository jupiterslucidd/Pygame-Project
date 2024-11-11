import pygame
from pygame.locals import *
import sys

from Test import DeathScreen

pygame.mixer.init()
pygame.init()

def level1():
  screen = pygame.display.set_mode((800, 500))

    # Background image
    scaryBackground = pygame.image.load("scaryBackground.jpeg")
    scaryBackground = pygame.transform.scale(scaryBackground, (800, 500))

    # "Maze" background along with image
    easyMaze = pygame.image.load("easyMaze.png")
    easyMaze = pygame.transform.scale(easyMaze, (600, 500))
    easyMaze_rect = easyMaze.get_rect(topleft=(0, 0))

    # "Player"
    player = pygame.image.load("player.png")
    player = pygame.transform.scale(player, (25,30))
    playerRect = player.get_rect()
    playerRect.topleft = (0, 15)  # Initial player position
    player_speed = 1

    # "Exit" option
    menuExit = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 35)
    menuExitSurf = menuExit.render("EXIT", True, (255, 255, 255))
    exitRect = menuExitSurf.get_rect()
    exitRect.center = (690, 400)

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            # Exit by clicking "EXIT"
            if event.type == MOUSEBUTTONDOWN:
                if exitRect.collidepoint(event.pos):
                    sys.exit(0)
    
        # Check movement in each direction and apply if no collision
        if keys[pygame.K_a]:  # Move left
            playerRect.x -= player_speed
        if keys[pygame.K_d]:  # Move right
            playerRect.x += player_speed
        if keys[pygame.K_w]:  # Move up
            playerRect.y -= player_speed
        if keys[pygame.K_s]:  # Move down
            playerRect.y += player_speed
        # Drawing
        screen.blit(scaryBackground, (0, 0))
        screen.blit(player, playerRect.topleft)
        screen.blit(easyMaze, easyMaze_rect.topleft)
        screen.blit(menuExitSurf, exitRect)
    
        pygame.display.flip()

level1()
