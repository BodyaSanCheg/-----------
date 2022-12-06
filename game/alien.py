import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """"Класс, представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загрузка изображения пришульца и назначение атрибута rect
        self.image = pygame.image.load('game/images/alien ship.bmp')
        # self.image = pygame.transform.scale(self.image, (self.screen_rect[2]/4,self.screen_rect[3]/6))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)

    def update(self):
        """Перемещение пришельцев вправо"""
        self.x += (self.settings.alien_speed_factor * 
                        self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True