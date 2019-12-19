import pygame, sys
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED_DARK = (164, 73, 73)
WIDTH = 710
HEIGHT = 710

# def draw_rect(screen, width, height, position_x, position_y):
#     pygame.draw.rect(screen, WHITE, [width, height, position_x, position_y], 3)

def draw_axis(screen):

    for i in range(1, 29):
        pygame.draw.line(screen, WHITE, [ 8 + i *24, 5 ], [ 8 + i*24, 700], 1)

    for i in range(1, 29):
        pygame.draw.line(screen, WHITE, [ 5, 8 + i *24 ], [ 700, 8 + i*24 ], 1)

def draw_single_piece(screen, piece):
    pygame.draw.rect(screen, RED_DARK, [ 10 + 24*piece['col'], 10 + 24*piece['row'], 21, 21])

def create_piece():
    piece = {}
    piece['row'] = 0
    piece['col'] = 0

    return piece 

def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake game')

    last_time_updated = time.time()
    piece = create_piece()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if( time.time() - last_time_updated > 0.5 ):
            last_time_updated = time.time()
            piece['row'] += 1
            piece['col'] += 1

        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE,  [5, 5, 700, 700], 3)

        draw_axis(screen)
        draw_single_piece(screen, piece)

        pygame.display.flip()
        


if __name__ == '__main__':
    run()