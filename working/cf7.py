#M x N , they are inputs that says how big is the rectangular board I am dealing with
def dominoes_placer(rectangular_board):
    domino_area = 2 * 1 #area of a domino's piece
    rectangular_board_area = rectangular_board[0] * rectangular_board[1]
    return int(rectangular_board_area/domino_area)
#user inputs
rectangular_board = list(map(int,input().split(" ")))
print(dominoes_placer(rectangular_board))