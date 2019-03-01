import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
	"""создает и управляет пулями"""
	def __init__(self, nlo_settings, screen, enemies):
		"""создает пулю и определяет ее параметры"""
		super().__init__()
		self.screen = screen

		#геометрия пули и начальные координаты
		self.rect = pygame.Rect(0, 0, nlo_settings.bullets_width, nlo_settings.bullets_height)
		self.rect.centerx = enemies.rect.centerx
		self.rect.bottom = enemies.rect.bottom

		#перевод позиции пули в веществ.формат и задание переметров пули
		self.y = float(self.rect.y)
		self.color = nlo_settings.bullets_color
		self.speed = nlo_settings.bullets_speed


	def update(self):
		"""создает перемещение пули при выстрелах"""
		#перемещение пули по экрану
		self.y += self.speed
		#обновление позиции прямоугольника
		self.rect.y = self.y

	def draw_bullets(self):
		"""вывод пули на экран"""
		pygame.draw.rect(self.screen, self.color, self.rect)