from IPython.display import clear_output

def display_board(board):
	clear_output()
	print(board[7]+'|'+board[8]+'|'+board[9]+'|')
	print(' ----- ')
	print(board[4]+'|'+board[5]+'|'+board[6]+'|')
	print(' ----- ')
	print(board[1]+'|'+board[2]+'|'+board[3]+'|')


theboard = [' ']*10
#display_board(theboard)





def marker_func():
	marker = ''
	while not marker == 'X' or marker == 'O':
		marker = input('PLAYER 1 : choose your marker')

	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')

#player1,player2 = marker_func()
#print(player2)







import random
def who_is_first():
	flip = random.randint(0,1)
	if flip == 0:
		return 'player1'
	else:
		return 'player2'





def mark_position(board, position, marker):
	board[position] = marker



#mark_position(theboard, 4, '#')
#display_board(theboard)




def win_check(board, mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal






def space_check(board, position):
	return board[position] == ' '






def board_check(board):
	for i in range(1, 10):
		if space_check(board,i):
			return False
	return True





def selsect_position(board):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input('Enter the position to insert your marker myan'))

	return position






def replay():
	choice = input('print y to play again and n to not')
	return choice == 'y'
		


























