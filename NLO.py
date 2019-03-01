import pygame
import game_functions as gf
from korabl import Korabl
from settings import Settings
from sfera import Sfera
from pygame.sprite import Group
from enemies import Enemies
from button import Button
from game_over import Game_over




def run_game():
	#функция подключает pygame, настройки, создает экран, инициализирует все модули и запускает основной цикл игры
	pygame.init()
	#определяет настройки
	nlo_settings = Settings()
	#определяет экран
	screen = pygame.display.set_mode((nlo_settings.screen_width, nlo_settings.screen_height))
	#создает название
	pygame.display.set_caption("N L O")
	#создание корабля
	korabl = Korabl(nlo_settings, screen)
	#создание щита
	sfera = Sfera(nlo_settings, screen, korabl)
	#изображение
	fon = pygame.image.load('images/fon.png')
	#группа для хранения пуль
	pyli = Group()
	#группа для хранения врагов
	enemies = Enemies(nlo_settings, screen)
	#группа для хранения пуль врагов
	bullets = Group()
	#группа для хранения жизней корабля
	all_lifes = Group()
	#создание трех жизней
	gf.all_lifes(screen, all_lifes, nlo_settings)
	#создание надписи приветствия
	welcome = Game_over(screen, 'WELCOME')
	#создание кнопки Play
	button_play = Button(nlo_settings, screen, 'Play')
	#создание надписи при проигрыше
	game_over = Game_over(screen, 'GAME OVER')
	#создание надписи при выигрыше
	you_win = Game_over(screen, 'CONGRATULATIONS!')
	#создание кнопки повтора игры
	try_again = Button(nlo_settings, screen, 'Try again')



	#основной цикл игры
	while True:
		#выводит фоновое изображение на экран
		screen.blit(fon,(0,0))
		#проверяет все события (нажатия клавиш, флаги и т.д.)
		gf.check_events(korabl, nlo_settings, screen, pyli, button_play, try_again, all_lifes)
		#условия для запуска игровых действий
		if nlo_settings.game_active:
			if nlo_settings.korabl_view:
				#обновления всех функций в зависимости от событий
				sfera.update()
				korabl.update()
				gf.pyli_update(enemies, pyli, sfera, nlo_settings, bullets)
				gf.life_control(screen, all_lifes, nlo_settings, bullets, korabl)
				gf.bullets_update(bullets, enemies, nlo_settings, screen, korabl, sfera)
				gf.enemies_update(enemies, nlo_settings, screen)
		#обновление экрана
		gf.update_screen(nlo_settings, screen, korabl, sfera, pyli, enemies, bullets, all_lifes, button_play, game_over, try_again, welcome, you_win)
#запуск игры
run_game()