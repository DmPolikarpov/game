class Settings():
	"""класс для хранения всех настроек игры"""
	def __init__(self):
		"""создает постоянные настройки игры"""
		#параметры экрана
		self.screen_height = 700
		self.screen_width = 1100
		#регулировка скорости щита
		self.sfera_speed = 4
		#параметры пули
		self.pyli_height = 10
		self.pyli_width = 5
		self.pyli_color = (0, 255, 0)
		self.pyli_screen_number = 2
		#количество попаданий во врагов
		self.enemies_hit = 0
		#количество спусков врага
		self.enemies_step = 3
		#параметры пули врагов
		self.bullets_height = 10
		self.bullets_width = 5
		self.bullets_color = (255, 0, 0)
		self.bullets_screen_number = 1

		#управление игрой (флаги)
		self.game_active = False
		self.korabl_view = True
		self.enemies_view = True
		self.game_over = False
		self.you_win = False

		#ускорение игры при переходе на новый уровень
		self.scale_boats_speed = 1.4
		self.scale_korabl_speed = 1.1
		self.scale_bullets_speed = 1.3
		self.dinamic_settings()

	def dinamic_settings(self):
		"""создает настройки, которые меняются при переходе на новый уровень"""
		#регулировка скорости врага
		self.enemies_speed = 6
		self.bullets_speed = 13
		self.pyli_speed = 11
		self.korabl_speed = 8
		self.number_hit = 3

	def speed_increase(self):
		"""увеличивает скорости"""
		self.enemies_speed *= self.scale_boats_speed
		self.bullets_speed *= self.scale_bullets_speed
		self.pyli_speed *= self.scale_bullets_speed
		self.korabl_speed *= self.scale_korabl_speed		