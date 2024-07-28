import pygame
import random


pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# color

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, pos)

# main function
def gameLoop():
    game_over = False
    game_close = False

    s_x = screen_width / 2
    s_y = screen_height / 2

    s_x_change = 0
    s_y_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("You Lost! Press SPACE-Play Again or Q-Quit", red, [screen_width / 6, screen_height / 3])
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    s_x_change = -snake_block
                    s_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    s_x_change = snake_block
                    s_y_change = 0
                elif event.key == pygame.K_UP:
                    s_y_change = -snake_block
                    s_x_change = 0
                elif event.key == pygame.K_DOWN:
                    s_y_change = snake_block
                    s_x_change = 0

        if s_x >= screen_width or s_x < 0 or s_y >= screen_height or s_y < 0:
            game_close = True
        s_x += s_x_change
        s_y += s_y_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(s_x)
        snake_Head.append(s_y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        if s_x == foodx and s_y == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def main_menu():
    menu = True
    while menu:
        screen.fill(blue)
        message("Welcome to Snake Game", green, [screen_width / 6, screen_height / 3])
        message("Press P to Play or Q to Quit", black, [screen_width / 6, screen_height / 2])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameLoop()
                if event.key == pygame.K_q:
                    menu = False

    pygame.quit()
    quit()

main_menu()

