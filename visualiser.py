import pygame
import sys
import time
from algorithms import *

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 635
WIDTH_FOR_BUTTONS = 800

# Start pygame and create initial window
pygame.init()
size = width, height = WIDTH_FOR_BUTTONS, WIDTH_FOR_BUTTONS
SCREEN = pygame.display.set_mode(size)

ROWS, COLS = 15, 15

OFFSET = 20
CELL_SIZE = 40

# frontier code borrowed from CS50 AI coursework
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return state in self.frontier

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class Node:
    def __init__(self, row, col, cell_size):
        self.col = col
        self.row = row
        self.x = OFFSET + row * cell_size
        self.y = OFFSET + col * cell_size
        self.colour = WHITE
        self.neighbours = []
        self.parent = None
        #self.actualNeighbours = list(set(self.neighbours))

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, self.colour, rect)
        return rect

    def isWall(self):
        return self.colour == BLACK

    def isStart(self):
        return self.colour == (0, 255, 0)

    def isEnd(self):
        return self.colour == (0, 0, 255)

    def getNeighbours(self, board):
        row = self.row
        col = self.col

        # get right neigh.
        if self.col <= COLS - 2 and not board[row][col + 1].isWall():
            self.neighbours.append(board[row][col + 1])
        # get left neigh.
        if self.col >= 1 and not board[row][col - 1].isWall():
            self.neighbours.append(board[row][col - 1])
        # get up neigh.
        if self.row >= 1 and not board[row - 1][col].isWall():
            self.neighbours.append(board[row - 1][col])
        # get down neigh.
        if self.row <= ROWS - 2 and not board[row + 1][col].isWall():
             self.neighbours.append(board[row + 1][col])

class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

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
    screen.fill(WHITE)
    # draw node squares on the board
    for row in boardToDraw:
        for node in row:
            rect = node.draw(screen)
            # draw gaps between nodes
            pygame.draw.rect(screen, BLACK, rect, 1)

    coord = OFFSET + (COLS * CELL_SIZE) + COLS + 20
    # draw button on board
    button = pygame.Rect(coord, OFFSET, 120, 60)
    pygame.draw.rect(screen, (211, 211, 211), button)

    # DELETE THIS LINE IF IT BREAKS STUFF
    pygame.time.wait(50)
    pygame.display.update()

# find row and column based on mouse position
def findClickedSquare(mousePosition):
    gap = (WIDTH - OFFSET) // COLS
    # N.B. technically x and y should be the reverse here but doing it like this for more natural orientation
    x_pos = (mousePosition[0] - OFFSET) // gap
    y_pos = (mousePosition[1] - OFFSET) // gap

    return (x_pos, y_pos)

def visualisePath(board, current):
    nodesToVisualise = []
    while current.parent != None:
        nodesToVisualise.append(current)
        current = current.parent

    nodesToVisualise.reverse()

    for node in nodesToVisualise:
        node.colour = (255, 255, 0)
        drawBoard(board, SCREEN)

def DFS(board, start, end):

    frontier = StackFrontier()
    frontier.add(start)
    explored = set()

    while not frontier.empty():
        # a pygame failsafe for quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        current = frontier.remove()
        explored.add(current)
        current.colour = (255, 165, 0)
        if current.row == end.row and current.col == end.col:
            visualisePath(board = board, current = current)
            return True
        else:
            # generate neighbours of current node
            current.getNeighbours(board)

            for neighbour in current.neighbours:
                if neighbour not in explored:
                    frontier.add(neighbour)
                    neighbour.parent = current
        drawBoard(board, SCREEN)

    # return False if no more neighbours to consider and we haven't returned a path yet
    return False

def BFS(board, start, end):

    frontier = QueueFrontier()
    frontier.add(start)
    explored = set()

    while not frontier.empty():
        # a pygame failsafe for quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        current = frontier.remove()
        print(current.row, current.col)
        explored.add(current)
        current.colour = (255, 165, 0)
        if current.row == end.row and current.col == end.col:
            visualisePath(board = board, current = current)
            return True
        else:
            # generate neighbours of current node
            current.getNeighbours(board)

            for neighbour in current.neighbours:
                if neighbour not in explored and not frontier.contains_state(neighbour):
                    frontier.add(neighbour)
                    neighbour.parent = current
        drawBoard(board, SCREEN)

    # return False if no more neighbours to consider and we haven't returned a path yet
    return False


def main(screen, width):
    # create the board
    board = createBoard()
    startNode = None
    endNode = None

    while True:
        # draw the created board
        drawBoard(board, SCREEN)
        # Check if game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # left button mouse click
            if pygame.mouse.get_pressed()[0]:
                mouse = pygame.mouse.get_pos()
                clicked_x, clicked_y = findClickedSquare(mouse)
                clickedNode = board[clicked_x][clicked_y]
                # if no startNode yet, make the first node clicked the start node
                if startNode == None and clickedNode != endNode:
                    startNode = clickedNode
                    startNode.colour = (0, 255, 0)
                elif endNode == None and clickedNode != startNode:
                    endNode = clickedNode
                    clickedNode.colour = (0, 0, 255)
                elif startNode and endNode and clickedNode != startNode and clickedNode != endNode:
                    clickedNode.colour = BLACK
                    #clickedNode.getNeighbours(board)

                clickedNode.draw(SCREEN)

            # keyboard press
            if event.type == pygame.KEYDOWN:
                print("Finding path...")
                algo = DFS(board, startNode, endNode)
                if algo == False:
                    print("Something went wrong")
                else:
                    print(algo)
        pygame.display.flip()

main(SCREEN, WIDTH)
