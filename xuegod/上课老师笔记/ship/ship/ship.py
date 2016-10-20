import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		"""初始化飞船，并且设置飞船初始位置"""
		
		#加载飞船图像并且获取其外接炬形
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘飞船放在底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.rect.centerx += 1
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.rect.centerx -= 1
			self.center += self.ai_settings.ship_speed_factor

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)