import numpy as np
import pygame
import sys
import tensorflow as tf
import time

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Start pygame
pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)


ROWS, COLS = 28, 28

OFFSET = 20
CELL_SIZE = 10

handwriting = [[0] * COLS for _ in range(ROWS)]
classification = None

while True:

    # Check if game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)

    # Check for mouse press
    # click, _, _ = pygame.mouse.get_pressed()
    # if click == 1:
    #     mouse = pygame.mouse.get_pos()
    # else:
    #     mouse = None

    # Draw each grid cell
    cells = []
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            rect = pygame.Rect(
                OFFSET + j * CELL_SIZE,
                OFFSET + i * CELL_SIZE,
                CELL_SIZE, CELL_SIZE
            )

            # If cell has been written on, darken cell
            # if handwriting[i][j]:
            #     channel = 255 - (handwriting[i][j] * 255)
            #     pygame.draw.rect(screen, (channel, channel, channel), rect)

            # Draw blank cell
            #else:
            # this draws the cell rectangles
            pygame.draw.rect(screen, WHITE, rect)
            # this draws the gaps between cell rectangles
            pygame.draw.rect(screen, BLACK, rect, 1)

            # If writing on this cell, fill in current cell and neighbors
            # if mouse and rect.collidepoint(mouse):
            #     handwriting[i][j] = 250 / 255
            #     if i + 1 < ROWS:
            #         handwriting[i + 1][j] = 220 / 255
            #     if j + 1 < COLS:
            #         handwriting[i][j + 1] = 220 / 255
            #     if i + 1 < ROWS and j + 1 < COLS:
            #         handwriting[i + 1][j + 1] = 190 / 255



    pygame.display.flip()
