data = ['_'] * 9


def get_playing_field(coll):
	print('---------')
	print(f'| {coll[0]} {coll[1]} {coll[2]} |')
	print(f'| {coll[3]} {coll[4]} {coll[5]} |')
	print(f'| {coll[6]} {coll[7]} {coll[8]} |')
	print('---------')


def get_game(coll, count=1):
	def user_data(data_user):
		result = ''
		if data_user == ['1', '1']:
			result = coll[6]
		if data_user == ['1', '2']:
			result = coll[3]
		if data_user == ['1', '3']:
			result = coll[0]
		if data_user == ['2', '1']:
			result = coll[7]
		if data_user == ['2', '2']:
			result = coll[4]
		if data_user == ['2', '3']:
			result = coll[1]
		if data_user == ['3', '1']:
			result = coll[8]
		if data_user == ['3', '2']:
			result = coll[5]
		if data_user == ['3', '3']:
			result = coll[2]
		return result
	
	def get_new_data_x(data_user):
		if data_user == ['1', '1']:
			coll[6] = 'X'
		if data_user == ['1', '2']:
			coll[3] = 'X'
		if data_user == ['1', '3']:
			coll[0] = 'X'
		if data_user == ['2', '1']:
			coll[7] = 'X'
		if data_user == ['2', '2']:
			coll[4] = 'X'
		if data_user == ['2', '3']:
			coll[1] = 'X'
		if data_user == ['3', '1']:
			coll[8] = 'X'
		if data_user == ['3', '2']:
			coll[5] = 'X'
		if data_user == ['3', '3']:
			coll[2] = 'X'
		return coll
	
	def get_new_data_o(data_user):
		if data_user == ['1', '1']:
			coll[6] = 'O'
		if data_user == ['1', '2']:
			coll[3] = 'O'
		if data_user == ['1', '3']:
			coll[0] = 'O'
		if data_user == ['2', '1']:
			coll[7] = 'O'
		if data_user == ['2', '2']:
			coll[4] = 'O'
		if data_user == ['2', '3']:
			coll[1] = 'O'
		if data_user == ['3', '1']:
			coll[8] = 'O'
		if data_user == ['3', '2']:
			coll[5] = 'O'
		if data_user == ['3', '3']:
			coll[2] = 'O'
		return coll
	
	def is_winner(char):
		winner = [char] * 3
		if coll[0:3] == winner or coll[3:6] == winner or coll[6:9] == winner:
			return True
		if coll[0:7:3] == winner or coll[1:8:3] == winner or coll[2:9:3] == winner:
			return True
		if coll[0:9:4] == winner or coll[2:8:2] == winner:
			return True
		return False
	
	def get_game_state(switch):
		if is_winner('O'):
			print('O wins')
			return start_stop(0)
		if is_winner('X'):
			print('X wins')
			return start_stop(0)
		if '_' not in coll:
			print('Draw')
			return start_stop(0)
		
		return start_stop(switch)
	
	def get_move_x():
		data_user = input('Enter the coordinates: ').split()
		
		for item in data_user:
			if not item.isdigit():
				print('You should enter numbers!')
				return get_move_x()
			elif int(item) > 3:
				print('Coordinates should be from 1 to 3!')
				return get_move_x()
		
		if user_data(data_user) != '_':
			print('This cell is occupied! Choose another one!')
			return get_move_x()
		else:
			get_playing_field(get_new_data_x(data_user))
		
		get_game_state(2)
	
	def get_move_o():
		data_user = input('Enter the coordinates: ').split()
		
		for item in data_user:
			if not item.isdigit():
				print('You should enter numbers!')
				return get_move_o()
			elif int(item) > 3:
				print('Coordinates should be from 1 to 3!')
				return get_move_o()
		
		if user_data(data_user) != '_':
			print('This cell is occupied! Choose another one!')
			return get_move_o()
		else:
			get_playing_field(get_new_data_o(data_user))
		
		get_game_state(1)
	
	def start_stop(switch):
		if switch == 1:
			return get_move_x()
		if switch == 2:
			return get_move_o()
		if switch == 0:
			return
	
	start_stop(count)


get_playing_field(data)
get_game(data)
