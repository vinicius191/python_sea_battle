import pygame

class Grid:

    def __init__(self, blockSize, xStart, yStart, color, win, **kwargs):
        self.sizeY = kwargs.get('size', None)[0]
        self.sizeX = kwargs.get('size', None)[1]
        self.blockSize = blockSize
        self.xStart = xStart
        self.yStart = yStart
        self.color = color
        self.win = win
        self.kwargs = kwargs

    def make_grid(self):
        map = []
        top_gap = self.yStart
        for y in range(self.sizeY):
            row = []
            left_gap = self.xStart
            if y > 0:
                top_gap += self.blockSize[1] + 2
            for x in range(self.sizeX):
                if x > 0:
                    left_gap += self.blockSize[0] + 2
                rect = (left_gap, top_gap, self.blockSize[0], self.blockSize[1])
                row.append(rect)
            map.append(row)
        return map

    def draw(self):
        g_ = []
        grid = self.make_grid()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                d_ = None
                d_ = pygame.draw.rect(self.win, self.color, grid[row][col], 1)
                g_.append([d_, [row, col], self.kwargs.get('alias', None)])

        return g_
    
    def draw_ships_list(self):
        rect = (self.xStart, self.yStart, self.blockSize[0], self.blockSize[1])
        pygame.draw.rect(self.win, self.color, rect, 1)