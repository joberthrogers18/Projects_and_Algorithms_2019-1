import pygame, sys 
import time
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT

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

def is_valid_position(matrix, row, column):
    if not(column>= 0 and column < 10 and row < 20):
        return False
    if (matrix[row][column] != '.'):
        return False
    
    return True

def listen_to_user_input(matrix, piece):
    for event in pygame.event.get():
        if event.type == KEYDOWN:     
            if(event.key == K_LEFT):
                if(is_valid_position(matrix, piece['row'], piece['column'] - 1)):
                    piece['column'] -= 1

            if(event.key == K_RIGHT):
                if(is_valid_position(matrix, piece['row'], piece['column'] + 1)):
                    piece['column'] += 1

def remove_completed_lines(matrix):
    num_lines_removed = 0

    for row in range(len(matrix)):
        if(line_is_completed(matrix, row)):
            for row_to_move_down in range(row, 0, -1):
                for column in range(10):
                    matrix[row_to_move_down][column] = matrix[row_to_move_down - 1][column]
            
            for x in range(10):
                matrix[0][x] = '.'
            num_lines_removed += 1
    return num_lines_removed

def line_is_completed(matrix, row):
    
    for column in range(10):
        if matrix[row][column] == '.':
            return False

    return True

def draw_score(screen, score):
    font = pygame.font.Font('freesansbold.ttf', 20) 
    text = font.render('Score: ' + str(score), True, WHITE)
    screen.blit(text, (400, 50))
    

def run_tetris_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('My Tetris')

    game_matrix = create_game_matrix()
    
    last_time_piece_moved = time.time()
    piece = create_piece()
    score = 0

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
            [100, 50, 10*20 + 10, 20*20 + 10], 
            5
        )

        draw_board(screen, game_matrix)
        draw_score(screen, score)

        listen_to_user_input(game_matrix, piece)

        if(piece['row'] == 19 or game_matrix[piece['row'] + 1][piece['column']] != '.'):
            game_matrix[piece['row']][piece['column']] = 'c'
            lines_removed = remove_completed_lines(game_matrix)
            score += lines_removed
            piece = create_piece()


        pygame.display.update()
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()


if __name__ ==  '__main__':
    run_tetris_game()