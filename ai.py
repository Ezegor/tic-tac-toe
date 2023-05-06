
from random import randint

def find_best_turn(player, field : list):
	best_field = field[:]
	x = -100
	for i in range(len(field)):
		if field[i] == '.':
			field[i] = player
			y = rec(player, change(player), field)
			if x < y:
				x = y
				best_field = field[:]
			field[i] = '.'
	return best_field
            

def rec(player, cur_player, field):
	s = check_field_state(field)
	if s:
		if s == player:
			return 10
		elif s != '.':
			return -10
		else:
			return 0
	if player == cur_player: x = -10
	else: x = 10
	for i in range(len(field)):
		if field[i] == '.':
			field[i] = cur_player
			y = rec(player, change(cur_player), field)
			if player == cur_player:
				x = max(x, y)
			else:
				x = min(x, y)
			field[i] = '.'
	return x
		
def change(cur_player):
	if cur_player == 'o': return 'x'
	else: return 'o'


	
	
	
def check_field_state(field):
		for i in range(3):
			if field[i * 3] != '.' and field[i * 3] == field[i * 3 + 1]\
					and field[i * 3 + 1] == field[i * 3 + 2]:
				return field[i * 3]
		for i in range(3):
			if field[i] != '.' and field[i] == field[i + 3]\
					and field[i + 3] == field[i + 6]:
				return field[i]
		if field[0] != '.' and field[4] == field[0]\
				and field[0] == field[8]:
			return field[0]
		if field[2] != '.' and field[4] == field[2]\
				and field[2] == field[6]:
			return field[2]
		if field.count('.') == 0:
			return '.'
		return None