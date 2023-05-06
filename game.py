import pygame
import sys

from ai import find_best_turn
from time import sleep

screen_size = 300

class Game():
	def __init__(self):
		pygame.init()
		self.field = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
		self.screen = pygame.display.set_mode((screen_size + 100, screen_size + 200))
		self.cell_size = int(screen_size / 3)
		self.player = 'x'

	def run(self):
		while(True):
			if self.check_field_state():
				self.message(self.check_field_state())
				pygame.display.update()
				sleep(1)
				for i in range(len(self.field)):
					self.field[i] = '.'
				self.player = 'x'
			if self.player == 'o':
				self.field = find_best_turn(self.player,self.field)
				self.player = 'x'
				pygame.event.clear()
			self.check_events()
			self.update_screen()
	
	def draw_field(self):
		dst = int(self.cell_size / 5)
		for x in range(50, screen_size + 50, self.cell_size):
			for y in range(50, screen_size + 50, self.cell_size):
				self.draw_cell(x, y)
				idx = int(y / self.cell_size) * 3 + int(x / self.cell_size)
				if self.field[idx] == 'o':
					pygame.draw.circle(self.screen, 'Black', 
						(x + self.cell_size / 2, y + self.cell_size / 2), 
						(self.cell_size - dst) / 2, 3)
				if self.field[idx] == 'x':
					pygame.draw.line(self.screen, 'Black', (x + dst, y + dst),
		      			(x + self.cell_size - dst, y + self.cell_size - dst), 3)
					pygame.draw.line(self.screen, 'Black', (x + self.cell_size - dst, y + dst),
		      			(x + dst, y + self.cell_size - dst), 3)
	
	def draw_cell(self, x, y):
		pygame.draw.aaline(self.screen, 'Black', (x, y), (x + self.cell_size, y), 10)
		pygame.draw.aaline(self.screen, 'Black', (x, y), (x, y + self.cell_size), 10)
		pygame.draw.aaline(self.screen, 'Black', (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size), 10)
		pygame.draw.aaline(self.screen, 'Black', (x, y + self.cell_size), (x + self.cell_size, y + self.cell_size), 10)

	def add_symbol(self, mx, my):
		if (mx < 50 or mx > 50 + screen_size or my < 50 or my > 50 + screen_size):
			return
		j, i = int((mx - 50) / self.cell_size), int((my - 50) / self.cell_size)
		if self.field[i * 3 + j] == '.':
			self.field[i * 3 + j] = self.player
		else: return
		if self.player == 'x': self.player = 'o'
		else: self.player = 'x'
		
	def check_field_state(self):
		for i in range(3):
			if self.field[i * 3] != '.' and self.field[i * 3] == self.field[i * 3 + 1]\
					and self.field[i * 3 + 1] == self.field[i * 3 + 2]:
				return self.field[i * 3]
		for i in range(3):
			if self.field[i] != '.' and self.field[i] == self.field[i + 3]\
					and self.field[i + 3] == self.field[i + 6]:
				return self.field[i]
		if self.field[0] != '.' and self.field[4] == self.field[0]\
				and self.field[0] == self.field[8]:
			return self.field[0]
		if self.field[2] != '.' and self.field[4] == self.field[2]\
				and self.field[2] == self.field[6]:
			return self.field[2]
		if self.field.count('.') == 0:
			return '.'
		return None


	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 and self.player == 'x':
					self.add_symbol(event.pos[0], event.pos[1])
						
					
	def message(self, state):
		font = pygame.font.SysFont(None, 100)
		text = f'{state} win!!!'
		if state == '.':
			text = 'Draw!!!'
		surf = font.render(text, False, 'Black')
		rect = surf.get_rect()
		rect.topleft = (50, screen_size + 60)
		self.screen.blit(surf, rect)
					
	def update_screen(self):
		self.screen.fill('White')
		self.draw_field()
		pygame.display.update()

if __name__ == '__main__':
	g = Game()
	g.run()