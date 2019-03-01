import sys
import pygame
from pyli import Pyli
from enemies import Enemies
from bullets import Bullets
from life import Life
from time import sleep
from pygame.sprite import Sprite

#этот модуль содержит все функции, необходимые для работы игры


def check_keydown_events(event, korabl, nlo_settings, screen, pyli):
	"""обрабатывает нажатия клавиш"""
	if event.key == pygame.K_RIGHT:
		#перемещает корабль вправо
		korabl.moving_right = True
	elif event.key == pygame.K_LEFT:
		#перемещает корабль влево
		korabl.moving_left = True
	elif event.key == pygame.K_SPACE:
		#создает новую пулю и включает ее в группу pyli
		if len(pyli) < nlo_settings.pyli_screen_number:
			new_pyli = Pyli(nlo_settings, screen, korabl)
			pyli.add(new_pyli)
	elif event.key == pygame.K_q:
		#быстрый выход из игры
		sys.exit()

def check_keyup_events(event, korabl):
	"""обрабатывает отпускания клавиш"""
	if event.key == pygame.K_RIGHT:
		#остановка перемещения корабля вправо
		korabl.moving_right = False
	elif event.key == pygame.K_LEFT:
		#остановка перемещения корабля влево
		korabl.moving_left = False

def check_events(korabl, nlo_settings, screen, pyli, button_play, try_again, all_lifes):
	"""обрабатывает нажатия клавиш и события"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#выход из игры
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			#проверяет и обрабатывает любое нажатие клавиш
			check_keydown_events(event, korabl, nlo_settings, screen, pyli)
		elif event.type == pygame.KEYUP:
			#проверяет и обрабатывает любое отпускание клавиш
			check_keyup_events(event, korabl)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#проверяет события, коллизии мыши и реагирует на них
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if nlo_settings.korabl_view and button_play.rect.collidepoint(mouse_x, mouse_y):
				#реакция на нажатие кнопки Play
				nlo_settings.game_active = True
				#мышь скрывается
				pygame.mouse.set_visible(False)
			elif try_again.rect.collidepoint(mouse_x, mouse_y):
				#реакция на нажатие кнопки try again
				nlo_settings.game_active = True
				nlo_settings.korabl_view = True
				nlo_settings.you_win = False
				nlo_settings.dinamic_settings()
				pygame.mouse.set_visible(False)
				#создание новых жизней
				life = Life(screen)
				life_width = life.rect.width
				for i in range(nlo_settings.number_hit):
					life = Life(screen)
					life.x = life_width*i
					life.rect.x = life.x
					all_lifes.add(life)


def pyli_update(enemies, pyli, sfera, nlo_settings, bullets):
	"""удаляет пули, вылетевшие за экран и проверяет коллизии пуль"""
	pyli.update()
	for pyla in pyli.copy():
		if pyla.rect.bottom <= 0 or pyla.rect.colliderect(sfera.rect):
			pyli.remove(pyla)
		elif pyla.rect.colliderect(enemies.rect):
			#проверяет столкновения пули и вражеского корабля
			pyli.empty()
			bullets.empty()
			sleep(0.5)
			nlo_settings.speed_increase()
			nlo_settings.enemies_hit += 1
			if nlo_settings.enemies_hit == 3:
				#условие окончания игры
				sleep(0.5)
				nlo_settings.korabl_view = False
				nlo_settings.game_active = False
				nlo_settings.enemies_hit = 0
				nlo_settings.you_win = True
				pygame.mouse.set_visible(True)				


def enemies_update(enemies, nlo_settings, screen):
	"""обновление вражеского корабля"""
	if nlo_settings.enemies_view == True:
		enemies.update(nlo_settings)


def bullets_update(bullets, enemies, nlo_settings, screen, korabl, sfera):
	"""обновление пуль вражеского корабля, контроль их количества"""
	if nlo_settings.enemies_view == True:
		bullets.update()
		if len(bullets) < nlo_settings.bullets_screen_number:
			new_bullet = Bullets(nlo_settings, screen, enemies)
			bullets.add(new_bullet)
		for bullet in bullets.copy():
			if bullet.rect.bottom >= nlo_settings.screen_height or bullet.rect.colliderect(sfera.rect):
				bullets.remove(bullet)


def all_lifes(screen, all_lifes, nlo_settings):
	"""создание жизней"""
	life = Life(screen)
	life_width = life.rect.width
	for i in range(nlo_settings.number_hit):
		life = Life(screen)
		life.x = life_width*i
		life.rect.x = life.x
		all_lifes.add(life)

def life_control(screen, all_lifes, nlo_settings, bullets, korabl):
	"""управление количеством жизней"""
	for bullet in bullets.copy():
		if bullet.rect.colliderect(korabl.rect):
			#проверка попадания пули вражеского корабля в корабль игрока
			nlo_settings.number_hit -= 1
			korabl.center_korabl()
			life = Life(screen)
			life_width = life.rect.width
			life.x = life_width*(nlo_settings.number_hit-1)
			life.rect.x = life.x
			for life in all_lifes.copy():
				if life.rect.x > (nlo_settings.number_hit-1) * life_width:
					all_lifes.remove(life)
			sleep(0.5)
			bullets.empty()
			if nlo_settings.number_hit == 0:
				#условие окончания игры
				nlo_settings.korabl_view = False
				nlo_settings.game_active = False	
				#мышь становится видно
				pygame.mouse.set_visible(True)


		

def update_screen(nlo_settings, screen, korabl, sfera, pyli, enemies, bullets, all_lifes, button_play, game_over, try_again, welcome, you_win):
	"""Обновляет изображения на экране"""
	#вывод пуль на экран
	for pyla in pyli.sprites():
		pyla.draw_pyli() 
	#вывод пуль врагов на экран
	if nlo_settings.enemies_view == True: 
		for bullet in bullets.sprites():
			bullet.draw_bullets()
	#выводит корабль на экран
	if nlo_settings.korabl_view == True:
		korabl.blit()
	#выводит щит на экран
	sfera.blit()
	#выводит врага на экран
	if nlo_settings.enemies_view == True:
		enemies.blit()
	#выводит жизни на экран
	for life in all_lifes.sprites():
		all_lifes.draw(screen)
	#выводит кнопку запуска игры на экран
	if nlo_settings.game_active == False:
		if nlo_settings.korabl_view == True:
			welcome.draw()
			button_play.draw_button()
	#выводит надпись на экран при проигрыше
	if nlo_settings.korabl_view == False and nlo_settings.you_win == False:
		game_over.draw()
		try_again.draw_button()
	#выводит надпись при выигрыше
	if nlo_settings.you_win == True:
		you_win.draw()
		try_again.draw_button()
	#отображение последнего прорисованного экрана
	pygame.display.flip()
