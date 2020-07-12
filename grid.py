import pygame
import numpy as np
import string

class Grid:

    pygame.font.init()
    axis_title = pygame.font.Font("fonts/Vollkorn-Bold.ttf", 14)

    def __init__(self, blockSize, x, y, color, win, **kwargs):
        self.sizeY = kwargs.get('size', None)[0]
        self.sizeX = kwargs.get('size', None)[1]
        self.blockSize = blockSize
        self.x = x
        self.y = y
        self.color = color
        self.win = win
        self.kwargs = kwargs
        self.grid = []
        self.x_labels = string.ascii_uppercase[:10]
        self.y_labels = [i for i in range(1, 11)]

        print(len(self.y_labels))

    def make_grid(self):
        map = []
        top_gap = self.y
        for y in range(self.sizeY):
            row = []
            left_gap = self.x
            if y > 0:
                top_gap += self.blockSize[1] + (-1) # (-1 is an extra gap if needed change it to 2+)
            for x in range(self.sizeX):
                if x > 0:
                    left_gap += self.blockSize[0] + (-1) # (-1 is an extra gap if needed change it to 2+)
                rect = (left_gap, top_gap, self.blockSize[0], self.blockSize[1])
                row.append(rect)
            map.append(row)
        return map

    def draw(self):
        g_ = []
        self.grid = self.make_grid()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                d_ = None
                rect_ = self.grid[row][col]
                d_ = pygame.draw.rect(self.win, self.color, self.grid[row][col], 1)
                g_.append([d_, [row, col], self.kwargs.get('alias', None)])

        return g_
    
    def draw_grid_labels(self, grid):
        np_grid = np.array(grid)
        for index, element in enumerate(np_grid[0:10, :]):
            x_text = self.axis_title.render(self.x_labels[index], True, (0, 0, 0))
            self.win.blit(x_text, (element[0][0] + 12, element[0][1] - 25))
            
        if grid[0][2] == 'Player':
            for index, element in enumerate(np_grid[:, :10][:10]):
                y_text = self.axis_title.render(str(self.y_labels[index]), True, (0, 0, 0))
                self.win.blit(y_text, (40, element[0][0] + 65))
        else:
            for index, element in enumerate(np_grid[:, :10][-10:]):
                y_text = self.axis_title.render(str(self.y_labels[index]), True, (0, 0, 0))
                self.win.blit(y_text, (780, element[0][0] - 315))
        
    def draw_ships_list(self):
        rect = (self.x, self.y, self.blockSize[0], self.blockSize[1])
        pygame.draw.rect(self.win, self.color, rect, 1) 