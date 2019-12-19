import pygame, sys 
import time
from pygame.locals import QUIT, KEYUP, K_ESCAPE

BLUE = (0, 0, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (217, 222, 226)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def create_game_matrix():
    game_matrix_columns = 10
    game_matrix_rows =20
    matrix = []

    for row in range(game_matrix_rows):
        new_row = []
        for column in range(game_matrix_columns):
            new_row.append('.')
        
        matrix.append(new_row)

    return matrix

def create_piece():
    piece = {}
    piece['row'] = 0
    piece['column'] = 4
    return piece

def draw_piece(screen, piece):

    # board margin + line thickeness + ( column * box-sizing )
    origin_x = 100 + 5 + ( piece['column']*20 + 1)
    origin_y = 50 + 5 + ( piece['row']*20 + 1)
    pygame.draw.rect(screen, GREY, [origin_x, origin_y, 20, 20])
    pygame.draw.rect(screen, WHITE, [origin_x, origin_y, 18, 18])

    return

def draw_board(screen, matrix):
    game_matrix_columns = 10
    game_matrix_rows =20
    
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if(matrix[row][column] == 'c'):
                origin_x = 100 + 5 + ( column*20 + 1)
                origin_y = 50 + 5 + ( row*20 + 1)
                pygame.draw.rect(screen, GREY, [origin_x, origin_y, 20, 20])
                pygame.draw.rect(screen, WHITE, [origin_x, origin_y, 18, 18])


def run_tetris_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('My Tetris')

    game_matrix = create_game_matrix()
    
    last_time_piece_moved = time.time()
    piece = create_piece()

    while True:
        screen.fill(BLACK)

        if(time.time() - last_time_piece_moved > 1 ):
                piece['row'] += 1
                last_time_piece_moved = time.time()

        draw_piece(screen, piece)

        # The list bellow, is an rectangle 100X50 is a position X and Y
        # The other values are the width and height of rectangle in list
        # The number 5 alone is the width of border of rectangle
        pygame.draw.rect(
            screen,
            BLUE,
            [100, 50, 10*20, 20*20 + 10], 
            5
        )

        draw_board(screen, game_matrix)

        if(piece['row'] == 19 or game_matrix[piece['row'] + 1][piece['column']] != '.'):
            game_matrix[piece['row']][piece['column']] = 'c'
            piece = create_piece()

        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()


if __name__ ==  '__main__':
    run_tetris_game()