import pygame
from pygame.locals import *
import sys
import random

pygame.mixer.init()
pygame.init()

def InstructionScreen():
    screen = pygame.display.set_mode((800, 500))

    # background image
    scaryBackground = pygame.image.load("scaryBackground.jpeg")
    scaryBackground = pygame.transform.scale(scaryBackground, (800, 500))

    # "Instructions" title
    menuInstructionsTitle = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 40)
    menuInstructionsTitleSurf = menuInstructionsTitle.render("INSTRUCTIONS", True, (255, 255, 255))
    instructionsTitleRect = menuInstructionsTitleSurf.get_rect()
    instructionsTitleRect.center = (400, 60)

    # "start"
    menuStart = pygame.font.Font('Creepster-Regular.ttf', 40)
    menuStartSurf = menuStart.render("START", True, (255, 255, 255))
    startRect = menuStartSurf.get_rect()
    startRect.center = (400, 450)

    # "Back" back to menu
    menuBack = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 35)
    menuBackSurf = menuBack.render("Back", True, (255, 255, 255))

    menuBackRect = menuBackSurf.get_rect()
    menuBackRect.center = (690, 455)

    # actual instructions
    menuInstructions = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 22)

    # lines of instructions
    line1 = menuInstructions.render("All you need to do is to get to the end of each maze!", True, (255, 255, 255))
    line1Rect = line1.get_rect(center=(400, 120))

    line2 = menuInstructions.render("There will be two levels of mazes which will increase in difficulty!", True,
                                    (255, 255, 255))
    line2Rect = line2.get_rect(center=(400, 150))

    line3 = menuInstructions.render("Beware of unexpected enemies!", True, (255, 255, 255))
    line3Rect = line3.get_rect(center=(400, 180))

    # moving instructions
    menuMovingInstructions = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 40)

    howTo = menuMovingInstructions.render("How to move:", True, (255, 255, 255))
    howToRect = howTo.get_rect(center=(180, 280))

    wKey = menuMovingInstructions.render("W", True, (255, 0, 0))
    wKeyRect = wKey.get_rect(center=(180, 340))

    aKey = menuMovingInstructions.render("A", True, (255, 0, 0))
    aKeyRect = aKey.get_rect(center=(140, 380))

    sKey = menuMovingInstructions.render("S", True, (255, 0, 0))
    sKeyRect = sKey.get_rect(center=(180, 380))

    dKey = menuMovingInstructions.render("D", True, (255, 0, 0))
    dKeyRect = dKey.get_rect(center=(220, 380))

    #"Your player:"
    playerTitle = menuMovingInstructions.render("Your player:", True, (255, 255, 255))
    playerTitleRect = playerTitle.get_rect(center=(580,280))

    #player image
    playerImage = pygame.image.load("player.png")
    playerImage = pygame.transform.scale(playerImage, (80,80))

    # WASD instructions
    menuWASDInstructions = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 20)

    line4 = menuWASDInstructions.render("W- Up", True, (255, 255, 255))
    line4Rect = line4.get_rect(center=(50, 340))

    line5 = menuWASDInstructions.render("A- Left", True, (255, 255, 255))
    line5Rect = line5.get_rect(center=(50, 360))

    line6 = menuWASDInstructions.render("S- Down", True, (255, 255, 255))
    line6Rect = line6.get_rect(center=(50, 380))

    line7 = menuWASDInstructions.render("D- Right", True, (255, 255, 255))
    line7Rect = line6.get_rect(center=(50, 400))

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if menuBackRect.collidepoint(event.pos):
                    MenuScreen()
            if event.type == MOUSEBUTTONDOWN:
                if startRect.collidepoint(event.pos):
                    level1()
        # change color of the "start" option to red when hovered over
        mouse_pos = pygame.mouse.get_pos()
        if startRect.collidepoint(mouse_pos):
            menuStartSurf = menuStart.render("START", True, (255, 0, 0))
        else:
            menuStartSurf = menuStart.render("START", True, (255, 255, 255))
            # change color of the "exit" option to red when hovered over
        if menuBackRect.collidepoint(mouse_pos):
            menuBackSurf = menuBack.render("Back", True, (255, 0, 0))
        else:
            menuBackSurf = menuBack.render("Back", True, (255, 255, 255))

        screen.blit(scaryBackground, (0, 0))

        screen.blit(menuInstructionsTitleSurf, instructionsTitleRect)
        screen.blit(menuStartSurf, startRect)
        screen.blit(menuBackSurf, menuBackRect)

        screen.blit(line1, line1Rect)
        screen.blit(line2, line2Rect)
        screen.blit(line3, line3Rect)

        screen.blit(howTo, howToRect)
        screen.blit(wKey, wKeyRect)
        screen.blit(aKey, aKeyRect)
        screen.blit(sKey, sKeyRect)
        screen.blit(dKey, dKeyRect)

        screen.blit(playerTitle, playerTitleRect)
        screen.blit(playerImage, (530, 320))

        screen.blit(line4, line4Rect)
        screen.blit(line5, line5Rect)
        screen.blit(line6, line6Rect)
        screen.blit(line7, line7Rect)

        pygame.display.flip()

def CreditsScreen():
    screen = pygame.display.set_mode((800, 500))

    # background image
    scaryBackground = pygame.image.load("scaryBackground.jpeg")
    scaryBackground = pygame.transform.scale(scaryBackground, (800, 500))

    # credits
    menuCredits = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 22)

    # lines of credits
    line1 = menuCredits.render("Rachel Gamble - Leader", True, (255, 255, 255))
    line1Rect = line1.get_rect(center=(400, 120))

    line2 = menuCredits.render("Tinnola Adeboye - Front-End/Sounds & Graphics", True, (255, 255, 255))
    line2Rect = line2.get_rect(center=(400, 160))

    line3 = menuCredits.render("Johnathan Atkins - ", True, (255, 255, 255))
    line3Rect = line3.get_rect(center=(400, 200))

    line4 = menuCredits.render("Malcom Mcginty - ", True, (255, 255, 255))
    line4Rect = line4.get_rect(center=(400, 240))

    line5 = menuCredits.render("Robert Russell - ", True, (255, 255, 255))
    line5Rect = line5.get_rect(center=(400, 280))

    # "Back" back to menu
    menuBack = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 35)
    menuBackSurf = menuBack.render("Back", True, (255, 255, 255))

    menuBackRect = menuBackSurf.get_rect()
    menuBackRect.center = (690, 455)

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if menuBackRect.collidepoint(event.pos):
                    MenuScreen()

        mouse_pos = pygame.mouse.get_pos()
        # change color of the "back" option to red when hovered over
        if menuBackRect.collidepoint(mouse_pos):
            menuBackSurf = menuBack.render("Back", True, (255, 0, 0))
        else:
            menuBackSurf = menuBack.render("Back", True, (255, 255, 255))

        screen.blit(scaryBackground, (0, 0))

        screen.blit(line1, line1Rect)
        screen.blit(line2, line2Rect)
        screen.blit(line3, line3Rect)
        screen.blit(line4, line4Rect)
        screen.blit(line5, line5Rect)

        screen.blit(menuBackSurf, menuBackRect)
        pygame.display.flip()

def DeathScreen():
    screen = pygame.display.set_mode((800, 500))

    # black and white background version
    scaryBackground = pygame.image.load("BWscaryBackground1.jpeg")
    scaryBackground = pygame.transform.scale(scaryBackground, (800, 500))

    # "wasted" title
    deadTitle = pygame.font.Font('pricedown bl.otf', 100)
    deadTitleSurf = deadTitle.render("wasted", True, (255, 0, 0))

    deadTitleRect = deadTitleSurf.get_rect()
    deadTitleRect.center = (400, 140)

    # "try again"
    deadTryagain = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 30)
    deadTryagainSurf = deadTryagain.render("Try Again", True, (255, 255, 255))

    deadTryagainRect = deadTryagainSurf.get_rect()
    deadTryagainRect.center = (400, 250)

    # "exit"
    deadExit = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 30)
    deadExitSurf = deadExit.render("Exit", True, (255, 255, 255))

    deadExitRect = deadExitSurf.get_rect()
    deadExitRect.center = (400, 289)

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if deadExitRect.collidepoint(event.pos):
                    sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if deadTryagainRect.collidepoint(event.pos):
                    level1()

        mouse_pos = pygame.mouse.get_pos()

        if deadTryagainRect.collidepoint(mouse_pos):
            deadTryagainSurf = deadTryagain.render("Try Again", True, (255, 0, 0))
        else:
            deadTryagainSurf = deadTryagain.render("Try Again ", True, (255, 255, 255))

        if deadExitRect.collidepoint(mouse_pos):
            deadExitSurf = deadExit.render("Exit", True, (255, 0, 0))
        else:
            deadExitSurf = deadExit.render("Exit", True, (255, 255, 255))

        screen.blit(scaryBackground, (0, 0))

        screen.blit(deadTitleSurf, deadTitleRect)
        screen.blit(deadTryagainSurf, deadTryagainRect)
        screen.blit(deadExitSurf, deadExitRect)

        pygame.display.flip()

def Hooray():
    screen = pygame.display.set_mode((800, 500))

    # background image
    scaryBackground = pygame.image.load("scaryBackground.jpeg")
    scaryBackground = pygame.transform.scale(scaryBackground, (800, 500))

    #"Hooray" Sound
    hiphipHooray = pygame.mixer.Sound("FNAFHooray.mp3")
    sound_played = False

    # "You Win!" title
    winTitle = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 120)
    winTitleSurf = winTitle.render("You Win!", True, (255, 255, 255))

    winTitleRect = winTitleSurf.get_rect()
    winTitleRect.center = (400, 140)

    # "Back to Menu" option
    menu = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 30)
    menuSurf = menu.render("Back to menu", True, (255, 255, 255))

    menuRect = menuSurf.get_rect()
    menuRect.center = (400, 250)

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
                    MenuScreen()  # Go back to menu when "Back to menu" is clicked

        mouse_pos = pygame.mouse.get_pos()

        if menuRect.collidepoint(mouse_pos):
            menuSurf = menu.render("Back to menu", True, (255, 0, 0))
        else:
            menuSurf = menu.render("Back to menu", True, (255, 255, 255))

        #plays hiphipHooray sound
        if not sound_played:
            hiphipHooray.play()
            sound_played = True

        # Render the background and win message
        screen.blit(scaryBackground, (0, 0))
        screen.blit(winTitleSurf, winTitleRect)
        screen.blit(menuSurf, menuRect)

        pygame.display.flip()  # Ensure the screen is updated

def level1():
    screen = pygame.display.set_mode((800, 500))

    # Background image
    scaryBackground = pygame.image.load("scaryBackground.jpeg")
    scaryBackground = pygame.transform.scale(scaryBackground, (800, 500))

    # "Maze" background along with image
    easyMaze = pygame.image.load("easyMaze.png")
    easyMaze = pygame.transform.scale(easyMaze, (600, 500))
    easyMaze_rect = easyMaze.get_rect(topleft=(0, 0))

    # "maze" mask
    easyMaze_mask = pygame.mask.from_surface(easyMaze)

    # "Player"
    player = pygame.image.load("player.png")
    player = pygame.transform.scale(player, (40, 50))
    playerRect = player.get_rect()
    playerRect.topleft = (0, 50)  # Initial player position
    player_speed = 1
    # "player" mask
    player_mask = pygame.mask.from_surface(player)

    # "Enemy"
    enemy = pygame.image.load("bat.png")
    enemy = pygame.transform.scale(enemy, (40, 50))
    enemy_mask = pygame.mask.from_surface(enemy)
    enemy_speed = 0.5

    def spawn_enemy():
        enemy_x = random.randint(easyMaze_rect.left, easyMaze_rect.right - enemy.get_width())
        enemy_y = random.randint(easyMaze_rect.top, easyMaze_rect.bottom - enemy.get_height())
        return pygame.Rect(enemy_x, enemy_y, enemy.get_width(), enemy.get_height())

    enemyRect = spawn_enemy()

    #Winner end
    winZone = pygame.Rect(easyMaze_rect.right - 60, easyMaze_rect.bottom - 60, 50, 50)

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

        offset = (playerRect.x - easyMaze_rect.x, playerRect.y - easyMaze_rect.y)
        if easyMaze_mask.overlap(player_mask, offset):
            DeathScreen()

        enemyRect.y += enemy_speed
        if enemyRect.top > easyMaze_rect.bottom:
            enemyRect = spawn_enemy()

        # death by enemy
        offset_enemy = (enemyRect.x - playerRect.x, enemyRect.y - playerRect.y)
        if player_mask.overlap(enemy_mask, offset_enemy):
            DeathScreen()

        # when player reaches end of maze
        if playerRect.colliderect(winZone):
            Hooray()

        #Display
        screen.blit(scaryBackground, (0, 0))
        screen.blit(player, playerRect.topleft)
        screen.blit(enemy, enemyRect.topleft)
        screen.blit(easyMaze, easyMaze_rect.topleft)
        screen.blit(menuExitSurf, exitRect)

        pygame.display.flip()

def MenuScreen():
    screen = pygame.display.set_mode((800, 500))

    # background image
    scaryBackground = pygame.image.load("scaryBackground.jpeg")
    scaryBackground = pygame.transform.scale(scaryBackground, (800, 500))

    # "scary maze" title
    menuTitle = pygame.font.Font('Creepster-Regular.ttf', 95)
    menuTitleSurf = menuTitle.render("Scary Maze", True, (255, 255, 255))

    titleRect = menuTitleSurf.get_rect()
    titleRect.center = (400, 70)

    # "start" option
    menuStart = pygame.font.Font('Creepster-Regular.ttf', 80)
    menuStartSurf = menuStart.render("START", True, (255, 255, 255))

    startRect = menuStartSurf.get_rect()
    startRect.center = (400, 190)

    # "instructions" option
    menuInstructions = pygame.font.Font('Creepster-Regular.ttf', 20)
    menuInstructionsSurf = menuInstructions.render("instructions", True, (255, 255, 255))

    menuInstructionsRect = menuInstructionsSurf.get_rect()
    menuInstructionsRect.center = (400, 260)

    # "credits" option
    menuCredits = pygame.font.Font('PixelifySans-VariableFont_wght.ttf', 20)
    menuCreditsSurf = menuCredits.render("credits", True, (255, 255, 255))

    creditsRect = menuCreditsSurf.get_rect()
    creditsRect.center = (70, 50)

    # "exit" option
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
            # exit by clicking "EXIT"
            if event.type == MOUSEBUTTONDOWN:
                if exitRect.collidepoint(event.pos):
                    sys.exit(0)

            # Spooky sound plays when you click start
            spookySound = pygame.mixer.Sound('SpookySound.mp3')
            if event.type == MOUSEBUTTONDOWN:
                if startRect.collidepoint(event.pos):
                    spookySound.play()
                    pygame.time.delay(2000) #Waits for sound to play then sends you to the next screen!
                    level1()

            # clapping sound plays when you click start
            clappingSound = pygame.mixer.Sound('clappingSound.mp3')
            if event.type == MOUSEBUTTONDOWN:
                if creditsRect.collidepoint(event.pos):
                    clappingSound.play()
                    clappingSound.fadeout(2500) # fading out the sound
                    level1()

            if event.type == MOUSEBUTTONDOWN:
                if menuInstructionsRect.collidepoint(event.pos):
                    InstructionScreen()
            if event.type == MOUSEBUTTONDOWN:
                if creditsRect.collidepoint(event.pos):
                    CreditsScreen()

        mouse_pos = pygame.mouse.get_pos()
        # change color of the "credits" option to red when hovered over
        if creditsRect.collidepoint(mouse_pos):
            menuCreditsSurf = menuCredits.render("credits", True, (255, 0, 0))
        else:
            menuCreditsSurf = menuCredits.render("credits", True, (255, 255, 255))
        # change color of the "start" option to red when hovered over
        if startRect.collidepoint(mouse_pos):
            menuStartSurf = menuStart.render("START", True, (255, 0, 0))
        else:
            menuStartSurf = menuStart.render("START", True, (255, 255, 255))
        # change color of the "exit" option to red when hovered over
        if exitRect.collidepoint(mouse_pos):
            menuExitSurf = menuExit.render("EXIT", True, (255, 0, 0))
        else:
            menuExitSurf = menuExit.render("EXIT", True, (255, 255, 255))
        # change color of the "instructions" option to red when hovered over
        if menuInstructionsRect.collidepoint(mouse_pos):
            menuInstructionsSurf = menuInstructions.render("instructions", True, (255, 0, 0))
        else:
            menuInstructionsSurf = menuInstructions.render("instructions", True, (255, 255, 255))

        screen.blit(scaryBackground, (0, 0))

        screen.blit(menuTitleSurf, titleRect)
        screen.blit(menuStartSurf, startRect)
        screen.blit(menuInstructionsSurf, menuInstructionsRect)
        screen.blit(menuCreditsSurf, creditsRect)
        screen.blit(menuExitSurf, exitRect)

        pygame.display.flip()

MenuScreen()
