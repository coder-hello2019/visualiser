import pygame
import sys
import time

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 800

# Start pygame and create initial window
pygame.init()
size = width, height = WIDTH, WIDTH
SCREEN = pygame.display.set_mode(size)

ROWS, COLS = 20, 20

OFFSET = 80
CELL_SIZE = 40

class Node:
    def __init__(self, row, col, cell_size):
        self.col = col
        self.row = row
        self.x = OFFSET + row * cell_size
        self.y = OFFSET + col * cell_size
        self.colour = WHITE
        self.neighbors = []

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(scren, self.color, rect)
        return rect

# generate board elements for board of specified size
def createBoard():
    # list of lists to hold each row full of nodes
    nodes = []
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            node = Node(row=i, col = j, cell_size = CELL_SIZE)
            row.append(node)
        nodes.append(row)
    return nodes

def drawBoard(boardToDraw, screen):
    for row in boardToDraw:
        for node in row:
            rect = node.draw()
            # draw gaps between nodes
            pygame.draw.rect(screen, BLACK, rect, 1)


def main(screen, width):
    while True:

        # Check if game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # screen background
        screen.fill(WHITE)

        # Check for mouse press
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
        else:
            mouse = None

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

                channel = (0, 255, 0)
                pygame.draw.rect(screen, channel, rect)

                # this draws the gaps between cell rectangles
                pygame.draw.rect(screen, BLACK, rect, 1)


                # If writing on this cell, fill in current cell and neighbors
                if mouse and rect.collidepoint(mouse):
                    print(mouse)

        pygame.display.flip()

main(SCREEN, WIDTH)
