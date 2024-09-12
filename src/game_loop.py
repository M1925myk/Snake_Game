import random

import pygame

from .ui import display_snake, display_score, display_message

from .setting import settings


class GameLoop:
    def __init__(self):
        self._reset_game_state()

    def run(self):
        while self.is_active:
            if self.is_game_over:
                self._display_game_over_menu()
            else:
                settings.screen.fill('gray')
                self._snake_step()
                self._refresh_food()
                pygame.display.update()
                settings.clock.tick(settings.snake_speed)

    def _display_game_over_menu(self):
        settings.screen.fill('gray')
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

    def _reset_game_state(self):
        self.is_game_over = False
        self.is_active = True

        self.s_x = settings.screen_width / 2
        self.s_y = settings.screen_height / 2

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
                    self.s_x_change = -settings.snake_block
                    self.s_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    self.s_x_change = settings.snake_block
                    self.s_y_change = 0
                elif event.key == pygame.K_UP:
                    self.s_y_change = -settings.snake_block
                    self.s_x_change = 0
                elif event.key == pygame.K_DOWN:
                    self.s_y_change = settings.snake_block
                    self.s_x_change = 0

        if self.s_x >= settings.screen_width or self.s_x < 0 or self.s_y >= settings.screen_height or self.s_y < 0:
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
        snake_block = settings.snake_block
        pygame.draw.rect(settings.screen, 'red', [self.food_x, self.food_y, snake_block, snake_block])
        if abs(self.s_x - self.food_x) <= snake_block and abs(self.s_y - self.food_y) <= snake_block:
            self.food_x = random.randint(5, 780)
            self.food_y = random.randint(5, 580)
            self.length_of_snake += 1
