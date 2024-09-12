import pygame


class Settings:
    def __init__(self):
        pygame.init()

        self._apply_screen_settings()
        self._apply_snake_settings()
        self._apply_font_settings()

        self.clock = pygame.time.Clock()

    def _apply_screen_settings(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')

    def _apply_snake_settings(self):
        self.snake_block = 10
        self.snake_speed = 15

    def _apply_font_settings(self):
        self.font_style = pygame.font.SysFont("comicsansms", 30)
        self.score_font = pygame.font.SysFont("comicsansms", 35)


settings = Settings()
