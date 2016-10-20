import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
	#初始化游戏，并且创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#设定屏幕大小
	pygame.display.set_caption('Alien Invasion')
	ship = Ship(ai_settings,screen)
	bullets = Group()
	#bg_color = (230,230,230)
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_bullets(bullets)
		# for bullet in bullets.copy():
		# 	if bullet.rect.bottom <= 0:
		# 		bullets.remove(bullet)
		# 		print(len(bullets))
		gf.update_screen(ai_settings,screen,ship,bullets)

		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()
		# screen.fill(ai_settings.bg_color)
		# ship.blitme()
		# pygame.display.flip()
run_game()