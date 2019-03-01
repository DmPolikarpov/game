import pygame

class Sfera():
	"""класс для защитного щита"""
	def __init__(self, nlo_settings, screen, korabl):
		"""создает щит и все его атрибуты"""
		self.screen = screen
		#загрузка щита и создание прямоугольника
		self.sfera = pygame.image.load('images/sfera.png')
		self.rect = self.sfera.get_rect()
		self.screen_rect = screen.get_rect()
		#назначение начальной позиции на экране
		self.rect.left = self.screen_rect.left
		self.rect.bottom = (korabl.rect.top - 10)
		self.x = self.rect.left
		#назначение скорости
		self.sfera_speed = nlo_settings.sfera_speed
		#назначение концевых флагов для перемещений
		self.x_min = True
		self.x_max = False

	def update(self):
		"""перемещает щит по экрану за кораблем"""
		#перемещает щит вправо
		if self.x_min:
			if self.rect.right < self.screen_rect.right:
				self.x += self.sfera_speed
			else:
				self.x_min = False
				self.x_max = True
		#перемещает щит влево
		elif self.x_max:
			if self.rect.left > self.screen_rect.left:
				self.x -= self.sfera_speed
			else:
				self.x_max = False
				self.x_min = True
		#обновление позиции прямоугольника
		self.rect.x = self.x

	def blit(self):
		"""выводит щит на экран"""
		self.screen.blit(self.sfera, self.rect)