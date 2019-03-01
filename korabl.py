import pygame

class Korabl():

	def __init__(self, nlo_settings, screen):
		"""создает корабль и его начальное положение"""
		self.screen = screen
		self.nlo_settings = nlo_settings

		#загружает корабль и получает прямоугольник
		self.nlo = pygame.image.load('images/nlo.png')
		self.rect = self.nlo.get_rect()
		self.screen_rect = screen.get_rect()
		#каждый новый корабль появляется у нижнего края экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#сохранение вещественной координаты центра координаты Х корабля
		self.center = float(self.rect.centerx)
		#флаг перемещения корабля
		self.moving_right = False
		self.moving_left = False
		

	def update(self):
		"""обновляет позицию корабля на экране"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.nlo_settings.korabl_speed
		if self.moving_left and self.rect.left > 0:
			self.center -= self.nlo_settings.korabl_speed
		#обновление атрибута rect на основании rect.center
		self.rect.centerx = self.center

	def center_korabl(self):
		"""переносит корабль в центр после попадаения"""
		self.center = self.screen_rect.centerx
		

	def blit(self):
		"""рисует корабль на экране"""
		self.screen.blit(self.nlo, self.rect)

