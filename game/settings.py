class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self) -> None:
        """Инициализирует статические настройки игры"""

        # Парамерны экрана
        self.screen_wigth = 1200
        self.screen_height = 700

        self.bg_collor = (230,230,230) # Цвет экрана

        self.game_name = 'Alien Invasion' # название игры
        
        # Настройки корабля
        self.ship_limit = 3

        # Параметры снарядов
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 2

        # Настройки пришельцев
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 -> влево
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 1.1

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initaialize_dynamic_settings()

    def initaialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # Подсчет очков
        self.alien_points = 50

        # fleet_direction = 1 обозначает движение вправо, а -1 -> влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)