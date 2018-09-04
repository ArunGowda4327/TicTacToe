from program import *


print('WELCOME TO TIC TAC TOE')

while True:

	theboard = [' ']*10
	player1_marker,player2_marker = marker_func()
	turn = who_is_first()
	print('----------------\n')
	print(turn + 'is going to play first\n')
	print('----------------\n')

	while True:
		if turn == 'player1':
			display_board(theboard)
			position = selsect_position(theboard)
			mark_position(theboard, position, player1_marker)

			if win_check(theboard, player1_marker):
				display_board(theboard)
				print('PLAYER 1 WON')
				break

			else:
				if board_check(theboard):
					display_board(theboard)
					print('TIE MATCH')
					break
				else:
					turn = 'player2'







		else:
			display_board(theboard)
			position = selsect_position(theboard)
			mark_position(theboard, position, player2_marker)

			if win_check(theboard, player2_marker):
				display_board(theboard)
				print('PLAYER 2 WON')
				break

			else:
				if board_check(theboard):
					display_board(theboard)
					print('TIE MATCH')
					break
				else:
					turn = 'player1'





	if not replay():
		break
