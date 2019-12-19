import pygame, sys
import time
import random
from pygame.locals import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED_DARK = (164, 73, 73)
WIDTH = 710
HEIGHT = 710

def create_matrix():
    matrix = []

    for row in range(29):
        new_row = []
        for col in range(29):
            new_row.append('.')
        
        matrix.append(new_row)

    return matrix


def draw_axis(screen):

    for i in range(1, 29):
        pygame.draw.line(screen, WHITE, [ 8 + i *24, 5 ], [ 8 + i*24, 700], 1)

    for i in range(1, 29):
        pygame.draw.line(screen, WHITE, [ 5, 8 + i *24 ], [ 700, 8 + i*24 ], 1)

def draw_single_piece(screen, matrix, col, row):
    pygame.draw.rect(screen, RED_DARK, [ 10 + 24*col, 10 + 24*row, 21, 21])

def draw_board(screen, matrix):
    for row in range(29):
        for col in range(29):
            if matrix[row][col] == 'c':
                draw_single_piece(screen, matrix, col, row)

def listen_input_user(matrix, row, col, direction):

    is_pressed = False

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            is_pressed = True
            if event.key == K_LEFT and is_valid_position(row, col - 1):
                matrix[row][col] = "."
                col -= 1
                matrix[row][col] = 'c'
                direction = 0
            if event.key == K_RIGHT and is_valid_position(row, col + 1):
                matrix[row][col] = "."
                col += 1
                matrix[row][col] = 'c'
                direction = 1
            if event.key == K_UP and is_valid_position(row - 1, col):
                matrix[row][col] = "."
                row -= 1
                matrix[row][col] = 'c'
                direction = 2
            if event.key == K_DOWN and is_valid_position(row + 1, col):
                matrix[row][col] = "."
                row += 1
                matrix[row][col] = 'c'
                direction = 3
    
    return row, col, direction, is_pressed

def is_valid_position(row, col):
    if row >=0 and row < 29 and col >= 0 and col < 29:
        return True

    return False
    

def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake game')

    last_time_updated = time.time()
    # piece = create_piece()

    matrix = create_matrix()

    direction = 1

    current_row = 0
    current_col = 0

    matrix[0][0] = 'c'
    is_pressed = False

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE,  [5, 5, 700, 700], 3)

        draw_axis(screen)

        current_row, current_col, direction, is_pressed = listen_input_user(matrix, current_row, current_col, direction)

        if( time.time() - last_time_updated > 0.7 and not is_pressed ):
            last_time_updated = time.time()
            
            if direction == 0 and is_valid_position(current_row, current_col - 1):
                matrix[current_row][current_col] = '.'
                matrix[current_row][current_col - 1] = 'c'
                current_col -= 1

            elif direction == 1 and is_valid_position(current_row, current_col + 1):
                matrix[current_row][current_col] = '.'
                matrix[current_row][current_col + 1] = 'c'
                current_col += 1

            elif direction == 2 and is_valid_position(current_row - 1, current_col ):
                matrix[current_row][current_col] = '.'
                matrix[current_row - 1][current_col] = 'c'
                current_row -= 1

            elif direction == 3 and is_valid_position(current_row + 1, current_col):
                matrix[current_row][current_col] = '.'
                matrix[current_row + 1][current_col] = 'c'
                current_row += 1
                        
            time.sleep(0.1)
        
        draw_board(screen, matrix)

        pygame.display.flip()
        

if __name__ == '__main__':
    run()