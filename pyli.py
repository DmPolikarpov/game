import pygame
from pygame.sprite import Sprite

class Pyli(Sprite):
	"""создает и управляет пулями"""
	def __init__(self, nlo_settings, screen, korabl):
		"""создает пулю и определяет ее параметры"""
		super().__init__()
		self.screen = screen

		#геометрия пули и начальные координаты
		self.rect = pygame.Rect(0, 0, nlo_settings.pyli_width, nlo_settings.pyli_height)
		self.rect.centerx = korabl.rect.centerx
		self.rect.top = korabl.rect.top

		#перевод позиции пули в веществ.формат и задание переметров пули
		self.y = float(self.rect.y)
		self.color = nlo_settings.pyli_color
		self.speed = nlo_settings.pyli_speed

	def update(self):
		"""создает перемещение пули при выстрелах"""
		self.y -= self.speed
		self.rect.y = self.y

	def draw_pyli(self):
		"""вывод пули на экран"""
		pygame.draw.rect(self.screen, self.color, self.rect)