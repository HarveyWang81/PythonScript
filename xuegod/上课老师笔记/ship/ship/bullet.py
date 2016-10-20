import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""一个对飞船发射的子弹进行管理的类"""
	def __init__(self,ai_sttings,screen,ship):
		super(Bullet,self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(0,0,ai_sttings.bullet_width,ai_sttings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)

		self.color = ai_sttings.bullet_color
		self.speed_factor = ai_sttings.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)	