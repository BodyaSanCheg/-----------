import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    
    """Класс для управления караблем"""
    def __init__(self, ai_game) -> None:
        
        """Инициализирует корабль и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Загружает изображение корабля и получает прямоугольник
        self.image_front = pygame.image.load('game/images/star_ship_front.bmp')
        self.image_front = self._image_size(self.image_front)
        self.image = self.image_front

        self.image_right = pygame.image.load('game/images/star_ship_right.bmp')
        self.image_right = self._image_size(self.image_right)

        self.image_left = pygame.image.load('game/images/star_ship_left.bmp')
        self.image_left = self._image_size(self.image_left)

        self.rect = self.image_front.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты корабля
        self.x = float(self.rect.x)
        
        # Флаги преремещения
        self.moving_right = False
        self.moving_left = False

    def _image_size(self, image):
        return pygame.transform.scale(image, (self.screen_rect[2]/14,self.screen_rect[3]/14))

    def update(self):
        """Обновляет позицию коробля с учетом флага"""
        # Обновляется атрибут х, а не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
            self.image = self.image_right


        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed_factor
            self.image = self.image_left
            
        if (not self.moving_right and not self.moving_left) or (self.moving_right and self.moving_left):
            self.image = self.image_front

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в лекущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)