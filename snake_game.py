import pygame
import random

pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Snake settings
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("comicsansms", 30)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, 'black')

    screen.blit(value, [0, 0])


def display_snake(snake_block, snake_body):
    for index, x in enumerate(snake_body):
        color = 'yellow' if index % 2 == 0 else 'green'
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])


def display_message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, pos)


# main function
def run_game_loop():
    game_over = False
    game_close = False

    s_x = screen_width / 2
    s_y = screen_height / 2

    s_x_change = 0
    s_y_change = 0

    snake_body = []
    length_of_snake = 1

    foodx = random.randint(5,780)
    foody = random.randint(5, 580)

    while not game_over:

        while game_close == True:
            screen.fill('gray')
            display_message("You Lost! Press SPACE-Play Again or Q-Quit", 'red', [100, 300])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        run_game_loop()

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
        screen.fill('gray')
        pygame.draw.rect(screen, 'red', [foodx, foody, snake_block, snake_block])
        snake_head = [s_x, s_y]
        snake_body.append(snake_head)

        if len(snake_body) > length_of_snake:
            del snake_body[0]

        if snake_head in snake_body[:-1]:
            game_close = True

        display_snake(snake_block, snake_body)
        display_score(length_of_snake - 1)
        pygame.display.update()

        if abs(s_x - foodx) <= snake_block and abs(s_y - foody) <= snake_block:
            foodx = random.randint(5, 780)
            foody = random.randint(5, 580)
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


def run_game():
    menu = True
    while menu:
        screen.fill('gray')
        display_message("Welcome to Snake Game", 'black', [screen_width / 6, screen_height / 3])
        display_message("Press P to Play or Q to Quit", 'black', [screen_width / 6, screen_height / 2])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    run_game_loop()
                if event.key == pygame.K_q:
                    menu = False

    pygame.quit()
    quit()


run_game()
