from numpy import unicode_
import pygame
import random

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
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
user_text = ''

input_rect = pygame.Rect(300, 250, 140, 32)
# color = pygame.Color('lightskyblue3')

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    """_summary_
    """
    global user_text
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        pygame.draw.rect(gameWindow, dark_blue, input_rect, 2)
        text_surface = font.render(user_text, True, orange)
        gameWindow.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 15)
        text_screen("Welcome to Clickey Snake without the Clickey", orange, 10, 50)
        text_screen("Enter Snake Speed Below, Must Between 5, 15 or cant start game ", orange, 5, 180)
        text_screen("Game Will Close If Text Input", orange, 10, 220)
        text_screen("Instructions - Use arrow key and collect as many fuit without ", orange, 5, 400)
        text_screen("hitting the wall or tail", orange, 5, 450)
        text_screen("Press Enter To Play", orange, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                        if int(user_text) < 16 and int(user_text) > 4:
                          gameloop()

        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = int(user_text)
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            gameWindow.fill(light_blue)
            text_screen("Game Over! Press Enter To Continue", dark_blue, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5

            gameWindow.fill(light_blue)
            text_screen("Score: " + str(score * 10), dark_blue, 5, 5)
            pygame.draw.rect(gameWindow, dark_blue, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, orange, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()