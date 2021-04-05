import pygame
import sys
import time

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 635

# Start pygame and create initial window
pygame.init()
size = width, height = WIDTH, WIDTH
SCREEN = pygame.display.set_mode(size)

ROWS, COLS = 15, 15

OFFSET = 20
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
        pygame.draw.rect(screen, self.colour, rect)
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

# graphically show the board i.e. draw all the board's rectangles
def drawBoard(boardToDraw, screen):
    for row in boardToDraw:
        for node in row:
            rect = node.draw(screen)
            # draw gaps between nodes
            pygame.draw.rect(screen, BLACK, rect, 1)

# find row and column based on mouse position
def findClickedSquare(mousePosition):
    gap = (WIDTH - OFFSET) // COLS
    # N.B. technically x and y should be the reverse here but doing it like this for more natural orientation
    x_pos = (mousePosition[0] - OFFSET) // gap
    y_pos = (mousePosition[1] - OFFSET) // gap

    return (x_pos, y_pos)


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

        # create the board
        board = createBoard()
        # draw the created board
        drawBoard(board, SCREEN)

        # check where the board has been pressed
        if mouse:
            clicked_x, clicked_y = findClickedSquare(mouse)
            clickedNode = board[clicked_x][clicked_y]
            clickedNode.colour = (0, 255, 0)
            clickedNode.draw(SCREEN)


        pygame.display.flip()

main(SCREEN, WIDTH)
