import pygame.font

class Button():
	"""создание кнопки и определение ее параметров"""

	def __init__(self, nlo_settings, screen, msg):
		"""создает кнопку"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#создаение размеров и свойств кнопки
		self.width = 200
		self.height = 50
		self.button_color = (255, 0, 0)
		self.text_color = (0, 255, 0)
		self.font = pygame.font.SysFont('arial', 30)
		#расположение кнопки на экране
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.y = 2*self.screen_rect.height/3
		self.rect.centerx = self.screen_rect.centerx

		#сообщение кнопки
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""преобразует текст в msg в прямоугольник и выравнивает текст по центру"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""рисует кнопку на экране"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)