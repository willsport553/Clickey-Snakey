import pygame
pygame.init()

# Colors
light_blue = (173,216,230)
dark_blue = (0,0,139)
orange = (255,140,0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Clickey Snake")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    gameWindow.fill(light_blue)
    pygame.display.update()

pygame.quit()
quit()