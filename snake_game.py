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


def run_game():
    display_menu()
    pygame.quit()
    quit()


def display_menu():
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
                if event.key == pygame.K_q:
                    menu = False
                if event.key == pygame.K_p:
                    GameLoop().run()
class GameLoop:
    def __init__(self):
        self._reset_game_state()

    def _display_game_over_menu(self):
        screen.fill('gray')
        display_message("You Lost! Press SPACE-Play Again or Q-Quit", 'red', [100, 300])
        display_score(self.length_of_snake - 1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.is_game_over = False
                    self.is_active = False
                if event.key == pygame.K_SPACE:
                    self.is_game_over = False
                    self._reset_game_state()

    def run(self):
        while self.is_active:
            if self.is_game_over:
                self._display_game_over_menu()
            else:
                screen.fill('gray')
                self._snake_step()
                self._refresh_food()
                pygame.display.update()
                clock.tick(snake_speed)

    def _reset_game_state(self):
        self.is_game_over = False
        self.is_active = True

        self.s_x = screen_width / 2
        self.s_y = screen_height / 2

        self.s_x_change = self.s_y_change = 0

        self.snake_body = []
        self.length_of_snake = 1

        self.food_x = random.randint(5, 780)
        self.food_y = random.randint(5, 580)

    def _snake_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.s_x_change = -snake_block
                    self.s_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    self.s_x_change = snake_block
                    self.s_y_change = 0
                elif  event.key == pygame.K_UP:
                    self.s_y_change = -snake_block
                    self.s_x_change = 0
                elif event.key == pygame.K_DOWN:
                    self.s_y_change = snake_block
                    self.s_x_change = 0

        if self.s_x >= screen_width or self.s_x < 0 or self.s_y >= screen_height or self.s_y < 0:
            self.is_game_over = True
        self.s_x += self.s_x_change
        self.s_y += self.s_y_change
        snake_head = [self.s_x, self.s_y]
        self.snake_body.append(snake_head)

        if len(self.snake_body) > self.length_of_snake:
            del self.snake_body[0]

        if snake_head in self.snake_body[:-1]:
            self.is_game_over = True

        display_snake(self.snake_body)
        display_score(self.length_of_snake - 1)

    def _refresh_food(self):
        pygame.draw.rect(screen, 'red', [self.food_x, self.food_y, snake_block, snake_block])
        if abs(self.s_x - self.food_x) <= snake_block and abs(self.s_y - self.food_y) <= snake_block:
            self.food_x = random.randint(5, 780)
            self.food_y = random.randint(5, 580)
            self.length_of_snake += 1

def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, 'black')
    screen.blit(value, [0, 0])


def display_snake(snake_body):
    for index, x in enumerate(snake_body):
        color = 'yellow' if index % 2 == 0 else 'green'
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])


def display_message(msg, color, pos):
    message = font_style.render(msg, True, color)
    screen.blit(message, pos)


run_game()
