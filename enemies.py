import pygame
from random import randint

class Enemies():
	"""создает класс вражеских кораблей и задает их параметры"""
	def __init__(self, nlo_settings, screen):
		"""создает вражеский корабль, определяет его характеристики и начальное положение"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.start_x = randint(100, 900)
	
		
		#задает параметры и начальные координаты
		self.enemies = pygame.image.load('images/enemy.png')
		self.rect = self.enemies.get_rect()
		
		#задает начальные координаты
		self.rect.x = self.start_x
		self.rect.y = self.rect.height
		#сохранение точной позиции вражеского корабля
		self.center = float(self.rect.centerx)
		#задает скорость перемещения вражеского корабля по экрану
		self.speed = nlo_settings.enemies_speed
		#назначение концевых флагов для перемещений
		self.x_min = True
		self.x_max = False
		self.count_y = 0
		

	def update(self, nlo_settings):
		"""задает перемещение вражеского корабля по экрану"""
		#перемещает вражеский корабль вправо
		if self.x_min:
			if self.rect.right < (self.screen_rect.right):
				self.center += self.speed
			else:
				self.rect.y += self.rect.height
				self.count_y += 1
				self.x_min = False
				self.x_max = True
				if self.count_y == nlo_settings.enemies_step: 
					self.rect.y = self.rect.height
					self.count_y = 0
		#перемещает вражеский корабль влево
		elif self.x_max:
			if self.rect.left > self.screen_rect.left:
				self.center -= self.speed
			else:
				self.x_max = False
				self.x_min = True
		#обновление позиции прямоугольника
		self.rect.x = self.center

	def blit(self):
		"""выводит вражеский корабль на экран в текущей позиции"""
		self.screen.blit(self.enemies, self.rect)
