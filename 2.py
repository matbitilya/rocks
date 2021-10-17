# N = input('enter N: ')
# M = input('enter M: ')
import timeit

def draw_board():
    global board
    for line in transpose(board):
        print(*line)

def transpose(matr):
    res=[]
    n=len(matr)
    m=len(matr[0])
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp=tmp+[matr[i][j]]
        res=res+[tmp]
    return res  

N, M = 10, 10

board = [['.' for _ in range(M)] for _ in range(N)]
turn = True

def fill(y1, y2, x):
    for y in range(y1 + 1, y2):

        global board, turn
        if turn:
            rock_color = 'W'
        else:
            rock_color = 'B'

        if board[x][y] != rock_color:
            board[x][y] = rock_color


def check_column(rock_color, x_placed, y_placed):
        y1, y2 = None, None
        for y, rock in enumerate(board[x_placed]):
            if rock == rock_color:
                if y1 == None:
                    y1 = y
                elif y2 == None:
                    y2 = y
                    fill(y1, y2, x_placed)
                    break

        x1, x2 = None, None
        for y, rock in enumerate(board[y_placed]):
            if rock == rock_color:
                if x1 == None:
                    x1 = y
                elif x2 == None:
                    x2 = y
                    fill(x1, x2, y_placed)
                    break        

def chech_rock(x, y):
    global board, turn
    if turn:
        rock_color = 'W'
    else:
        rock_color = 'B'
    
    if board[x][y] == '.':
        board[x][y] = rock_color

        
        board = transpose(board)
        check_column(rock_color, x, y)
        board = transpose(board)
        check_column(rock_color, x, y)


        draw_board()
        turn = not turn
    else:
        print('error: field is taken')

def input_xy():
    return [int(number) - 1 for number in input('Enter: ').split(' ')]




def count():
    global board
    white_count = 0
    black_count = 0

    for column in board:
        for n in column:
            if n == 'W':
                white_count += 1
            elif n == 'B':
                black_count += 1
    print(f'white has {white_count - black_count} more rocks')

def main():
    x, y = input_xy()

    while x != -1 and y != -1:
        chech_rock(x, y)
        count()
        
        x, y = input_xy()

main()