import pygame
from pygame.locals import *
import sys

from Test import DeathScreen

pygame.mixer.init()
pygame.init()

def level1():
    pygame.mixer.init()
    pygame.init()

    screen = pygame.display.set_mode((800, 500))

    # Background image
    scaryBackground = pygame.image.load("scaryBackground.jpeg")
    scaryBackground = pygame.transform.scale(scaryBackground, (800, 500))

    # "Maze" background along with image
    easyMaze = pygame.image.load("easyMaze.png")
    easyMaze = pygame.transform.scale(easyMaze, (600, 400))
    easyMaze_mask = pygame.mask.from_surface(easyMaze)

    # "Player"
    player = pygame.image.load("player.png")
    playerRect = player.get_rect()
    playerRect.topleft = (100, 100)  # Initial player position
    player_speed = 5

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

        # Player movement
        if keys[pygame.K_a]:
            playerRect.x -= player_speed
        if keys[pygame.K_d]:
            playerRect.x += player_speed
        if keys[pygame.K_w]:
            playerRect.y -= player_speed
        if keys[pygame.K_s]:
            playerRect.y += player_speed

        # Collision detection
        player_mask = pygame.mask.from_surface(player)
        offset = (playerRect.x - 0, playerRect.y - 0)  # Adjust to easyMaze position if necessary
        if easyMaze_mask.overlap(player_mask, offset):
            DeathScreen()  # Display collision message

        # Drawing
        screen.blit(scaryBackground, (0, 0))
        screen.blit(easyMaze, (0, 0))
        screen.blit(player, playerRect.topleft)  # Draw player at its position
        screen.blit(menuExitSurf, exitRect)

        pygame.display.flip()

level1()
