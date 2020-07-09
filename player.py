import pygame
import grid as Grid
import constants
import log as Log


class Player:

    pygame.font.init()
    title_font = pygame.font.Font("fonts/Vollkorn-Bold.ttf", 40)

    def __init__(self, alias, canvas, blockSize, xStart, yStart, win, **kwargs):
        self.alias = alias
        self.size = kwargs.get('size', None)
        self.canvas = canvas
        self.blockSize = blockSize
        self.xStart = xStart
        self.yStart = yStart
        self.grid = []
        self.win = win
        self.color = (0, 0, 0)
        self.g_ = None
        self.grid = Grid.Grid(self.blockSize, self.xStart, self.yStart, self.color, self.win, size=self.size, alias=self.alias) 
    
    def draw_grid(self):
        grid = Grid.Grid(self.blockSize, self.xStart, self.yStart, self.color, self.win, size=self.size, alias=self.alias)
        self.g_ = grid.draw()

    def draw_grid_labels(self):
        self.grid.draw_grid_labels(self.g_)

    def draw_title_message(self, txt):
        text = self.title_font.render(txt, True, constants.PLAYER_TITLE_COLOR)
        self.win.blit(text, (self.xStart + 20, self.yStart - 80))


    def collide_check(self, pos):
        '''
        Check for collision on the grid (Player or Enemy)

        Args:
            pos (touple): Coordinates clicked by users mouse (x,y)

        Returns:
            The coordinates of the grid
        '''
        for rect in self.g_:
            if rect[0].collidepoint(pos):
                collide_to = 'Collide to ' + str(self.alias) + ' on '+ str(pos)
                position = str(rect[1][0]) + ', ' + str(rect[1][1])
                print(collide_to + ' at x, y = ' + position)

                log = Log.Log(self.win, 550, 510)
                log.show_message(self.win, attacker='Player', defender='Enemy', type='HIT', position=position)

                break 
