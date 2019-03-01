import pygame
from pygame.sprite import Sprite

class Life(Sprite):
	"""создает жизни корабля"""
	def __init__(self, screen):
		super().__init__()
		self.screen = screen
					
		"""загружает изображение и задает расположение на экране"""
		self.image = pygame.image.load('images/life.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#задает координаты прямоугольника
		self.rect.top = self.screen_rect.top
		self.rect.left = self.screen_rect.left

	def blitme(self):
		"""отображает на экране"""
		self.screen.blit(self.image, self.rect)

