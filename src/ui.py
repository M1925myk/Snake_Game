import pygame

from .setting import settings


def display_menu():
    from src.game_loop import GameLoop

    menu = True
    game_loop = GameLoop()
    while menu:
        settings.screen.fill('gray')
        display_message(
            "Welcome to Snake Game", 'black',
            [settings.screen_width / 6, settings.screen_height / 3]
        )
        display_message(
            "Press P to Play or Q to Quit", 'black',
            [settings.screen_width / 6, settings.screen_height / 2]
        )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_loop.run()
                if event.key == pygame.K_q:
                    menu = False


def display_score(score):
    value = settings.score_font.render("Your Score: " + str(score), True, 'black')
    settings.screen.blit(value, [0, 0])


def display_snake(snake_body):
    for index, x in enumerate(snake_body):
        color = 'yellow' if index % 2 == 0 else 'green'
        pygame.draw.rect(settings.screen, color, [x[0], x[1], settings.snake_block, settings.snake_block])


def display_message(msg, color, pos):
    message = settings.font_style.render(msg, True, color)
    settings.screen.blit(message, pos)
