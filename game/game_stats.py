class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_game) -> None:
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в не активном режиме
        self.game_active = False

        # Рекорд не должен сбрасываться
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статитстику, изменяющуюся в ходе игры"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1