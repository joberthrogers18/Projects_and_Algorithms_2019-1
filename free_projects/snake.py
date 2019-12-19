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

def create_piece():
    piece = {}
    piece['row'] = 0
    piece['col'] = 0

    return piece 

def draw_board(screen, matrix):
    for row in range(29):
        for col in range(29):
            if matrix[row][col] == 'c':
                draw_single_piece(screen, matrix, col, row)

def listen_input_user(matrix, row, col):

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                matrix[row][col] = "."
                col -= 1
                matrix[row][col] = 'c'
            if event.key == K_RIGHT:
                matrix[row][col] = "."
                col += 1
                matrix[row][col] = 'c'
            if event.key == K_UP:
                matrix[row][col] = "."
                row -= 1
                matrix[row][col] = 'c'
            if event.key == K_DOWN:
                matrix[row][col] = "."
                row += 1
                matrix[row][col] = 'c'
    
    return row, col

def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake game')

    last_time_updated = time.time()
    piece = create_piece()

    matrix = create_matrix()
    # 0 is horizontal and 1 is vertical
    direction = 0

    current_row = 0
    current_col = 0

    matrix[0][0] = 'c'

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE,  [5, 5, 700, 700], 3)

        draw_axis(screen)

        # if( time.time() - last_time_updated > 0.5 ):
        #     last_time_updated = time.time()
            
        current_row, current_col = listen_input_user(matrix, current_row, current_col)
        
        draw_board(screen, matrix)

        pygame.display.flip()
        


if __name__ == '__main__':
    run()