#Importing Modules
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

input_rect = pygame.Rect(10, 260, 200, 32)


def text_screen(text, color, x, y):
    """This Function defines the font and color and size of the text

    Args:
        text (_type_):  type of font
        color (_type_):  what color the text is
        x (_type_):  size of x coordinate of text
        y (_type_): size of the y coordinate of text
    """
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    """

    Args:
        snk_list (list):List that represents the amount of tail the snake has
        snake_size (integer): How many times its original size the snake is
    """
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    """This is the main menu function. It runs when the game is opened. It has a multiple lines of text as well as an input that changes the speed of the snake. 
    When enter is pressed then the game is run with the speed of the snake now definied.   
    """
    global user_text
    exit_game = False
    while not exit_game:
        gameWindow.fill((dark_blue))
        pygame.draw.rect(gameWindow, light_blue, input_rect, 4)
        text_surface = font.render(user_text, True, orange)
        gameWindow.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 15)
        text_screen("Welcome to Clickey Snake without the Clickey", orange, 10, 70)
        text_screen("Enter Snake Speed Below, Must Between 5, 15 or can't start game ", light_blue, 10, 180)
        text_screen("Game Will Close If Text Input", light_blue, 10, 220)
        text_screen("Instructions  ", orange, 10, 400)
        text_screen("Use arrow key and collect as many fuit ", orange, 10, 460)
        text_screen("without hitting the wall or tail", orange, 10, 490)
        text_screen("Press Enter To Play", orange, 10, 340)
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
#Spawn fruit coordinates randomly
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = int(user_text)
    snake_size = 30
    fps = 60
    #If game over is true then creates new window with keystroke allowing playing to replay game
    while not exit_game:
        if game_over:
            gameWindow.fill(light_blue)
            #prints text on screen
            text_screen("Game Over! Press Enter To Continue", dark_blue, 100, 250)
            #Allows player to quit the game 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                #when enter is clicked restartes game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            #if exit game or gameover not used then these are main game. 
            #Allows the user to quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                #allows user to move snake right by clicking right arrow - does this by recognizing when arrow click then changing the velocity in opposite direction to 0 thefore moving the snake.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    #allows user to move snake left by clicking left arrow - does this by recognizing when arrow click then changing the velocity in opposite direction to 0 thefore moving the snake.
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    #allows the user to move the snake up by clicking up arrow - does this by recognizing when arrow click then changing the velocity in opposite direction to 0 thefore moving the snake.
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    #allows the user to move the snake down by click arrow - does this by recognizing when arrow click then changing the velocity in opposite direction to 0 thefore moving the snake.
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            #adding snake coordiates to velocity. 
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            #when snake in is a close enough proximity to fruit it regitster this then add 1 to score and respawn fruit randomly. It also increases snake length
            if abs(snake_x - food_x)<28 and abs(snake_y - food_y)<28:
                score +=1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
            #Adds score as the food is eaten
            gameWindow.fill(light_blue)
            text_screen("Score: " + str(score * 10), dark_blue, 5, 5)
            pygame.draw.rect(gameWindow, dark_blue, [food_x, food_y, snake_size, snake_size])

            #Creates a list for the head then adds to the list everytime fruit eaten
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            #Makes sure snake does not get longer than the lsit
            if len(snk_list)>snk_length:
                del snk_list[0]
            #if snake head hits list stops game
            if head in snk_list[:-1]:
                game_over = True
            #If snake collies with wall then game over
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, orange, snk_list, snake_size)
            #To update loop consitantly 
        pygame.display.update()
        #allows to pick fps
        clock.tick(fps)
    #allows user to quit
    pygame.quit()
    quit()
#runs welcome function at start for menu
welcome()