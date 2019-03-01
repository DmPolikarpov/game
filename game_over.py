import pygame.font

class Game_over():
	"""создает экран, появляющийся после проигрыша"""
	def __init__(self, screen, msg):
		"""создает экран и задает его параметры"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		#задает размеры, цвет фона и надписи
		self.rect = pygame.Rect(0, 0, self.screen_rect.width, self.screen_rect.height)
		self.center = self.screen_rect.center
		self.color = (200, 100, 0)
		self.text_color = (0, 250, 0)
		#преобразует текст в msg в прямоугольник и выравнивает текст по центру
		self.font = pygame.font.SysFont('arial', 60)
		self.msg = self.font.render(msg, True, self.text_color, self.color)
		self.msg_rect = self.msg.get_rect()
		self.msg_rect.center = self.rect.center

	def draw(self):
		#выводит на экран
		self.screen.fill(self.color, self.rect)
		self.screen.blit(self.msg, self.msg_rect)